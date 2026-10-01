from playwright.sync_api import sync_playwright
from pathlib import Path
import json,csv,time,sys,hashlib,traceback

root=Path(__file__).resolve().parent
html=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root/'air-empire-network-ai-v2.3.0-alpha7.0-ae-cargo-market-clear-standalone.html'
outdir=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else root/'results'
outdir.mkdir(parents=True,exist_ok=True)
seed=20260722
page_errors=[]; console_errors=[]

def js_snapshot(page):
    return page.evaluate(r'''() => {
      const s=window.__AIR_EMPIRE_V221_DEBUG__.getGameState();
      const airlines=s.airlines||[];
      const latest=airlines.map(a=>[a,a.history?.at?.(-1)]).filter(x=>x[1]);
      const n=x=>Number(x)||0;
      const revenue=latest.reduce((z,x)=>z+n(x[1].revenue),0);
      const profit=latest.reduce((z,x)=>z+n(x[1].profit),0);
      const pre=latest.reduce((z,x)=>z+n(x[1].preDividendProfit),0);
      const dividendIncome=latest.reduce((z,x)=>z+n(x[1].subsidiaryDividendIncomeAlpha7)+n(x[1].strategicStakeDividendIncomeAlpha7),0);
      const dividendPaid=latest.reduce((z,x)=>z+n(x[1].stakeDividendPaidAlpha7),0);
      const subs=airlines.filter(a=>a.parentAirlineId);
      const init=s.historicalEntrantInitializationLedgerV700AC||[];
      const closed=s.closedAirlinesArchiveV700AC||[];
      const shells=airlines.filter(a=>['merged','ceased','closed'].includes(String(a.status||'').toLowerCase()));
      const market=s.lastCargoMarketClearV700AE||{};
      const audit=window.__AIR_EMPIRE_V700AE__?.audit?.()||{};
      let cargoRevenue=0,pax=0,paxCap=0;
      for(const [a,st] of latest) for(const r of st.routes||[]){
        cargoRevenue+=n(r.cargoRevenue);
        if((r.routeType||'passenger')==='passenger'&&n(r.paxCarried)>0&&n(r.loadFactor)>0){pax+=n(r.paxCarried);paxCap+=n(r.paxCarried)/Math.max(.0001,n(r.loadFactor));}
      }
      return {
        turn:n(s.turnNumber),year:n(s.year),quarter:n(s.quarter),airlines:airlines.length,subsidiaries:subs.length,
        routes:airlines.reduce((z,a)=>z+(a.routes?.length||0),0),fleet:airlines.reduce((z,a)=>z+(a.fleet?.length||0),0),
        revenue,profit,preDividendProfit:pre,netMargin:revenue?profit/revenue:0,dividendIncome,dividendPaid,
        passengerLF:paxCap?pax/paxCap:0,cargoRevenue,cargoRevenueShare:revenue?cargoRevenue/revenue:0,
        zeroRouteSubs:subs.filter(a=>(a.routes?.length||0)===0).length,zeroFleetSubs:subs.filter(a=>(a.fleet?.length||0)===0).length,
        inactiveShells:shells.length,entrantInitCount:init.length,entrantInitFailures:init.filter(x=>!x.ok).length,
        liquidations:closed.length,marketAdjustedPools:n(market.adjustedPools),marketRemovedKg:n(market.removedKg),marketViolations:n(market.violations),
        cargoRevenueGtTotal:n(audit.cargoRevenueGtTotal),accountingNonFinite:n(audit.accountingNonFinite),auditValid:audit.valid!==false,
        rng:{seed:s.randomSeedV253,state:s.randomStateV253,calls:s.randomCallsV253}
      };
    }''')

def annual_2024(page):
    return page.evaluate(r'''() => {
      const s=window.__AIR_EMPIRE_V221_DEBUG__.getGameState(), n=x=>Number(x)||0;
      const rows=[];let revenue=0,profit=0,cargoRevenue=0,pax=0,paxCap=0;
      for(const a of s.airlines||[]) for(const st of a.history||[]){if(st.year!==2024)continue;revenue+=n(st.revenue);profit+=n(st.profit);for(const r of st.routes||[]){cargoRevenue+=n(r.cargoRevenue);if((r.routeType||'passenger')==='passenger'&&n(r.paxCarried)>0&&n(r.loadFactor)>0){pax+=n(r.paxCarried);paxCap+=n(r.paxCarried)/Math.max(.0001,n(r.loadFactor));}}}
      const groupRoot=(a)=>{let x=a,seen=new Set();while(x?.parentAirlineId&&!seen.has(x.id)){seen.add(x.id);const p=(s.airlines||[]).find(z=>z.id===x.parentAirlineId);if(!p)break;x=p;}return x;};
      const targets=['Qantas','Lufthansa','Emirates','Etihad Airways','EVA Air','China Airlines'];
      const companies={};
      for(const name of targets){const root=(s.airlines||[]).find(a=>a.name===name);if(!root){companies[name]=null;continue;}const members=(s.airlines||[]).filter(a=>groupRoot(a)?.id===root.id);let gr=0,gc=0;for(const a of members)for(const st of a.history||[]){if(st.year!==2024)continue;gr+=n(st.revenue);for(const r of st.routes||[])gc+=n(r.cargoRevenue);}companies[name]={rootId:root.id,members:members.map(a=>a.name),revenue:gr,cargoRevenue:gc,cargoShare:gr?gc/gr:0};}
      const cargoNames=['Lufthansa Cargo','Emirates SkyCargo','Etihad Cargo','EVA Air Cargo','China Airlines Cargo','Qantas Freight'];
      const dedicated={};for(const name of cargoNames){const a=(s.airlines||[]).find(x=>x.name===name);dedicated[name]=a?{id:a.id,routes:a.routes?.length||0,fleet:a.fleet?.length||0,status:a.status||a.operatingStatusV600B62||'active'}:null;}
      return {revenue,profit,netMargin:revenue?profit/revenue:0,cargoRevenue,cargoRevenueShare:revenue?cargoRevenue/revenue:0,passengerLF:paxCap?pax/paxCap:0,companies,dedicated};
    }''')

start=time.time(); quarter_totals=[]; checkpoints=[]; error=None
try:
  with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=['--no-sandbox','--disable-gpu','--disable-dev-shm-usage'])
    page=b.new_page(viewport={'width':1280,'height':720})
    page.on('pageerror',lambda e: page_errors.append(str(e)))
    page.on('console',lambda m: console_errors.append(m.text) if m.type=='error' else None)
    # Standalone HTML contains all game data; external map tiles are irrelevant to the simulation.
    page.route('**/*',lambda route: route.continue_() if route.request.url.startswith(('data:','blob:','about:')) else route.abort())
    content=html.read_text(encoding='utf-8')
    page.set_content(content,wait_until='domcontentloaded',timeout=120000)
    page.wait_for_function('window.__AIR_EMPIRE_V221_DEBUG__ && window.__AIR_EMPIRE_V253__ && window.__AIR_EMPIRE_V700AE__',timeout=120000)
    init=page.evaluate("() => { window.__AIR_EMPIRE_V253__.setSeed(20260722,null); return window.__AIR_EMPIRE_V221_DEBUG__.startGameForTesting('klm',1955,'balanced'); }")
    for i in range(280):
      q0=time.time();page.evaluate('window.__AIR_EMPIRE_V221_DEBUG__.advanceOne()');snap=js_snapshot(page);snap['elapsedQuarterSeconds']=time.time()-q0;quarter_totals.append(snap)
      if (i+1)%20==0:
        cp=dict(snap);cp['completed']=i+1;cp['elapsedTotalSeconds']=time.time()-start;checkpoints.append(cp)
        print(json.dumps({'checkpoint':cp},ensure_ascii=False),flush=True)
    reality=annual_2024(page);final=js_snapshot(page)
    final['cargoValidator']=page.evaluate('window.__AIR_EMPIRE_V600B62__?.validate?.() ?? null')
    final['cargoNetworkValidator']=page.evaluate('window.__AIR_EMPIRE_V600B3__?.validate?.() ?? null')
    final['cargoMarketAudit']=page.evaluate('window.__AIR_EMPIRE_V700AE__?.audit?.() ?? null')
    final['marketStats']=page.evaluate('window.__AIR_EMPIRE_V221_DEBUG__.getGameState().cargoMarketClearStatsV700AE ?? null')
    final['historicalEntrantInitializationLedger']=page.evaluate('window.__AIR_EMPIRE_V221_DEBUG__.getGameState().historicalEntrantInitializationLedgerV700AC ?? []')
    final['closedAirlinesArchive']=page.evaluate('window.__AIR_EMPIRE_V221_DEBUG__.getGameState().closedAirlinesArchiveV700AC ?? []')
    b.close()
except Exception as e:
  error=f'{type(e).__name__}: {e}';traceback.print_exc()
  init=locals().get('init',None);reality=None;final=quarter_totals[-1] if quarter_totals else None

audit={
 'version':'alpha7.0-ae-cargo-market-clear','seed':seed,'completed':error is None and len(quarter_totals)==280,
 'period':{'start':'1955Q1','end':f"{final.get('year')}Q{final.get('quarter')}" if final else None,'quarters':len(quarter_totals)},
 'elapsedSeconds':time.time()-start,'init':init,'checkpoints':checkpoints,'quarterTotals':quarter_totals,'reality2024':reality,'final':final,
 'pageErrors':page_errors,'consoleErrors':console_errors,'error':error,
 'sha256':hashlib.sha256(html.read_bytes()).hexdigest()
}
(outdir/'ALPHA700AE_1955Q1_280Q_AUDIT.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
with (outdir/'ALPHA700AE_1955Q1_280Q_CHECKPOINTS.csv').open('w',newline='',encoding='utf-8') as f:
  if checkpoints:
    keys=[k for k,v in checkpoints[0].items() if not isinstance(v,(dict,list))];w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows([{k:x.get(k) for k in keys} for x in checkpoints])
(outdir/'ALPHA700AE_2024_REALITY.json').write_text(json.dumps(reality,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'completed':audit['completed'],'quarters':len(quarter_totals),'elapsed':audit['elapsedSeconds'],'reality2024':reality,'final':final,'pageErrors':page_errors,'error':error},ensure_ascii=False,indent=2))
if not audit['completed']: sys.exit(2)
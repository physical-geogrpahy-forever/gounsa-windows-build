from pathlib import Path
import sys, hashlib

src=Path(sys.argv[1] if len(sys.argv)>1 else 'air-empire-network-ai-v2.3.0-alpha7.0-ad-complete-entrant-lifecycle-standalone.html')
out=Path(sys.argv[2] if len(sys.argv)>2 else 'air-empire-network-ai-v2.3.0-alpha7.0-ae-cargo-market-clear-standalone.html')
text=src.read_text(encoding='utf-8')

old_capacity='''  function cargoCapacityPerFlightV600(aircraft, distanceKm2, passengerLoadFactor=0) {
    if (isFreighterAircraftV600(aircraft)) {
      return { weightKg: payloadAtDistanceV600(aircraft, distanceKm2), volumeM3: Math.max(1, aircraft.cargo_volume_m3 ?? (aircraft.payload_kg ?? aircraft.cargo_kg ?? 0) / 155), source: "main_deck_freighter" };
    }
    const seats = Math.max(0, aircraft.seats ?? 0);
    const nominalBelly = Math.max(0, aircraft.cargo_kg ?? 0);
    const structuralPayload = Math.max(nominalBelly, aircraft.max_payload_kg ?? seats * 105 + nominalBelly * 1.18);
    const rangeRatio = distanceKm2 / Math.max(1, aircraft.range_km ?? distanceKm2);
    const rangePayloadFactor = rangeRatio <= 0.55 ? 1 : Math.max(0.68, 1 - (rangeRatio - 0.55) / 0.35 * 0.32);
    const passengersPerFlight = seats * Math.max(0, Math.min(1, passengerLoadFactor));
    const weightAvailable = Math.max(0, structuralPayload * rangePayloadFactor - passengersPerFlight * 105);
    const lowLoadFlex = 1 + (1 - Math.max(0, Math.min(1, passengerLoadFactor))) * 0.30;
    const weightKg = Math.max(0, Math.min(weightAvailable, nominalBelly * lowLoadFlex));
    const volumeM3 = Math.max(0, aircraft.belly_volume_m3 ?? nominalBelly / 145 * 1.08);
    return { weightKg, volumeM3, source: "passenger_belly" };
  }'''
new_capacity='''  function cargoCapacityPerFlightV600(aircraft, distanceKm2, passengerLoadFactor=0) {
    if (isFreighterAircraftV600(aircraft)) {
      return { weightKg: payloadAtDistanceV600(aircraft, distanceKm2), volumeM3: Math.max(1, aircraft.cargo_volume_m3 ?? (aircraft.payload_kg ?? aircraft.cargo_kg ?? 0) / 155), source: "main_deck_freighter" };
    }
    const seats = Math.max(0, aircraft.seats ?? 0);
    const nominalBelly = Math.max(0, aircraft.cargo_kg ?? 0);
    const structuralPayload = Math.max(nominalBelly, aircraft.max_payload_kg ?? seats * 105 + nominalBelly * 1.18);
    const rangeRatio = distanceKm2 / Math.max(1, aircraft.range_km ?? distanceKm2);
    const rangePayloadFactor = rangeRatio <= 0.55 ? 1 : Math.max(0.68, 1 - (rangeRatio - 0.55) / 0.35 * 0.32);
    const lf = Math.max(0, Math.min(1, passengerLoadFactor));
    const passengersPerFlight = seats * lf;
    // Structural payload already includes passenger body weight.  Do not subtract
    // checked baggage from this residual a second time; baggage is accounted for
    // independently against the physical belly allowance below.
    const structuralWeightAvailable = Math.max(0, structuralPayload * rangePayloadFactor - passengersPerFlight * 105);
    const lowLoadFlex = 1 + (1 - lf) * 0.30;
    const widebody = aircraft.category === "widebody" || seats >= 220;
    const regional = !widebody && seats < 110;
    const checkedBagKgPerPax = widebody ? 18 : (regional ? 14 : 16);
    const checkedBagM3PerPax = widebody ? 0.085 : (regional ? 0.065 : 0.075);
    const operationalWeightReserveShare = widebody ? 0.05 : (regional ? 0.10 : 0.08);
    const blockedVolumeShare = widebody ? 0.08 : (regional ? 0.22 : 0.15);
    const physicalBellyWeight = Math.max(0, nominalBelly * lowLoadFlex - passengersPerFlight * checkedBagKgPerPax - nominalBelly * operationalWeightReserveShare);
    const nominalBellyVolumeM3 = Math.max(0, aircraft.belly_volume_m3 ?? nominalBelly / 145 * 1.08);
    const physicalBellyVolumeM3 = Math.max(0, nominalBellyVolumeM3 * (1 - blockedVolumeShare) - passengersPerFlight * checkedBagM3PerPax);
    const weightKg = Math.max(0, Math.min(structuralWeightAvailable, physicalBellyWeight));
    const volumeM3 = physicalBellyVolumeM3;
    return { weightKg, volumeM3, source: "passenger_belly", baggageReservedKgV700AE: passengersPerFlight * checkedBagKgPerPax, baggageReservedM3V700AE: passengersPerFlight * checkedBagM3PerPax };
  }'''
assert text.count(old_capacity)==1, f'capacity match {text.count(old_capacity)}'
text=text.replace(old_capacity,new_capacity,1)

old_stmt='''function adjustStatementV600B3(airline, st, {revenue=0,cost=0}={}) {
  if(!st||(!revenue&&!cost))return;
  const net=revenue-cost;
  st.revenue=(st.revenue??0)+revenue;st.operatingCost=(st.operatingCost??0)+cost;
  for(const k of ["cashOperatingProfit","accountingOperatingProfit","operatingProfitBeforeCapabilityInvestment","freeCashFlowBeforeDividends","preDividendProfit","profit"]) st[k]=(st[k]??0)+net;
  airline.cash=(airline.cash??0)+net;st.cashAfter=airline.cash;
}'''
new_stmt='''function syncConsolidatedCargoDeltaV700AE(st,{revenue=0,cost=0}={}) {
  if(!st)return;const net=(Number(revenue)||0)-(Number(cost)||0);
  if("consolidatedRevenueAlpha5" in st)st.consolidatedRevenueAlpha5=(Number(st.consolidatedRevenueAlpha5)||0)+(Number(revenue)||0);
  if("consolidatedOperatingCostAlpha5" in st)st.consolidatedOperatingCostAlpha5=(Number(st.consolidatedOperatingCostAlpha5)||0)+(Number(cost)||0);
  if("consolidatedOperatingProfitAlpha5" in st)st.consolidatedOperatingProfitAlpha5=(Number(st.consolidatedOperatingProfitAlpha5)||0)+net;
  if("consolidatedNetProfitAfterExtraordinaryAlpha5" in st)st.consolidatedNetProfitAfterExtraordinaryAlpha5=(Number(st.consolidatedNetProfitAfterExtraordinaryAlpha5)||0)+net;
  if("consolidatedOperatingMarginAlpha5" in st){const r=Number(st.consolidatedRevenueAlpha5)||0;st.consolidatedOperatingMarginAlpha5=r>0?(Number(st.consolidatedOperatingProfitAlpha5)||0)/r:0;}
}
function adjustStatementV600B3(airline, st, {revenue=0,cost=0}={}) {
  if(!st||(!revenue&&!cost))return;
  const net=revenue-cost;
  st.revenue=(st.revenue??0)+revenue;st.operatingCost=(st.operatingCost??0)+cost;
  for(const k of ["cashOperatingProfit","accountingOperatingProfit","operatingProfitBeforeCapabilityInvestment","freeCashFlowBeforeDividends","preDividendProfit","profit"]) st[k]=(st[k]??0)+net;
  syncConsolidatedCargoDeltaV700AE(st,{revenue,cost});
  airline.cash=(airline.cash??0)+net;st.cashAfter=airline.cash;
}'''
assert text.count(old_stmt)==1, f'statement match {text.count(old_stmt)}'
text=text.replace(old_stmt,new_stmt,1)

# Cargo historical margin post-adjustment must also keep Alpha5 fields in sync.
old_b62='''  st.revenue=(st.revenue||0)+revenueAdjustment; st.operatingCost=(st.operatingCost||0)+costAdjustment;
  for(const k of ["cashOperatingProfit","accountingOperatingProfit","operatingProfitBeforeCapabilityInvestment","freeCashFlowBeforeDividends","preDividendProfit","profit"]) st[k]=(st[k]||0)+appliedNet;
  airline.cash=(airline.cash||0)+appliedNet; st.cashAfter=airline.cash;'''
new_b62='''  st.revenue=(st.revenue||0)+revenueAdjustment; st.operatingCost=(st.operatingCost||0)+costAdjustment;
  for(const k of ["cashOperatingProfit","accountingOperatingProfit","operatingProfitBeforeCapabilityInvestment","freeCashFlowBeforeDividends","preDividendProfit","profit"]) st[k]=(st[k]||0)+appliedNet;
  syncConsolidatedCargoDeltaV700AE(st,{revenue:revenueAdjustment,cost:costAdjustment});
  airline.cash=(airline.cash||0)+appliedNet; st.cashAfter=airline.cash;'''
assert text.count(old_b62)==1, f'b62 match {text.count(old_b62)}'
text=text.replace(old_b62,new_b62,1)

marker='''const advanceTurnBeforeV600B3=advanceTurn;
advanceTurn=function(state,ctx){const result=advanceTurnBeforeV600B3(state,ctx);const __cargoT0V700G=performance.now();result.cargoNetworkV600B3=applyCargoNetworkEconomicsV600B3(state,ctx);const __cargoMsV700G=performance.now()-__cargoT0V700G;if(state.performanceCoreV700G?.last){state.performanceCoreV700G.last.cargoConnectionMs=__cargoMsV700G;state.performanceCoreV700G.totals.cargoConnectionMs=(state.performanceCoreV700G.totals.cargoConnectionMs||0)+__cargoMsV700G;}return result;};'''
assert text.count(marker)==1

injected=r'''

// ---------------------------------------------------------------------------
// AIR EMPIRE alpha7.0-ae — group-level cargo market clearing
// ---------------------------------------------------------------------------
const V700AE = Object.freeze({version:"2.3.0-alpha7.0-ae-cargo-market-clear", toleranceKg:1e-5});
function cargoGroupRootV700AE(airline,state){
  let cur=airline,seen=new Set();
  while(cur?.parentAirlineId&&!seen.has(cur.id)){seen.add(cur.id);const p=(state.airlines||[]).find(a=>a.id===cur.parentAirlineId);if(!p)break;cur=p;}
  return cur?.id||airline?.id||"unknown";
}
function waterFillGroupsV700AE(claims,marketKg){
  const out=new Map(),active=[...claims.entries()].map(([id,kg])=>({id,kg:Math.max(0,Number(kg)||0)}));
  let remain=Math.max(0,Number(marketKg)||0),pool=active;
  while(pool.length){const share=remain/pool.length;const small=pool.filter(x=>x.kg<=share+1e-12);if(!small.length){for(const x of pool)out.set(x.id,share);remain=0;break;}for(const x of small){out.set(x.id,x.kg);remain-=x.kg;}const done=new Set(small.map(x=>x.id));pool=pool.filter(x=>!done.has(x.id));if(remain<=1e-12){for(const x of pool)out.set(x.id,0);break;}}
  return out;
}
function recomputeCargoRouteLoadV700AE(airline,route,report,ctx){
  if(!route||!report)return;const ac=ctx.aircraftById?.[route.aircraftId],A=ctx.airportsByIata?.[route.a],B=ctx.airportsByIata?.[route.b];if(!ac||!A||!B)return;
  const dist=route.distanceKm??distanceBetweenAirports(A,B),util=Math.max(0,Math.min(1,Number(report.utilizationRatio)||1));
  const cap=cargoCapacityPerFlightV600(ac,dist,(route.routeType??"passenger")==="passenger"?(Number(report.loadFactor)||0):0);
  const flights=Math.max(0,Number(route.flightsPerWeekOneWay)||0)*WEEKS_PER_QUARTER*util*2;
  const wcap=Math.max(0,cap.weightKg*flights),vcap=Math.max(0,cap.volumeM3*flights);
  report.cargoWeightLoadFactorV600=wcap>0?Math.max(0,Math.min(1,(Number(report.cargoKgCarried)||0)/wcap)):0;
  report.cargoVolumeLoadFactorV600=vcap>0?Math.max(0,Math.min(1,(Number(report.cargoVolumeM3CarriedV600)||0)/vcap)):0;
  report.cargoLoadFactor=Math.max(report.cargoWeightLoadFactorV600,report.cargoVolumeLoadFactorV600);
}
function cargoMarketDemandQuarterV700AE(from,to,cls,state,ctx){
  const A=ctx.airportsByIata?.[from],B=ctx.airportsByIata?.[to];if(!A||!B)return 0;const dist=distanceBetweenAirports(A,B);
  return Math.max(0,Number(estimateWeeklyCargoDemandBreakdownV600(A,B,dist,state.year,state)?.byClass?.[cls])||0)*WEEKS_PER_QUARTER;
}
function directCargoContributionV700AE(airline,route,report,from,to,cls,state,ctx){
  const direction=from===route.a?report.cargoDirectionBreakdownV600?.outbound:report.cargoDirectionBreakdownV600?.inbound;if(!direction)return null;
  const raw=Math.max(0,Number(direction.byClass?.[cls])||0),util=Math.max(0,Math.min(1,Number(report.utilizationRatio)||1));const kg=raw*WEEKS_PER_QUARTER*util;if(kg<=0)return null;
  return {kind:"direct",airline,route,report,from,to,cls,group:cargoGroupRootV700AE(airline,state),kg,rawWeekly:raw,util};
}
function connectingCargoContributionsV700AE(rows,state){
  const out=[];for(const row of rows||[]){const airline=(state.airlines||[]).find(a=>a.id===row.operatorId);if(!airline)continue;for(const cls of Object.keys(CARGO_CLASSES_V600)){const raw=Math.max(0,Number(row.byClass?.[cls])||0),kg=raw*WEEKS_PER_QUARTER;if(kg>0)out.push({kind:"connecting",airline,row,from:row.from,to:row.to,cls,group:cargoGroupRootV700AE(airline,state),kg,rawWeekly:raw});}}return out;
}
function applyDirectFactorV700AE(c,factor,state,ctx){
  factor=Math.max(0,Math.min(1,factor));if(factor>=1-1e-12)return {removedKg:0,revenueDelta:0,costDelta:0};
  const {airline,route,report,from,cls,rawWeekly,util}=c,def=CARGO_CLASSES_V600[cls];const oldRaw=rawWeekly,newRaw=oldRaw*factor,deltaRaw=newRaw-oldRaw;
  const A=ctx.airportsByIata?.[from],to=from===route.a?route.b:route.a,B=ctx.airportsByIata?.[to],dist=route.distanceKm??distanceBetweenAirports(A,B);const q=WEEKS_PER_QUARTER*util;
  const revenueDelta=deltaRaw*cargoYieldPerKg(dist)*def.yieldMultiplier*(Number(route.cargoFareMultiplier)||1)*q;
  const handlingFactor=Math.sqrt(cargoAirportIndexesV600(A).warehouse*cargoAirportIndexesV600(B).warehouse);
  const costDelta=deltaRaw*def.handlingUsdKg*handlingFactor*costEraMultiplier(state.year)*q;
  const kgDelta=deltaRaw*q,volDelta=kgDelta/(def.densityKgM3||150);const d=from===route.a?report.cargoDirectionBreakdownV600.outbound:report.cargoDirectionBreakdownV600.inbound;
  d.byClass[cls]=newRaw;d.carriedKg=Math.max(0,(Number(d.carriedKg)||0)+deltaRaw);d.usedVolumeM3=Math.max(0,(Number(d.usedVolumeM3)||0)+deltaRaw/(def.densityKgM3||150));
  report.cargoKgCarried=Math.max(0,(Number(report.cargoKgCarried)||0)+kgDelta);report.cargoVolumeM3CarriedV600=Math.max(0,(Number(report.cargoVolumeM3CarriedV600)||0)+volDelta);
  if(from===route.a)report.cargoOutboundKgV600=Math.max(0,(Number(report.cargoOutboundKgV600)||0)+kgDelta);else report.cargoInboundKgV600=Math.max(0,(Number(report.cargoInboundKgV600)||0)+kgDelta);
  report.cargoClassBreakdownV600??={};report.cargoClassBreakdownV600[cls]=Math.max(0,(Number(report.cargoClassBreakdownV600[cls])||0)+kgDelta);
  report.cargoRevenue=Math.max(0,(Number(report.cargoRevenue)||0)+revenueDelta);report.cargoHandlingCost=Math.max(0,(Number(report.cargoHandlingCost)||0)+costDelta);
  report.revenue=(Number(report.revenue)||0)+revenueDelta;report.operatingCost=(Number(report.operatingCost)||0)+costDelta;report.profit=(Number(report.profit)||0)+revenueDelta-costDelta;
  const st=airline.history?.at?.(-1);adjustStatementV600B3(airline,st,{revenue:revenueDelta,cost:costDelta});
  return {removedKg:-kgDelta,revenueDelta,costDelta};
}
function connectingEconomicsV700AE(row,byClass,state,ctx){
  const operator=(state.airlines||[]).find(a=>a.id===row.operatorId),A=ctx.airportsByIata?.[row.from],H=ctx.airportsByIata?.[row.hub],B=ctx.airportsByIata?.[row.to];if(!operator||!A||!H||!B)return {kg:0,volumeM3:0,revenue:0,handlingCost:0,parentCost:0,intercompanyPayment:0};
  const direct=distanceBetweenAirports(A,B),profile=cargoAiProfileV600B(operator),era=costEraMultiplier(state.year),kg=Object.values(byClass).reduce((s,v)=>s+(Number(v)||0),0),volumeM3=cargoClassVolumeV600B3(byClass);let revenue=0,handlingCost=0;
  const hf=(cargoAirportIndexesV600(A).warehouse+cargoAirportIndexesV600(H).warehouse+cargoAirportIndexesV600(B).warehouse)/3;
  for(const [cls,v0] of Object.entries(byClass)){const v=Number(v0)||0,def=CARGO_CLASSES_V600[cls];revenue+=v*cargoYieldPerKg(direct)*def.yieldMultiplier*profile.fare*V600B3.transferRevenueFactor;handlingCost+=v*def.handlingUsdKg*hf*era*1.42;}
  let parentCost=0,intercompanyPayment=0;for(const legMeta of [row.leg1,row.leg2].filter(l=>l.ownerId!==operator.id)){const owner=(state.airlines||[]).find(a=>a.id===legMeta.ownerId),route=owner?.routes?.find(r=>r.id===legMeta.routeId);if(!route)continue;let legCost=0;for(const [cls,v0] of Object.entries(byClass))legCost+=(Number(v0)||0)*(CARGO_CLASSES_V600[cls]?.handlingUsdKg??0.2)*0.30*era;legCost+=kg*(Number(route.distanceKm)||0)*0.000015*era;parentCost+=legCost;intercompanyPayment+=legCost*(1+V600B3.parentBellyTransferMargin);}
  return {kg,volumeM3,revenue,handlingCost,parentCost,intercompanyPayment};
}
function applyConnectingRowFactorsV700AE(row,factors,state,ctx){
  const operator=(state.airlines||[]).find(a=>a.id===row.operatorId),st=operator?.history?.at?.(-1);if(!operator||!st)return {removedKg:0};
  const oldBy={...row.byClass},newBy={};for(const cls of Object.keys(CARGO_CLASSES_V600))newBy[cls]=(Number(oldBy[cls])||0)*Math.max(0,Math.min(1,Number(factors[cls]??1)));
  const oldE=connectingEconomicsV700AE(row,oldBy,state,ctx),newE=connectingEconomicsV700AE(row,newBy,state,ctx),q=WEEKS_PER_QUARTER;
  const dkg=(newE.kg-oldE.kg)*q,dvol=(newE.volumeM3-oldE.volumeM3)*q,drev=(newE.revenue-oldE.revenue)*q,dhandling=(newE.handlingCost-oldE.handlingCost)*q,dpayment=(newE.intercompanyPayment-oldE.intercompanyPayment)*q,dpcost=(newE.parentCost-oldE.parentCost)*q;
  const own=[row.leg1,row.leg2].filter(l=>l.ownerId===operator.id),ownDist=own.reduce((s,l)=>s+(Number(operator.routes?.find(r=>r.id===l.routeId)?.distanceKm)||1),0)||1;
  for(const lm of own){const route=operator.routes?.find(r=>r.id===lm.routeId),rp=(st.routes||[]).find(r=>r.routeId===lm.routeId),share=(Number(route?.distanceKm)||1)/ownDist;adjustRouteReportV600B3(rp,{kg:dkg,volumeM3:dvol,revenue:drev*share,cost:dhandling*share,externalCargoRevenue:drev*share});}
  const parents=[row.leg1,row.leg2].filter(l=>l.ownerId!==operator.id),n=parents.length||1;for(const lm of parents){const p=(state.airlines||[]).find(a=>a.id===lm.ownerId),pst=p?.history?.at?.(-1),pr=(pst?.routes||[]).find(r=>r.routeId===lm.routeId);if(!p||!pst)continue;adjustStatementV600B3(p,pst,{revenue:dpayment/n,cost:dpcost/n});adjustRouteReportV600B3(pr,{kg:dkg,volumeM3:dvol,revenue:dpayment/n,cost:dpcost/n,intercompanyRevenue:dpayment/n,parentBelly:true});}
  adjustStatementV600B3(operator,st,{revenue:drev,cost:dhandling+dpayment});
  row.byClass=newBy;row.kg=newE.kg;row.volumeM3=newE.volumeM3;row.revenue=newE.revenue;row.handlingCost=newE.handlingCost;row.parentCost=newE.parentCost;row.intercompanyPayment=newE.intercompanyPayment;
  row.kgQuarter=newE.kg*q;row.revenueQuarter=newE.revenue*q;row.handlingCostQuarter=newE.handlingCost*q;row.parentCostQuarter=newE.parentCost*q;row.intercompanyPaymentQuarter=newE.intercompanyPayment*q;
  return {removedKg:-dkg,revenueDelta:drev,costDelta:dhandling+dpayment,parentRevenueDelta:dpayment,parentCostDelta:dpcost};
}
function refreshConnectingSummariesV700AE(state,currentRows){
  const byOp=new Map();for(const r of currentRows){let x=byOp.get(r.operatorId);if(!x){x=[];byOp.set(r.operatorId,x);}x.push(r);}for(const [id,rows] of byOp){const a=(state.airlines||[]).find(x=>x.id===id),st=a?.history?.at?.(-1);if(!st)continue;st.cargoNetworkV600B3={itineraries:rows.filter(r=>(r.kgQuarter||0)>0).length,connectingKg:rows.reduce((s,r)=>s+(Number(r.kgQuarter)||0),0),parentBellyKg:rows.filter(r=>r.leg1.source==="belly"||r.leg2.source==="belly").reduce((s,r)=>s+(Number(r.kgQuarter)||0),0),externalRevenue:rows.reduce((s,r)=>s+(Number(r.revenueQuarter)||0),0),variableCost:rows.reduce((s,r)=>s+(Number(r.handlingCostQuarter)||0)+(Number(r.parentCostQuarter)||0),0),intercompanyPayments:rows.reduce((s,r)=>s+(Number(r.intercompanyPaymentQuarter)||0),0),maxTransfers:1};}
}
function clearCargoMarketV700AE(state,ctx,networkResult){
  const n=Math.max(0,Number(networkResult?.itineraries)||0),ledger=state.cargoNetworkLedgerV600B3??[],currentRows=n?ledger.slice(Math.max(0,ledger.length-n)):[];const contributions=[];
  for(const airline of state.airlines||[]){if(airline.status==="merged")continue;const st=airline.history?.at?.(-1);if(!st)continue;const reports=new Map((st.routes||[]).map(r=>[r.routeId,r]));for(const route of airline.routes||[]){const report=reports.get(route.id);if(!report?.cargoDirectionBreakdownV600)continue;for(const [from,to] of [[route.a,route.b],[route.b,route.a]])for(const cls of Object.keys(CARGO_CLASSES_V600)){const c=directCargoContributionV700AE(airline,route,report,from,to,cls,state,ctx);if(c)contributions.push(c);}}}
  contributions.push(...connectingCargoContributionsV700AE(currentRows,state));const pools=new Map();for(const c of contributions){const key=`${c.from}>${c.to}|${c.cls}`;let a=pools.get(key);if(!a){a=[];pools.set(key,a);}a.push(c);}
  let adjustedPools=0,removedKg=0,violations=0,marketKgTotal=0,desiredKgTotal=0,carriedKgTotal=0;const cf=new Map();
  for(const [key,items] of pools){const [od,cls]=key.split("|"),[from,to]=od.split(">");const market=cargoMarketDemandQuarterV700AE(from,to,cls,state,ctx);marketKgTotal+=market;const claims=new Map();for(const c of items)claims.set(c.group,(claims.get(c.group)||0)+c.kg);const desired=[...claims.values()].reduce((s,v)=>s+v,0);desiredKgTotal+=desired;let alloc=claims;if(desired>market+V700AE.toleranceKg){alloc=waterFillGroupsV700AE(claims,market);adjustedPools++;}
    let poolCarried=0;for(const c of items){const claim=claims.get(c.group)||0,groupAlloc=alloc.get(c.group)??claim,factor=claim>0?Math.min(1,groupAlloc/claim):1;poolCarried+=c.kg*factor;if(c.kind==="direct"){removedKg+=applyDirectFactorV700AE(c,factor,state,ctx).removedKg;}else{let row=cf.get(c.row);if(!row){row={};cf.set(c.row,row);}row[c.cls]=factor;}}
    carriedKgTotal+=poolCarried;if(poolCarried>market+Math.max(V700AE.toleranceKg,market*1e-9))violations++;
  }
  let connRemoved=0;for(const [row,factors] of cf)connRemoved+=applyConnectingRowFactorsV700AE(row,factors,state,ctx).removedKg;removedKg+=connRemoved;refreshConnectingSummariesV700AE(state,currentRows);
  for(const airline of state.airlines||[]){const st=airline.history?.at?.(-1);if(!st)continue;for(const report of st.routes||[]){const route=airline.routes?.find(r=>r.id===report.routeId);if(route)recomputeCargoRouteLoadV700AE(airline,route,report,ctx);}}
  const stats=state.cargoNetworkStatsV600B3;if(stats&&currentRows.length){const currentKg=currentRows.reduce((s,r)=>s+(Number(r.kgQuarter)||0),0),currentRev=currentRows.reduce((s,r)=>s+(Number(r.revenueQuarter)||0),0),currentPay=currentRows.reduce((s,r)=>s+(Number(r.intercompanyPaymentQuarter)||0),0);const oldKg=currentRows.reduce((s,r)=>s+(Number(r._preClearKgQuarterV700AE)||Number(r.kgQuarter)||0),0);if(!Number.isFinite(stats._lastClearAdjustedV700AE)){/* cumulative correction handled once below */}stats._lastClearAdjustedV700AE=(stats._lastClearAdjustedV700AE||0)+1;}
  const result={version:V700AE.version,year:currentRows[0]?.year??(state.airlines?.find(a=>a.history?.length)?.history?.at?.(-1)?.year??state.year),quarter:currentRows[0]?.quarter??(state.airlines?.find(a=>a.history?.length)?.history?.at?.(-1)?.quarter??state.quarter),pools:pools.size,adjustedPools,removedKg,marketKgTotal,desiredKgTotal,carriedKgTotal,violations};
  state.lastCargoMarketClearV700AE=result;const s=state.cargoMarketClearStatsV700AE??(state.cargoMarketClearStatsV700AE={quarters:0,adjustedPools:0,removedKg:0,violations:0});s.quarters++;s.adjustedPools+=adjustedPools;s.removedKg+=removedKg;s.violations+=violations;return result;
}
function auditCargoMarketV700AE(state=gameState,ctx=context()){
  const clear=state.lastCargoMarketClearV700AE||{};let cargoRevenueGtTotal=0,accountingNonFinite=0;const rows=[];for(const a of state.airlines||[]){const st=a.history?.at?.(-1);if(!st)continue;const cargoRev=(st.routes||[]).reduce((s,r)=>s+(Number(r.cargoRevenue)||0),0);if(cargoRev>(Number(st.revenue)||0)+1) {cargoRevenueGtTotal++;rows.push({airlineId:a.id,type:"cargo_revenue_gt_total",cargoRevenue:cargoRev,revenue:st.revenue});}for(const k of ["consolidatedRevenueAlpha5","consolidatedOperatingCostAlpha5","consolidatedOperatingProfitAlpha5","consolidatedNetProfitAfterExtraordinaryAlpha5"]){if(k in st&&!Number.isFinite(Number(st[k]))){accountingNonFinite++;rows.push({airlineId:a.id,type:"nonfinite",field:k,value:st[k]});}}}
  return {valid:(clear.violations||0)===0&&cargoRevenueGtTotal===0&&accountingNonFinite===0,marketViolations:clear.violations||0,cargoRevenueGtTotal,accountingNonFinite,rows};
}
window.__AIR_EMPIRE_V700AE__={version:V700AE.version,config:V700AE,groupRoot:cargoGroupRootV700AE,waterFill:waterFillGroupsV700AE,clear:(state=gameState,ctx=context(),networkResult=null)=>clearCargoMarketV700AE(state,ctx,networkResult),audit:(state=gameState,ctx=context())=>auditCargoMarketV700AE(state,ctx)};
const advanceTurnBeforeV700AE=advanceTurn;
advanceTurn=function(state,ctx){const result=advanceTurnBeforeV700AE(state,ctx);result.cargoMarketClearV700AE=clearCargoMarketV700AE(state,ctx,result.cargoNetworkV600B3);return result;};
window.__AIR_EMPIRE_V700AE_BUILD__={version:V700AE.version,source:"2.3.0-alpha7.0-ad",changes:["group-level OD/class/direction cargo demand conservation","parent and cargo subsidiary share one cargo market group","belly checked-baggage and blocked-volume constraints without double-subtracting passenger payload","Alpha5 consolidated accounting synchronized after cargo post-adjustments"]};
'''
text=text.replace(marker,marker+injected,1)

out.write_text(text,encoding='utf-8')
print(out)
print('size',out.stat().st_size)
print('sha256',hashlib.sha256(out.read_bytes()).hexdigest())
const {test}=require('node:test');
const assert=require('node:assert/strict');
const report=require('../frontend/profile_report.js');
const data={scope:'SOURCE_PROFILES_NOT_CANONICAL_STATIONS',profiles:[
 {id:'synthetic-110',name:'Synthetic',voltage:110,count:2,statuses:{agreement:2},reviewCount:0,links:[{id:'h1',direct:true}]},
 {id:'synthetic-220',name:'Synthetic',voltage:220,count:0,statuses:{},reviewCount:0,links:[]}],
 headings:{h1:{title:'Synthetic heading',status:null,positions:[1]}},
 provenance:{pipeline_source_date:'2026-07-31',input_sha256:{fixture:'synthetic'}}};
test('report preserves snapshot, uncertainty and note without changing evidence',()=>{
 const original=JSON.stringify(data);const r=report.build(data,'synthetic-110','<script>note</script>','2026-10-07T10:00:00Z');
 assert.equal(r.user_note.classification,'USER_INPUT_NOT_SOURCE_EVIDENCE');
 assert.equal(r.profile.identity_status,'UNVERIFIED_SOURCE_PROFILE');
 assert.equal(r.pipeline.pending_applications_coverage,'UNKNOWN');
 assert.equal(r.provenance.input_sha256.fixture,'synthetic');
 assert.match(report.markdown(r),/Synthetic heading/);
 assert.match(report.markdown(r),/score/);
 r.pipeline.status_counts.agreement=99;assert.equal(JSON.stringify(data),original);
});
test('notes separated by stable profile ID including voltage',()=>{
 const values=new Map();const storage={getItem:k=>values.get(k)??null,setItem:(k,v)=>values.set(k,v)};
 report.saveNote(storage,'synthetic-110','110 note');report.saveNote(storage,'synthetic-220','220 note');
 assert.equal(report.readNote(storage,'synthetic-110').text,'110 note');
 assert.equal(report.readNote(storage,'synthetic-220').text,'220 note');
});
test('unavailable or corrupted storage never claims saved',()=>{
 assert.equal(report.readNote({getItem:()=>'{invalid'},'a').state,'unavailable');
 assert.equal(report.readNote({getItem:()=>{throw Error('blocked')}},'a').state,'unavailable');
 assert.throws(()=>report.saveNote({setItem:()=>{throw Error('quota')}},'a','note'));
});
test('unknown profile and oversized note rejected; absent projects remain unknown coverage',()=>{
 assert.throws(()=>report.build(data,'missing','','2026-10-07'));
 assert.throws(()=>report.build(data,'synthetic-110','x'.repeat(20001),'2026-10-07'));
 const r=report.build(data,'synthetic-220','','2026-10-07');
 assert.equal(r.pipeline.operational_coverage,'UNKNOWN');assert.match(report.markdown(r),/Brak dopasowań/);
});

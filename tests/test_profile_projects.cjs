const {test}=require('node:test');
const assert=require('node:assert/strict');
const projects=require('../frontend/profile_projects.js');
const report=require('../frontend/profile_report.js');
const rows=[
 {record_id:'synthetic-1',project_name:'Synthetic BESS',applicant:'Spółka Testowa <img src=x onerror=alert(1)>',technology_reported:'MEE',status_reported:'WARUNKI PRZYŁĄCZENIA wydane',export_MW:'0',import_MW:null,raw_import:'10 E-',raw_export:0,row:5,review_reasons:['IMPORT_POWER_ANNOTATION_OR_INVALID']},
 {record_id:'synthetic-2',project_name:'Synthetic PV',applicant:'Other',technology_reported:'PV',status_reported:'UMOWA O PRZYŁĄCZENIE obowiązująca',export_MW:'20',import_MW:'2',row:6,review_reasons:[]}
];
test('status filters keep conditions separate from agreements and applicant search works',()=>{
 assert.equal(projects.filter(rows,'conditions').length,1);
 assert.equal(projects.filter(rows,'agreements')[0].record_id,'synthetic-2');
 assert.equal(projects.filter(rows,'all',' SPÓŁKA ').length,1);
 assert.equal(projects.filter(rows,'agreements','BESS').length,0);
 assert.equal(projects.category('WNIOSEK niekompletny'),'applications');
});
test('source text cannot become executable HTML; zero remains distinct from unknown',()=>{
 const html=projects.cards(rows,{pipeline_source_date:'2026-07-31'});
 assert.ok(!html.includes('<img'));assert.ok(html.includes('&lt;img'));
 assert.match(html,/0 MW/);assert.match(html,/Nieustalona.*10 E-/);
 assert.match(html,/KRS \/ NIP/);assert.match(html,/Nie zweryfikowano/);
});
test('report preserves investor evidence and annotations independently of filters',()=>{
 const data={profiles:[{id:'synthetic',name:'Fixture',voltage:220,count:2,statuses:{},reviewCount:1,links:[],projects:rows}],headings:{},provenance:{pipeline_source_date:'2026-07-31'},pipeline_footnotes:[{marker:'E-',meaning:'Synthetic footnote'}]};
 const r=report.build(data,'synthetic','','2026-10-07');
 assert.equal(r.projects.length,2);assert.equal(r.projects[0].import_MW,null);
 assert.equal(r.coverage.find(c=>c.section==='Tożsamość inwestorów').status,'UNKNOWN');
 assert.match(report.markdown(r),/Synthetic footnote/);
 r.projects[0].applicant='changed';assert.notEqual(rows[0].applicant,'changed');
});

import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Activity, BookOpenCheck, Brain, Database, FileSearch, Gauge, Layers3, Library, LockKeyhole, MessageSquareQuote, Search, ShieldCheck, Sparkles } from 'lucide-react';
import { Area, AreaChart, Bar, BarChart, CartesianGrid, Cell, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import './styles.css';

const pages = ['Overview', 'Ask Knowledge', 'Ingestion', 'Citation Review', 'Grounding Monitor', 'Query Traces', 'Admin'];
const latency = [{day:'Mon',ms:182},{day:'Tue',ms:169},{day:'Wed',ms:154},{day:'Thu',ms:148},{day:'Fri',ms:141}];
const collections = [{name:'Policies',value:34,color:'#38bdf8'},{name:'Runbooks',value:26,color:'#a78bfa'},{name:'Contracts',value:21,color:'#22c55e'},{name:'FAQs',value:19,color:'#f59e0b'}];
const traces = [
  ['QRY-89012','policy refund approval','4 chunks','0.86 grounded','142ms'],
  ['QRY-89021','incident escalation runbook','5 chunks','0.91 grounded','155ms'],
  ['QRY-89035','contract renewal terms','3 chunks','0.78 grounded','188ms'],
  ['QRY-89044','security exception process','6 chunks','0.94 grounded','133ms']
];
const sources = [
  ['DOC-112','Refund Policy Handbook','policies/refunds.md','0.91'],
  ['DOC-284','Enterprise Escalation Runbook','runbooks/escalation.md','0.88'],
  ['DOC-337','Renewal Contract Playbook','contracts/renewals.md','0.81']
];

function answerFallback(question){
  const grounded = question.toLowerCase().includes('policy') || question.toLowerCase().includes('runbook') || question.toLowerCase().includes('contract');
  return {
    query_id: `QRY-${Date.now().toString().slice(-5)}`,
    answer: grounded ? 'Based on the retrieved enterprise knowledge, the recommended action is to follow the approved policy workflow, attach the relevant evidence, and escalate only when account tier or risk criteria require supervisor approval.' : 'The knowledge base found partial context. The safest answer is to request a source refresh or add more documents before making a final business decision.',
    groundedness: grounded ? 0.91 : 0.62,
    latency_ms: grounded ? 146 : 219,
    retriever_version: 'hybrid-demo-v1',
    citations: sources
  };
}

function App(){
  const [active,setActive] = useState('Overview');
  const [question,setQuestion] = useState('What is the approved policy for refund escalation?');
  const [answer,setAnswer] = useState(answerFallback(question));
  const metrics = useMemo(()=>[
    ['Indexed Documents','48.2K','+11%',Library],['Grounded Answers','94.1%','+5.7%',ShieldCheck],['Avg Latency','146ms','-18%',Gauge],['Query Traces','128K','+24%',Activity]
  ],[]);
  const ask = async()=>{
    try{
      const response = await fetch('/answer',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question})});
      if(!response.ok) throw new Error('offline');
      setAnswer(await response.json());
    }catch{setAnswer(answerFallback(question));}
  };
  return <main className="app-shell"><aside className="sidebar"><div className="brand"><BookOpenCheck/><div><strong>KnowledgeCore AI</strong><span>Enterprise RAG Platform</span></div></div>{pages.map(p=><button className={active===p?'active':''} onClick={()=>setActive(p)} key={p}>{p}</button>)}</aside><section className="workspace"><header className="topbar"><div><p className="eyebrow">Grounded enterprise knowledge</p><h1>{active}</h1></div><button onClick={ask}>Ask knowledge</button></header>{active==='Overview'&&<Overview metrics={metrics}/>} {active==='Ask Knowledge'&&<AskKnowledge question={question} setQuestion={setQuestion} answer={answer} ask={ask}/>} {active==='Ingestion'&&<Ingestion/>} {active==='Citation Review'&&<CitationReview answer={answer}/>} {active==='Grounding Monitor'&&<GroundingMonitor/>} {active==='Query Traces'&&<QueryTraces/>} {active==='Admin'&&<Admin/>}</section></main>
}
function Overview({metrics}){return <><section className="metrics">{metrics.map(([l,v,d,Icon])=><article className="card" key={l}><Icon/><span>{l}</span><strong>{v}</strong><small>{d}</small></article>)}</section><section className="grid"><Panel title="Retrieval latency" icon={<Activity/>}><ResponsiveContainer width="100%" height={260}><AreaChart data={latency}><CartesianGrid strokeDasharray="3 3" stroke="#25364b"/><XAxis dataKey="day" stroke="#9cafc4"/><YAxis stroke="#9cafc4"/><Tooltip/><Area dataKey="ms" stroke="#38bdf8" fill="#0e7490"/></AreaChart></ResponsiveContainer></Panel><Panel title="Knowledge collections" icon={<Database/>}><ResponsiveContainer width="100%" height={260}><PieChart><Pie data={collections} dataKey="value" nameKey="name" outerRadius={92}>{collections.map(c=><Cell key={c.name} fill={c.color}/>)}</Pie><Tooltip/></PieChart></ResponsiveContainer></Panel></section></>}
function AskKnowledge({question,setQuestion,answer,ask}){return <section className="grid"><Panel title="Ask enterprise knowledge" icon={<Search/>}><textarea value={question} onChange={e=>setQuestion(e.target.value)}/><button onClick={ask}>Generate grounded answer</button></Panel><Panel title="Answer workspace" icon={<Sparkles/>}><div className="answer"><strong>{answer.query_id}</strong><p>{answer.answer}</p><span>Groundedness {Math.round(answer.groundedness*100)}% · {answer.latency_ms}ms · {answer.retriever_version}</span></div></Panel></section>}
function Ingestion(){return <section className="grid"><Panel title="Ingestion pipeline" icon={<Layers3/>}><div className="pipeline"><div>Upload</div><div>Chunk</div><div>Index</div><div>Trace</div><div>Ready</div></div></Panel><Panel title="Source health" icon={<Database/>}><div className="reason">Policies collection refreshed 14 minutes ago.</div><div className="reason">Runbooks collection has 2 stale documents.</div><div className="reason">Contracts collection requires permission sync.</div></Panel></section>}
function CitationReview({answer}){return <Panel title="Citation-backed evidence" icon={<FileSearch/>}><div className="table">{(answer.citations||sources).map(row=><div className="row" key={row[0]}>{row.map(cell=><span key={cell}>{cell}</span>)}</div>)}</div></Panel>}
function GroundingMonitor(){return <section className="grid"><Panel title="Grounding quality" icon={<ShieldCheck/>}><ResponsiveContainer width="100%" height={260}><BarChart data={[{k:'Faithful',v:94},{k:'Cited',v:91},{k:'Complete',v:86},{k:'Low Risk',v:96}]}><XAxis dataKey="k" stroke="#9cafc4"/><YAxis stroke="#9cafc4"/><Tooltip/><Bar dataKey="v" fill="#38bdf8"/></BarChart></ResponsiveContainer></Panel><Panel title="Guardrail signals" icon={<LockKeyhole/>}><div className="reason">Low-grounding responses require review.</div><div className="reason">Citations are mandatory for policy answers.</div><div className="reason">Tenant permissions filter restricted documents.</div></Panel></section>}
function QueryTraces(){return <Panel title="Traceable query history" icon={<MessageSquareQuote/>}><div className="table traces">{traces.map(row=><div className="row" key={row[0]}>{row.map(cell=><span key={cell}>{cell}</span>)}</div>)}</div></Panel>}
function Admin(){return <section className="grid"><Panel title="Platform controls" icon={<Brain/>}><div className="reason">Retriever version: hybrid-demo-v1</div><div className="reason">Chunk size: 900 tokens</div><div className="reason">Grounding threshold: 0.75</div><div className="reason">Trace stream: enabled</div></Panel><Panel title="Access model" icon={<LockKeyhole/>}><div className="reason">Tenant-aware document permissions.</div><div className="reason">Admin ingestion role required for source refresh.</div><div className="reason">Audit traces retained for compliance review.</div></Panel></section>}
function Panel({title,icon,children}){return <article className="panel"><div className="panel-title">{icon}<h2>{title}</h2></div>{children}</article>}

createRoot(document.getElementById('root')).render(<App/>);

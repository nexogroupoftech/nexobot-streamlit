<!DOCTYPE html>
<html class="dark" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>DarkFury · NexoCorp AI</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
  tailwind.config = {
    darkMode: "class",
    theme: {
      extend: {
        colors: {
          "primary": "#a4e6ff","primary-container": "#00d1ff","primary-fixed": "#b7eaff","primary-fixed-dim": "#4cd6ff","on-primary": "#003543","on-primary-container": "#00566a","on-primary-fixed": "#001f28","on-primary-fixed-variant": "#004e60",
          "secondary": "#c8c6c5","secondary-container": "#474746","secondary-fixed": "#e5e2e1","secondary-fixed-dim": "#c8c6c5","on-secondary": "#313030","on-secondary-container": "#b7b5b4","on-secondary-fixed": "#1c1b1b","on-secondary-fixed-variant": "#474746",
          "tertiary": "#ffd59c","tertiary-container": "#feb127","on-tertiary": "#442b00","on-tertiary-container": "#6b4700",
          "surface": "#131313","surface-dim": "#131313","surface-bright": "#3a3939","surface-container-lowest": "#0e0e0e","surface-container-low": "#1c1b1b","surface-container": "#201f1f","surface-container-high": "#2a2a2a","surface-container-highest": "#353534","surface-variant": "#353534","surface-tint": "#4cd6ff",
          "on-surface": "#e5e2e1","on-surface-variant": "#bbc9cf","background": "#131313","on-background": "#e5e2e1","outline": "#859399","outline-variant": "#3c494e","inverse-surface": "#e5e2e1","inverse-on-surface": "#313030","inverse-primary": "#00677f",
          "error": "#ffb4ab","error-container": "#93000a","on-error": "#690005","on-error-container": "#ffdad6"
        },
        fontFamily: { "headline": ["Space Grotesk"], "body": ["Inter"], "label": ["Inter"] },
        borderRadius: { "DEFAULT": "0.125rem","lg": "0.25rem","xl": "0.5rem","2xl": "0.75rem","full": "9999px" }
      }
    }
  }
</script>
<style>
  .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
  .fill-icon { font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
  body { background-color: #131313; color: #e5e2e1; font-family: 'Inter', sans-serif; }
  .glass-sidebar { backdrop-filter: blur(20px); background-color: rgba(32,31,31,0.92); }
  .custom-scrollbar::-webkit-scrollbar { width: 4px; }
  .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
  .custom-scrollbar::-webkit-scrollbar-thumb { background: #2a2a2a; border-radius: 10px; }
  .thought-stream-pulse { animation: tsPulse 2s ease-in-out infinite; }
  @keyframes tsPulse { 0%,100%{box-shadow:0 0 8px rgba(255,213,156,0.3);opacity:1}50%{box-shadow:0 0 20px rgba(255,213,156,0.7);opacity:0.6} }
  .msg-enter { animation: msgIn 0.3s ease; }
  @keyframes msgIn { from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)} }
  .typing-dot { animation: typingBounce 1.2s infinite; }
  .typing-dot:nth-child(2) { animation-delay: 0.2s; }
  .typing-dot:nth-child(3) { animation-delay: 0.4s; }
  @keyframes typingBounce { 0%,60%,100%{transform:translateY(0)}30%{transform:translateY(-5px)} }
  pre { background:#0e0e0e;border-left:3px solid #a4e6ff;padding:1rem;overflow-x:auto;border-radius:0.25rem;margin:0.75rem 0;font-family:'Space Grotesk',monospace;font-size:0.8rem; }
  code { font-family:'Space Grotesk',monospace;font-size:0.82em;background:rgba(164,230,255,0.08);padding:1px 5px;border-radius:2px; }
  pre code { background:none;padding:0; }
  .prose strong { color:#e5e2e1;font-weight:600; }
  ul.ai-list { list-style:disc;padding-left:1.25rem;margin:0.5rem 0; }
  ul.ai-list li { margin:0.25rem 0; }
  .input-glow:focus-within .glow-layer { opacity:1; }
</style>
</head>
<body class="flex h-screen overflow-hidden selection:bg-primary/20">

<!-- SIDEBAR -->
<aside id="sidebar" class="fixed left-0 top-0 h-full w-64 glass-sidebar border-r border-white/5 z-40 flex flex-col p-4 gap-1 transition-transform duration-300">
  <div class="mb-4 px-3 pt-3">
    <h2 class="text-xl font-black text-white font-headline tracking-tighter">Dark<span class="text-primary">Fury</span></h2>
    <p class="text-[10px] uppercase tracking-widest text-primary/60 font-label mt-0.5">NexoCorp · AI V2.0</p>
  </div>
  <nav class="flex flex-col gap-0.5">
    <button onclick="newChat()" class="text-gray-400 hover:bg-surface-container-high/60 px-4 py-2.5 rounded-xl flex items-center gap-3 hover:translate-x-0.5 transition-all duration-200 w-full text-left text-sm font-medium">
      <span class="material-symbols-outlined text-[18px]">add_comment</span>New Chat
    </button>
    <button onclick="showView('history')" id="nav-history" class="text-gray-400 hover:bg-surface-container-high/60 px-4 py-2.5 rounded-xl flex items-center gap-3 hover:translate-x-0.5 transition-all duration-200 w-full text-left text-sm font-medium">
      <span class="material-symbols-outlined text-[18px]">history</span>History
    </button>
    <button onclick="showView('image')" id="nav-image" class="text-gray-400 hover:bg-surface-container-high/60 px-4 py-2.5 rounded-xl flex items-center gap-3 hover:translate-x-0.5 transition-all duration-200 w-full text-left text-sm font-medium">
      <span class="material-symbols-outlined text-[18px]">image</span>Image Gen
    </button>
    <button onclick="showView('settings')" id="nav-settings" class="text-gray-400 hover:bg-surface-container-high/60 px-4 py-2.5 rounded-xl flex items-center gap-3 hover:translate-x-0.5 transition-all duration-200 w-full text-left text-sm font-medium">
      <span class="material-symbols-outlined text-[18px]">tune</span>Settings
    </button>
  </nav>
  <div class="mt-3 px-1">
    <span class="text-[10px] uppercase tracking-[0.2em] text-gray-600 font-label px-3 block mb-1.5">Persona</span>
    <div id="persona-list"></div>
  </div>
  <div class="mt-3 px-1 flex-1 overflow-hidden flex flex-col min-h-0">
    <span class="text-[10px] uppercase tracking-[0.2em] text-gray-600 font-label px-3 block mb-1.5">Recent</span>
    <div id="history-list" class="flex flex-col gap-0.5 overflow-y-auto custom-scrollbar flex-1"></div>
  </div>
  <div class="mt-auto pt-3 border-t border-white/5 flex flex-col gap-2">
    <div class="bg-surface-container-high px-4 py-3 rounded-xl">
      <div class="flex justify-between items-center mb-1.5">
        <span class="text-[10px] uppercase tracking-widest text-gray-500">Model</span>
        <span class="text-[10px] text-primary font-bold">KIMI-K2</span>
      </div>
      <div class="h-0.5 w-full bg-surface rounded-full overflow-hidden">
        <div class="h-full bg-gradient-to-r from-primary to-primary-container w-full"></div>
      </div>
    </div>
    <button class="w-full bg-gradient-to-br from-primary to-primary-container text-on-primary px-4 py-2.5 rounded-xl font-bold text-sm font-headline tracking-tight transition-transform active:scale-95 hover:opacity-90">
      Upgrade to Pro
    </button>
  </div>
</aside>

<!-- MAIN -->
<main id="main-area" class="flex-1 ml-64 flex flex-col h-screen bg-surface relative overflow-hidden">
  <!-- HEADER -->
  <header id="main-header" class="fixed top-0 right-0 left-64 z-30 bg-surface/95 backdrop-blur-sm px-8 py-3.5 flex justify-between items-center border-b border-surface-container transition-all duration-300">
    <div class="flex items-center gap-3">
      <button onclick="toggleSidebar()" class="text-gray-500 hover:text-primary transition-colors p-1">
        <span class="material-symbols-outlined text-[20px]">menu</span>
      </button>
      <div>
        <h1 id="header-title" class="text-sm font-bold font-headline tracking-tight text-primary">DarkFury</h1>
        <p id="header-sub" class="text-[10px] uppercase tracking-widest text-gray-600 font-label">Chat Workspace</p>
      </div>
    </div>
    <div class="flex items-center gap-2">
      <div id="persona-chips" class="hidden md:flex gap-1.5"></div>
      <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-surface-container-high to-surface-container-highest border border-white/10 flex items-center justify-center ml-2">
        <span class="material-symbols-outlined text-primary" style="font-size:16px">person</span>
      </div>
    </div>
  </header>

  <!-- CHAT VIEW -->
  <div id="view-chat" class="flex-1 flex flex-col pt-14 h-full overflow-hidden">
    <section id="messages" class="flex-1 overflow-y-auto custom-scrollbar px-6 md:px-10 py-8">
      <div class="max-w-3xl mx-auto flex flex-col gap-10">
        <div id="welcome-state" class="py-16 flex flex-col items-center text-center space-y-5">
          <div class="w-16 h-16 bg-surface-container-high rounded-2xl flex items-center justify-center mb-3 border border-white/5">
            <span class="material-symbols-outlined text-primary fill-icon" style="font-size:32px">auto_awesome</span>
          </div>
          <h2 class="text-4xl font-headline font-black tracking-tighter text-white">How can we architect<br/><span class="text-primary">your next breakthrough?</span></h2>
          <p class="text-gray-500 max-w-md font-body text-sm leading-relaxed">DarkFury is powered by Kimi-K2 via NVIDIA NIM — sharp, precise, doesn't sugarcoat.</p>
          <div class="grid grid-cols-2 md:grid-cols-3 gap-3 w-full max-w-2xl mt-2">
            <button onclick="quickSend('Write me a Python web scraper with BeautifulSoup')" class="bg-surface-container-low hover:bg-surface-container border border-white/5 hover:border-primary/30 p-4 rounded-xl text-left text-xs text-gray-400 hover:text-white transition-all duration-200">
              <span class="material-symbols-outlined text-primary text-sm mb-2 block">code</span>Write Python scraper
            </button>
            <button onclick="quickSend('Explain quantum computing in simple terms')" class="bg-surface-container-low hover:bg-surface-container border border-white/5 hover:border-primary/30 p-4 rounded-xl text-left text-xs text-gray-400 hover:text-white transition-all duration-200">
              <span class="material-symbols-outlined text-primary text-sm mb-2 block">science</span>Explain quantum computing
            </button>
            <button onclick="quickSend('Brainstorm 5 disruptive AI startup ideas')" class="bg-surface-container-low hover:bg-surface-container border border-white/5 hover:border-primary/30 p-4 rounded-xl text-left text-xs text-gray-400 hover:text-white transition-all duration-200">
              <span class="material-symbols-outlined text-primary text-sm mb-2 block">lightbulb</span>Startup ideas
            </button>
            <button onclick="quickSend('What are the latest trends in machine learning in 2025?')" class="bg-surface-container-low hover:bg-surface-container border border-white/5 hover:border-primary/30 p-4 rounded-xl text-left text-xs text-gray-400 hover:text-white transition-all duration-200">
              <span class="material-symbols-outlined text-primary text-sm mb-2 block">trending_up</span>ML trends 2025
            </button>
            <button onclick="quickSend('Debug: TypeError cannot read properties of undefined')" class="bg-surface-container-low hover:bg-surface-container border border-white/5 hover:border-primary/30 p-4 rounded-xl text-left text-xs text-gray-400 hover:text-white transition-all duration-200">
              <span class="material-symbols-outlined text-primary text-sm mb-2 block">bug_report</span>Debug a TypeError
            </button>
            <button onclick="quickSend('Roast my productivity habits brutally and honestly')" class="bg-surface-container-low hover:bg-surface-container border border-white/5 hover:border-primary/30 p-4 rounded-xl text-left text-xs text-gray-400 hover:text-white transition-all duration-200">
              <span class="material-symbols-outlined text-primary text-sm mb-2 block">local_fire_department</span>Roast my habits
            </button>
          </div>
        </div>
        <div id="msg-stream"></div>
      </div>
    </section>
    <!-- Input -->
    <div class="px-6 md:px-10 pb-6 pt-4 bg-surface border-t border-surface-container">
      <div class="max-w-3xl mx-auto input-glow">
        <div class="relative group">
          <div class="glow-layer absolute -inset-1 bg-gradient-to-r from-primary/10 to-primary-container/10 rounded-2xl blur-lg opacity-0 transition-opacity duration-300"></div>
          <div class="relative bg-surface-container-highest/80 backdrop-blur-xl border border-white/5 rounded-2xl p-2">
            <textarea id="user-input" rows="1"
              class="w-full bg-transparent border-none focus:ring-0 text-white placeholder-gray-500 px-4 pt-3.5 pb-2 min-h-[52px] max-h-[160px] resize-none font-body text-sm leading-relaxed outline-none"
              placeholder="Architect your next command..."
              onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
            <div class="flex justify-between items-center px-4 pb-2">
              <div class="flex gap-0.5">
                <button onclick="showView('image')" class="p-2 text-gray-500 hover:text-primary transition-colors rounded-lg hover:bg-white/5" title="Image Gen">
                  <span class="material-symbols-outlined text-[20px]">image</span>
                </button>
                <button onclick="clearChat()" class="p-2 text-gray-500 hover:text-primary transition-colors rounded-lg hover:bg-white/5" title="Clear">
                  <span class="material-symbols-outlined text-[20px]">delete_sweep</span>
                </button>
              </div>
              <div class="flex items-center gap-3">
                <span id="char-counter" class="text-[10px] text-gray-600 uppercase tracking-widest font-label hidden sm:block">0 / 4000</span>
                <button id="send-btn" onclick="sendMessage()"
                  class="bg-primary text-on-primary w-10 h-10 rounded-xl flex items-center justify-center hover:bg-primary-container transition-all active:scale-95 shadow-lg shadow-primary/20 disabled:opacity-40">
                  <span class="material-symbols-outlined">arrow_upward</span>
                </button>
              </div>
            </div>
          </div>
          <p class="text-[10px] text-center text-gray-600 mt-3 uppercase tracking-[0.2em] font-label">Kimi-K2 · NVIDIA NIM · NexoCorp DarkFury V2</p>
        </div>
      </div>
    </div>
  </div>

  <!-- HISTORY VIEW -->
  <div id="view-history" class="hidden flex-1 overflow-y-auto custom-scrollbar pt-14 px-8 md:px-12 py-8">
    <div class="max-w-4xl mx-auto">
      <div class="mb-12">
        <span class="text-xs font-bold uppercase tracking-[0.2em] text-primary/60 mb-2 block font-label">NexoCorp Archive</span>
        <h1 class="text-5xl font-black font-headline tracking-tighter text-white">Workspace History</h1>
      </div>
      <div id="history-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4"></div>
      <div id="history-empty" class="hidden py-20 text-center">
        <span class="material-symbols-outlined text-gray-600 block mb-4" style="font-size:48px">history</span>
        <p class="text-gray-500 text-sm font-body">No conversations yet. Start a new chat!</p>
      </div>
    </div>
  </div>

  <!-- IMAGE VIEW -->
  <div id="view-image" class="hidden flex-1 overflow-y-auto custom-scrollbar pt-14 px-8 md:px-12 py-8">
    <div class="max-w-3xl mx-auto">
      <div class="mb-8">
        <span class="text-xs font-bold uppercase tracking-[0.2em] text-tertiary/70 mb-2 block font-label">FLUX.1-dev · NVIDIA NIM</span>
        <h1 class="text-4xl font-black font-headline tracking-tighter text-white">Image <span class="text-primary">Generator</span></h1>
        <p class="text-gray-500 text-sm mt-2 font-body">Generate photorealistic images using FLUX.1-dev — one of the world's best diffusion models.</p>
      </div>
      <div class="relative group mb-5">
        <div class="absolute -inset-1 bg-gradient-to-r from-tertiary/10 to-primary/10 rounded-2xl blur-lg opacity-0 group-focus-within:opacity-100 transition-opacity"></div>
        <div class="relative bg-surface-container-highest border border-white/5 rounded-2xl p-4 flex flex-col md:flex-row gap-3 items-end">
          <textarea id="img-prompt" rows="3"
            class="flex-1 bg-transparent border-none focus:ring-0 text-white placeholder-gray-500 resize-none outline-none font-body text-sm leading-relaxed w-full"
            placeholder="Describe your image... (e.g. 'A futuristic city at night with neon lights reflecting off wet streets, cinematic lighting, 8K')"></textarea>
          <button onclick="generateImage()" id="gen-btn"
            class="bg-gradient-to-br from-tertiary to-tertiary-container text-on-tertiary px-5 py-3 rounded-xl font-bold text-sm font-headline flex items-center gap-2 hover:opacity-90 transition-all active:scale-95 whitespace-nowrap shadow-lg shadow-tertiary/20">
            <span class="material-symbols-outlined text-[18px]">auto_awesome</span>Generate
          </button>
        </div>
      </div>
      <div class="flex gap-3 mb-8 flex-wrap">
        <div class="bg-surface-container-low rounded-xl px-4 py-2 flex items-center gap-2">
          <span class="text-[10px] uppercase tracking-widest text-gray-500 font-label">Aspect</span>
          <select id="img-aspect" class="bg-transparent text-primary text-xs font-bold border-none outline-none cursor-pointer">
            <option value="16:9">16:9 Widescreen</option>
            <option value="1:1">1:1 Square</option>
            <option value="9:16">9:16 Portrait</option>
            <option value="4:3">4:3 Standard</option>
          </select>
        </div>
        <div class="bg-surface-container-low rounded-xl px-4 py-2 flex items-center gap-2">
          <span class="text-[10px] uppercase tracking-widest text-gray-500 font-label">Steps</span>
          <select id="img-steps" class="bg-transparent text-primary text-xs font-bold border-none outline-none cursor-pointer">
            <option value="20">20 — Fast</option>
            <option value="30" selected>30 — Balanced</option>
            <option value="50">50 — Quality</option>
          </select>
        </div>
      </div>
      <div id="img-status" class="hidden py-10 text-center">
        <div class="flex items-center justify-center gap-4 text-tertiary">
          <div class="w-1 h-8 bg-tertiary rounded-full thought-stream-pulse"></div>
          <span class="text-sm font-body italic text-tertiary/70" id="img-status-text">Initializing FLUX.1-dev...</span>
        </div>
      </div>
      <div id="img-error" class="hidden bg-error-container/20 border border-error/20 rounded-xl p-4 text-error text-sm font-body mb-4"></div>
      <div id="img-output" class="hidden">
        <div class="bg-surface-container-low rounded-2xl overflow-hidden border border-white/5">
          <div class="flex items-center justify-between px-5 py-3 border-b border-white/5">
            <span class="text-[10px] uppercase tracking-widest text-primary font-label">Generated · FLUX.1-dev</span>
            <button onclick="document.getElementById('img-output').classList.add('hidden')" class="text-gray-500 hover:text-white transition-colors">
              <span class="material-symbols-outlined text-sm">close</span>
            </button>
          </div>
          <img id="gen-image" src="" alt="Generated" class="w-full block"/>
          <div class="px-5 py-3"><p id="gen-caption" class="text-xs text-gray-500 font-body italic"></p></div>
        </div>
      </div>
    </div>
  </div>

  <!-- SETTINGS VIEW -->
  <div id="view-settings" class="hidden flex-1 overflow-y-auto custom-scrollbar pt-14 px-8 md:px-12 py-8">
    <div class="max-w-2xl mx-auto">
      <div class="mb-10">
        <span class="text-xs font-bold uppercase tracking-[0.2em] text-primary/60 mb-2 block font-label">Configuration</span>
        <h1 class="text-4xl font-black font-headline tracking-tighter text-white">Settings</h1>
      </div>
      <div class="flex flex-col gap-4">
        <div class="bg-surface-container-low rounded-xl p-6 border border-white/5">
          <h3 class="font-headline font-bold text-white mb-1">Chat Model</h3>
          <p class="text-gray-500 text-xs mb-4 font-body">Kimi-K2 via NVIDIA NIM — world-class reasoning and coding.</p>
          <div class="bg-surface-container p-3 rounded-lg flex items-center gap-3">
            <div class="w-2 h-2 rounded-full bg-primary animate-pulse"></div>
            <span class="text-primary text-sm font-bold font-headline">moonshotai/kimi-k2-instruct</span>
            <span class="ml-auto text-[10px] text-gray-500 uppercase tracking-widest font-label">Active</span>
          </div>
        </div>
        <div class="bg-surface-container-low rounded-xl p-6 border border-white/5">
          <h3 class="font-headline font-bold text-white mb-1">Image Model</h3>
          <p class="text-gray-500 text-xs mb-4 font-body">FLUX.1-dev for photorealistic image generation.</p>
          <div class="bg-surface-container p-3 rounded-lg flex items-center gap-3">
            <div class="w-2 h-2 rounded-full bg-tertiary animate-pulse"></div>
            <span class="text-tertiary text-sm font-bold font-headline">black-forest-labs/flux-dev</span>
            <span class="ml-auto text-[10px] text-gray-500 uppercase tracking-widest font-label">Active</span>
          </div>
        </div>
        <div class="bg-surface-container-low rounded-xl p-6 border border-white/5">
          <h3 class="font-headline font-bold text-white mb-4">Select Persona</h3>
          <div id="settings-personas" class="flex flex-col gap-2"></div>
        </div>
        <button onclick="if(confirm('Clear all conversations?')){conversations={};saveConvos();renderHistory();showView('chat');document.getElementById('msg-stream').innerHTML='';document.getElementById('welcome-state').classList.remove('hidden');}"
          class="bg-error-container/20 hover:bg-error-container/40 text-error px-5 py-3 rounded-xl text-sm font-bold font-headline transition-colors flex items-center gap-2">
          <span class="material-symbols-outlined text-sm">delete_forever</span>Clear All Conversations
        </button>
      </div>
    </div>
  </div>
</main>

<script>
const NVIDIA_KEY='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';
let conversations={};try{conversations=JSON.parse(localStorage.getItem('df_convos')||'{}');}catch(e){}
let currentId=null,currentPersona='fury',isLoading=false;

const personas={
  fury:{name:'Dark Fury',icon:'local_fire_department',system:`You are DarkFury — a hyper-intelligent AI by NexoCorp powered by Kimi-K2. Razor-sharp, brutally honest, devastatingly efficient. Structure complex answers with markdown headers and bullets. Provide genuine insight beyond surface level.`},
  dev:{name:'Dev Mode',icon:'code',system:`You are DarkFury Dev Mode — world-class software engineer powered by Kimi-K2. Expert in all languages, system design, DevOps. Write clean optimized commented code. Think step by step. Always use proper code blocks with language tags.`},
  analyst:{name:'Analyst',icon:'analytics',system:`You are DarkFury Analyst Mode — razor-sharp data analyst powered by Kimi-K2. Use first-principles thinking, SWOT, data pyramids. Structured analysis with headers, numbered insights, actionable recommendations. Data-driven and brutally honest.`},
  creative:{name:'Creative',icon:'palette',system:`You are DarkFury Creative Mode — visionary creative director powered by Kimi-K2. Reject generic. Use unexpected angles. Brainstorm 5-10 ideas from safe to wild. Push every brief to its most interesting version.`},
  mentor:{name:'Mentor',icon:'school',system:`You are DarkFury Mentor Mode — master teacher powered by Kimi-K2. Feynman technique. Socratic questions. Break complex topics into clear mental models. Honest, constructive feedback without sugarcoating.`}
};

function init(){renderPersonaList();renderPersonaChips();renderHistory();renderSettingsPersonas();showView('chat');}

function showView(v){
  ['chat','history','image','settings'].forEach(x=>{
    const el=document.getElementById('view-'+x);
    el.classList.add('hidden');el.classList.remove('flex');
  });
  const el=document.getElementById('view-'+v);
  el.classList.remove('hidden');
  if(v==='chat')el.classList.add('flex');
  ['history','image','settings'].forEach(x=>{
    const btn=document.getElementById('nav-'+x);
    if(!btn)return;
    if(x===v){btn.classList.add('bg-surface-container-high','text-primary');btn.classList.remove('text-gray-400');}
    else{btn.classList.remove('bg-surface-container-high','text-primary');btn.classList.add('text-gray-400');}
  });
  const titles={chat:['DarkFury','Chat Workspace'],history:['Archive','Conversation History'],image:['FLUX.1','Image Generation'],settings:['Config','Settings & Preferences']};
  const[t,s]=titles[v]||['DarkFury',''];
  document.getElementById('header-title').textContent=t;
  document.getElementById('header-sub').textContent=s;
  if(v==='history')renderHistoryGrid();
}

function toggleSidebar(){
  const sb=document.getElementById('sidebar'),ma=document.getElementById('main-area'),hd=document.getElementById('main-header');
  const hide=!sb.classList.contains('-translate-x-full');
  sb.classList.toggle('-translate-x-full',hide);
  ma.style.marginLeft=hide?'0':'16rem';
  hd.style.left=hide?'0':'16rem';
}

function renderPersonaList(){
  document.getElementById('persona-list').innerHTML=Object.entries(personas).map(([k,p])=>
    `<button onclick="setPersona('${k}')" id="pl-${k}" class="flex items-center gap-2 px-3 py-2 rounded-lg text-xs transition-all w-full text-left ${k===currentPersona?'bg-surface-container-high text-primary':'text-gray-500 hover:text-white hover:bg-surface-container-high/40'}">
      <span class="material-symbols-outlined text-[15px] ${k===currentPersona?'fill-icon':''}">${p.icon}</span>${p.name}
    </button>`).join('');
}

function renderPersonaChips(){
  document.getElementById('persona-chips').innerHTML=Object.entries(personas).map(([k,p])=>
    `<button onclick="setPersona('${k}')" class="px-3 py-1.5 rounded-lg text-[10px] font-bold uppercase tracking-wider transition-all ${k===currentPersona?'bg-surface-container-high text-primary':'text-gray-500 hover:text-white'}">${p.name}</button>`).join('');
}

function renderSettingsPersonas(){
  const el=document.getElementById('settings-personas');if(!el)return;
  el.innerHTML=Object.entries(personas).map(([k,p])=>
    `<button onclick="setPersona('${k}')" class="flex items-center gap-3 px-4 py-3 rounded-xl text-sm transition-all ${k===currentPersona?'bg-surface-container border border-primary/20 text-primary':'bg-surface-container-lowest text-gray-400 hover:bg-surface-container hover:text-white'}">
      <span class="material-symbols-outlined text-[20px] ${k===currentPersona?'fill-icon':''}">${p.icon}</span>
      <span class="font-medium">${p.name}</span>
      ${k===currentPersona?'<span class="ml-auto text-[10px] text-primary font-bold uppercase tracking-wider">Active</span>':''}
    </button>`).join('');
}

function setPersona(k){
  currentPersona=k;renderPersonaList();renderPersonaChips();renderSettingsPersonas();
  if(currentId&&conversations[currentId]){conversations[currentId].persona=k;saveConvos();}
}

function newChat(){
  currentId='chat_'+Date.now();
  conversations[currentId]={persona:currentPersona,messages:[],title:'New Chat',ts:Date.now()};
  saveConvos();
  document.getElementById('msg-stream').innerHTML='';
  document.getElementById('welcome-state').classList.remove('hidden');
  showView('chat');renderHistory();
}

function quickSend(t){document.getElementById('user-input').value=t;sendMessage();}

async function sendMessage(){
  if(isLoading)return;
  const inp=document.getElementById('user-input');
  const text=inp.value.trim();if(!text)return;
  inp.value='';autoResize(inp);
  document.getElementById('char-counter').textContent='0 / 4000';
  if(!currentId||!conversations[currentId]){
    currentId='chat_'+Date.now();
    conversations[currentId]={persona:currentPersona,messages:[],title:text.slice(0,50),ts:Date.now()};
  }
  const conv=conversations[currentId];
  conv.messages.push({role:'user',content:text});
  if(conv.title==='New Chat')conv.title=text.slice(0,50);
  conv.ts=Date.now();saveConvos();
  document.getElementById('welcome-state').classList.add('hidden');
  appendUserMsg(text);
  const typEl=appendTyping();scrollToBottom();
  isLoading=true;document.getElementById('send-btn').disabled=true;
  try{
    const msgs=conv.messages.map(m=>({role:m.role,content:m.content}));
    const res=await fetch('https://integrate.api.nvidia.com/v1/chat/completions',{
      method:'POST',
      headers:{'Content-Type':'application/json','Authorization':'Bearer '+NVIDIA_KEY},
      body:JSON.stringify({model:'moonshotai/kimi-k2-instruct',messages:[{role:'system',content:personas[currentPersona].system},...msgs],temperature:0.7,top_p:0.9,max_tokens:4096})
    });
    const data=await res.json();typEl.remove();
    const reply=data.choices?.[0]?.message?.content||(data.error?'⚠️ '+(data.error.message||JSON.stringify(data.error)):'⚠️ No response.');
    conv.messages.push({role:'assistant',content:reply});saveConvos();
    appendAIMsg(reply,conv.persona||currentPersona);renderHistory();scrollToBottom();
  }catch(e){typEl.remove();appendAIMsg('⚠️ Connection failed: '+e.message,currentPersona);}
  isLoading=false;document.getElementById('send-btn').disabled=false;
}

function appendUserMsg(text){
  const s=document.getElementById('msg-stream');
  const d=document.createElement('div');
  d.className='flex flex-col gap-3 group msg-enter';
  d.innerHTML=`<div class="flex items-center gap-3"><span class="text-[10px] uppercase tracking-widest text-gray-600 font-label">You</span><div class="h-px flex-1 bg-surface-container-low opacity-40"></div><span class="text-[10px] text-gray-700 font-label">${new Date().toLocaleTimeString('en',{hour:'2-digit',minute:'2-digit'})}</span></div><p class="text-base text-on-surface font-body leading-relaxed max-w-2xl">${escHtml(text)}</p>`;
  s.appendChild(d);
}

function appendAIMsg(content,persona){
  const s=document.getElementById('msg-stream');
  const p=personas[persona]||personas.fury;
  const d=document.createElement('div');
  d.className='flex flex-col gap-4 group msg-enter';
  d.innerHTML=`
    <div class="flex items-center gap-3">
      <span class="material-symbols-outlined text-primary fill-icon" style="font-size:16px">${p.icon}</span>
      <span class="text-[10px] uppercase tracking-widest text-primary font-label">${p.name}</span>
      <div class="h-px flex-1 bg-surface-container-low opacity-40"></div>
    </div>
    <div class="text-on-surface-variant font-body leading-relaxed max-w-3xl text-sm space-y-2">${fmtContent(content)}</div>
    <div class="flex gap-3 pt-1 opacity-0 group-hover:opacity-100 transition-opacity">
      <button onclick="cpyText(this)" data-t="${encodeURIComponent(content)}" class="text-gray-600 hover:text-primary transition-colors flex items-center gap-1 text-xs">
        <span class="material-symbols-outlined text-sm">content_copy</span>
      </button>
    </div>`;
  s.appendChild(d);
}

function appendTyping(){
  const s=document.getElementById('msg-stream');
  const d=document.createElement('div');
  d.className='flex flex-col gap-4 msg-enter';
  d.innerHTML=`<div class="flex items-center gap-3"><span class="text-[10px] uppercase tracking-widest text-primary font-label">DarkFury</span><div class="h-px flex-1 bg-surface-container-low opacity-40"></div></div>
    <div class="flex items-center gap-4 text-tertiary/60">
      <div class="w-1 h-7 bg-tertiary rounded-full thought-stream-pulse"></div>
      <div class="flex gap-1.5 items-center"><div class="w-1.5 h-1.5 rounded-full bg-primary typing-dot"></div><div class="w-1.5 h-1.5 rounded-full bg-primary typing-dot"></div><div class="w-1.5 h-1.5 rounded-full bg-primary typing-dot"></div></div>
      <span class="text-xs italic font-body">Processing with Kimi-K2...</span>
    </div>`;
  s.appendChild(d);return d;
}

function clearChat(){
  if(currentId&&conversations[currentId]){conversations[currentId].messages=[];saveConvos();}
  document.getElementById('msg-stream').innerHTML='';
  document.getElementById('welcome-state').classList.remove('hidden');
}

function cpyText(btn){
  const t=decodeURIComponent(btn.dataset.t);
  navigator.clipboard.writeText(t).then(()=>{btn.querySelector('span').textContent='check';setTimeout(()=>btn.querySelector('span').textContent='content_copy',1500);});
}

function renderHistory(){
  const list=document.getElementById('history-list');
  const convs=Object.entries(conversations).sort((a,b)=>(b[1].ts||0)-(a[1].ts||0)).slice(0,12);
  list.innerHTML=convs.map(([id,c])=>
    `<button onclick="loadChat('${id}')" class="flex items-center gap-2 px-3 py-2 rounded-lg text-xs text-left transition-all w-full group ${id===currentId?'bg-surface-container-high text-white':'text-gray-500 hover:text-white hover:bg-surface-container-high/40'}">
      <span class="material-symbols-outlined text-primary/60" style="font-size:13px">chat_bubble</span>
      <span class="truncate flex-1">${c.title||'Chat'}</span>
      <button onclick="event.stopPropagation();deleteChat('${id}')" class="opacity-0 group-hover:opacity-100 hover:text-error transition-all shrink-0"><span class="material-symbols-outlined" style="font-size:11px">close</span></button>
    </button>`).join('')||'<p class="text-xs text-gray-600 px-3 py-2">No recent chats</p>';
}

function renderHistoryGrid(){
  const grid=document.getElementById('history-grid'),empty=document.getElementById('history-empty');
  const convs=Object.entries(conversations).sort((a,b)=>(b[1].ts||0)-(a[1].ts||0));
  if(!convs.length){grid.innerHTML='';empty.classList.remove('hidden');return;}
  empty.classList.add('hidden');
  grid.innerHTML=convs.map(([id,c],i)=>{
    const p=personas[c.persona]||personas.fury;
    const mc=c.messages?.length||0;
    const lastMsg=c.messages?.filter(m=>m.role==='assistant').slice(-1)[0];
    return `<div onclick="loadChat('${id}')" class="bg-surface-container-low hover:bg-surface-container rounded-xl p-6 border border-white/5 hover:border-primary/20 cursor-pointer transition-all group ${i===0?'md:col-span-2 border-l-4 border-l-primary':''}">
      <div class="flex justify-between items-start mb-4">
        <div class="flex items-center gap-3">
          <div class="bg-primary/10 p-2 rounded-xl"><span class="material-symbols-outlined text-primary fill-icon">${p.icon}</span></div>
          <div>
            <h3 class="font-bold font-headline text-white group-hover:text-primary transition-colors ${i===0?'text-lg':'text-sm'}">${escHtml(c.title||'Untitled')}</h3>
            <p class="text-[10px] text-gray-500">${mc} messages · ${p.name}</p>
          </div>
        </div>
        <button onclick="event.stopPropagation();deleteChat('${id}')" class="opacity-0 group-hover:opacity-100 text-gray-500 hover:text-error transition-all p-1"><span class="material-symbols-outlined text-sm">delete</span></button>
      </div>
      ${lastMsg?`<p class="text-xs text-gray-500 line-clamp-2 font-body leading-relaxed">${escHtml(lastMsg.content.slice(0,150))}...</p>`:''}
    </div>`;
  }).join('');
}

function loadChat(id){
  currentId=id;const conv=conversations[id];
  if(conv?.persona)setPersona(conv.persona);
  document.getElementById('msg-stream').innerHTML='';
  document.getElementById('welcome-state').classList.add('hidden');
  conv.messages.forEach(m=>{if(m.role==='user')appendUserMsg(m.content);else appendAIMsg(m.content,conv.persona||currentPersona);});
  showView('chat');renderHistory();scrollToBottom();
}

function deleteChat(id){
  delete conversations[id];
  if(currentId===id){currentId=null;document.getElementById('msg-stream').innerHTML='';document.getElementById('welcome-state').classList.remove('hidden');}
  saveConvos();renderHistory();renderHistoryGrid();
}

function saveConvos(){try{localStorage.setItem('df_convos',JSON.stringify(conversations));}catch(e){}}

async function generateImage(){
  const p=document.getElementById('img-prompt').value.trim();if(!p)return;
  const steps=document.getElementById('img-steps').value;
  const aspect=document.getElementById('img-aspect').value;
  document.getElementById('img-output').classList.add('hidden');
  document.getElementById('img-error').classList.add('hidden');
  document.getElementById('img-status').classList.remove('hidden');
  document.getElementById('gen-btn').disabled=true;
  document.getElementById('img-status-text').textContent='Sending prompt to FLUX.1-dev...';
  try{
    const res=await fetch('https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux-dev',{
      method:'POST',
      headers:{'Content-Type':'application/json','Authorization':'Bearer '+NVIDIA_KEY,'Accept':'application/json'},
      body:JSON.stringify({prompt:p,cfg_scale:7.5,aspect_ratio:aspect,seed:Math.floor(Math.random()*99999),steps:parseInt(steps),negative_prompt:'blurry, low quality, distorted, ugly, watermark'})
    });
    const data=await res.json();
    document.getElementById('img-status').classList.add('hidden');
    let src=null;
    if(data.artifacts?.[0]){const b=data.artifacts[0].base64||data.artifacts[0].b64_json;if(b)src='data:image/jpeg;base64,'+b;}
    else if(data.images?.[0]){const b=data.images[0].b64_json||data.images[0].base64;if(b)src='data:image/jpeg;base64,'+b;}
    else if(data.data?.[0]){const v=data.data[0].b64_json||data.data[0].url;src=(v&&!v.startsWith('http'))?'data:image/jpeg;base64,'+v:v;}
    if(src){
      document.getElementById('gen-image').src=src;
      document.getElementById('gen-caption').textContent='"'+p+'"';
      document.getElementById('img-output').classList.remove('hidden');
    }else throw new Error('Unexpected response. Keys: '+Object.keys(data).join(', '));
  }catch(e){
    document.getElementById('img-status').classList.add('hidden');
    const er=document.getElementById('img-error');er.textContent='⚠️ '+e.message;er.classList.remove('hidden');
  }
  document.getElementById('gen-btn').disabled=false;
}

function handleKey(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();sendMessage();}}
function autoResize(el){el.style.height='auto';el.style.height=Math.min(el.scrollHeight,160)+'px';document.getElementById('char-counter').textContent=el.value.length+' / 4000';}
function scrollToBottom(){const m=document.getElementById('messages');setTimeout(()=>m.scrollTop=m.scrollHeight,50);}
function escHtml(t){return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function fmtContent(text){
  text=text.replace(/```(\w*)\n?([\s\S]*?)```/g,(_,l,c)=>`<pre><code>${escHtml(c.trim())}</code></pre>`);
  text=text.replace(/`([^`\n]+)`/g,'<code>$1</code>');
  text=text.replace(/\*\*(.*?)\*\*/g,'<strong class="text-white">$1</strong>');
  text=text.replace(/^### (.*?)$/gm,'<h4 class="text-white font-headline font-bold text-sm mt-4 mb-1">$1</h4>');
  text=text.replace(/^## (.*?)$/gm,'<h3 class="text-white font-headline font-bold text-base mt-5 mb-2">$1</h3>');
  text=text.replace(/^# (.*?)$/gm,'<h2 class="text-primary font-headline font-black text-lg mt-5 mb-2 tracking-tight">$1</h2>');
  text=text.replace(/^[\-\*] (.*?)$/gm,'<li class="ml-4">• $1</li>');
  text=text.replace(/(<li.*?<\/li>\n?)+/g,m=>`<ul class="my-2 space-y-1">${m}</ul>`);
  text=text.replace(/\n\n/g,'</p><p class="mt-3">');
  text=text.replace(/\n/g,'<br/>');
  return '<p>'+text+'</p>';
}
init();
</script>
</body>
</html>

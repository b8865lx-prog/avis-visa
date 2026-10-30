const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const hd=$('header');addEventListener('scroll',()=>hd.classList.toggle('s',scrollY>20),{passive:true});
$('.mn').onclick=()=>$('nav').classList.toggle('o');$$('nav a').forEach(a=>a.onclick=()=>$('nav').classList.remove('o'));
const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{threshold:.2});
$$('.rv').forEach(x=>io.observe(x));
$$('form[data-wa]').forEach(f=>f.onsubmit=e=>{e.preventDefault();
 const l=[...new FormData(f)].filter(([k,v])=>v.trim()).map(([k,v])=>k+': '+v);
 open('https://wa.me/'+WA+'?text='+encodeURIComponent('Halo AVis, saya mau konsultasi visa.\n'+l.join('\n')),'_blank')});
$$('.loop').forEach(b=>{const t=b.firstElementChild;const n=t.children.length;t.innerHTML+=t.innerHTML;[...t.children].slice(n).forEach(c=>{c.setAttribute('aria-hidden','true');$$('a',c).forEach(x=>x.tabIndex=-1)});
 let x=0,hold=false,drag=false,sx=0,mv=0;const h=()=>t.scrollWidth/2,rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
 (function f(){if(!hold&&!drag&&!rm)x-=.5;if(x<-h())x+=h();if(x>0)x-=h();t.style.transform='translateX('+x+'px)';requestAnimationFrame(f)})();
 b.addEventListener('pointerdown',e=>{drag=true;mv=0;sx=e.clientX-x});
 addEventListener('pointermove',e=>{if(drag){mv=Math.abs(e.clientX-x-sx);x=e.clientX-sx}});
 addEventListener('pointerup',()=>drag=false);
 b.addEventListener('click',e=>{if(mv>8){e.preventDefault();mv=0}},true);
 b.onmouseenter=()=>hold=true;b.onmouseleave=()=>hold=false});

/* Pop up promo WHV: muncul 1x per sesi di main page */
(()=>{const m=$('#promo');if(!m)return;const K='avis_promo_whv';
try{if(sessionStorage.getItem(K))return}catch(_){}
let last;const seen=()=>{try{sessionStorage.setItem(K,'1')}catch(_){}};
const tutup=()=>{m.classList.remove('o');m.setAttribute('aria-hidden','true');document.body.style.overflow='';seen();last&&last.focus&&last.focus()};
const buka=()=>{last=document.activeElement;m.classList.add('o');m.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';$('.pmb',m).focus()};
setTimeout(buka,1500);
m.addEventListener('click',ev=>{if(ev.target===m||ev.target.closest('[data-x]'))tutup()});
$('.pmb',m).addEventListener('click',seen);
addEventListener('keydown',ev=>{if(!m.classList.contains('o'))return;
 if(ev.key==='Escape')return tutup();
 if(ev.key==='Tab'){const f=$$('button,a',m);const a=f[0],z=f[f.length-1];
  if(ev.shiftKey&&document.activeElement===a){ev.preventDefault();z.focus()}
  else if(!ev.shiftKey&&document.activeElement===z){ev.preventDefault();a.focus()}}});
})();

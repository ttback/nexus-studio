"use strict";(self.webpackChunkAutoGen_Studio=self.webpackChunkAutoGen_Studio||[]).push([[116],{48861:function(e,t,a){a.r(t),a.d(t,{default:function(){return v}});var l=a(96540),s=a(18504),n=a(92744),r=a(70870),c=a(63532),m=a(68777),i=a(42489),o=a(85575),d=a(54015),u=a(28007),g=a(43881);var E=e=>{let{location:t}=e;const a=(0,r.Tt)(),{user:s}=l.useContext(n.v),[E,v]=l.useState(!1),[p,y]=l.useState(null),[h,N]=l.useState(null),f=a+"/gallery?user_id="+(null==s?void 0:s.email),[x,b]=l.useState({status:!0,message:"All good"}),[w,k]=l.useState(null);l.useEffect((()=>{const e=new URLSearchParams(t.search).get("id");e?(A(e),k(e)):A(null)}),[]);const A=e=>{const t=e?a+"/gallery?gallery_id="+e:f;b(null),v(!0);(0,r.hI)(t,{method:"GET",headers:{"Content-Type":"application/json"}},(t=>{t&&t.status?(console.log("gallery",t),e?N(t.data[0]):y(t.data)):c.Ay.error(t.message),v(!1)}),(e=>{b(e),c.Ay.error(e.message),v(!1)}))},S=e=>{let{item:t}=e;return l.createElement("div",null,l.createElement("div",{className:"mb-4 text-sm"},"This session contains ",t.messages.length," messages and was created"," ",(0,r.fF)(t.timestamp)),l.createElement("div",{className:""},l.createElement(g.A,{initMessages:t.messages,editable:!1})))},C=e=>{let{tags:t}=e;const a=t.map(((e,t)=>l.createElement("div",{key:"tag"+t,className:"mr-2 inline-block"},l.createElement("span",{className:"text-xs bg-secondary border px-3 p-1 rounded"},e))));return l.createElement("div",{className:"flex flex-wrap"},a)},G=null==p?void 0:p.map(((e,t)=>{var a,s;const n=(null==h?void 0:h.id)===e.id;return l.createElement("div",{key:"galleryrow"+t,className:""},l.createElement(i.Zp,{active:n,onClick:()=>{N(e),(0,u.navigate)("/gallery?id="+e.id)},className:"h-full p-2 cursor-pointer",title:(0,r.EJ)((null===(a=e.messages[0])||void 0===a?void 0:a.content)||"",20)},l.createElement("div",{className:"my-2"}," ",(0,r.EJ)((null===(s=e.messages[0])||void 0===s?void 0:s.content)||"",80)),l.createElement("div",{className:"text-xs"}," ",e.messages.length," message",e.messages.length>1&&"s"),l.createElement("div",{className:"my-2 border-t border-dashed w-full pt-2 inline-flex gap-2 "},l.createElement(C,{tags:e.tags})," "),l.createElement("div",{className:"text-xs"},(0,r.fF)(e.timestamp))))}));return l.createElement("div",{className:" "},l.createElement("div",{className:"mb-4 text-2xl"},"Gallery"),h&&l.createElement("div",{className:"mb-4   w-full"},l.createElement(m.Ay,{type:"primary",onClick:()=>{N(null),(0,u.navigate)("/gallery?_="+Date.now()),w&&(A(null),k(null))},className:"bg-primary text-white px-2 py-1 rounded"},l.createElement(o.A,{className:"h-4 w-4 inline mr-1"}),"Back to gallery")),!h&&l.createElement(l.Fragment,null,l.createElement("div",null,"View a collection of AutoGen agent specifications and sessions"," "),l.createElement("div",{className:"mt-4 grid gap-3 grid-cols-2 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6"},G)),p&&0===p.length&&l.createElement("div",{className:"text-sm border rounded text-secondary p-2"},l.createElement(d.A,{className:"h-4 w-4 inline mr-1"}),"No gallery items found. Please create a chat session and publish to gallery."),h&&l.createElement("div",{className:"mt-4 border-t pt-2"},l.createElement(S,{item:h})),E&&l.createElement("div",{className:"w-full text-center boder mt-4"},l.createElement("div",null," ",l.createElement(i.g0,null)),"loading gallery"))};var v=e=>{let{location:t,data:a}=e;return l.createElement(s.A,{meta:a.site.siteMetadata,title:"Gallery",link:"/gallery"},l.createElement("main",{style:{height:"100%"},className:" h-full "},l.createElement(E,{location:t})))}}}]);
//# sourceMappingURL=component---src-pages-gallery-index-tsx-480455c98d1f657356fd.js.map
import React from 'react'
import Router from 'next/router'
import Link from 'next/link'
const Home=()=>(
  <>
    <div>我是新首页</div>
    <div><Link href="/jspangA?name=lilll">去a页面</Link></div>
    <div><Link href="/jspangB">去b页面</Link></div>
    <div><button onClick={()=>Router.push("/jspangA")}>JspangA</button></div>
  </>
);
export default Home;
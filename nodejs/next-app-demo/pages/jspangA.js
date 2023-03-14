import Link from 'next/link'
import { withRouter } from 'next/router'

export default withRouter(({router})=>(
    <>
        <div> {router.query.name}JSpang-a page</div>
        <Link href="/index2">返回首页</Link>
    </>

));
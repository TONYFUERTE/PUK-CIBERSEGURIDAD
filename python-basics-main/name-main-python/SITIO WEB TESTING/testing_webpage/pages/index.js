import Head from 'next/head'
import Layout, { siteTitle } from '../components/layout'
import utilStyles from '../styles/utils.module.css'

export default function Home() {

  const titulo = "Login"

  return (
    <Layout titulo="Login">
      <Head>
          <title>{ titulo }</title>
          <script src="/static/login.js"></script>
      </Head>
      
      <div className={utilStyles.alignment}>
      <label><b>Username</b></label><br></br>
      <div><input id="username" className={utilStyles.textboxes} type="text" placeholder="Enter Username" name="username"/></div>
      <br></br>
      <label><b>Password</b></label><br></br>
      <div><input id="password" className={utilStyles.textboxes} type="password" placeholder="Enter Password" name="password"/></div>
      <br></br>
      <div><button id="loginButton" className={utilStyles.botones}>Login</button></div>

      <h2>Mensaje:</h2>
      <div id="resultado"></div>

      <footer>
      <script src="/static/login.js"></script>
      </footer>

    </div>
    </Layout>
  )
}

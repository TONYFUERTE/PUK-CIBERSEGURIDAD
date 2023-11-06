import Head from 'next/head'
import styles from './layout.module.css'
import utilStyles from '../styles/utils.module.css'
import Link from 'next/link'

const name = 'Jesús del Castillo'
export const siteTitle = 'Example site for testing'

export default function Layout({ children, home, titulo }) {
  return (
    <div className={styles.container}>
      <Head>
        <title>{ titulo }</title>
        <script type="text/javascript" src="/static/jquery.min.js"></script>
      </Head>
      <nav>
        <Link href="/">
          Login
        </Link>
        <Link href="/elements/checkboxes">
          Checkboxes
        </Link>
        <Link href="/elements/radiobuttons">
          Radiobuttons
        </Link>
        <Link href="/elements/comboboxes">
          Comboboxes
        </Link>
        <Link href="/elements/iframes">
          iFrames
        </Link>
        <Link href="/elements/waits">
          Waits
        </Link>
        <Link href="/elements/alerts">
          Alerts
        </Link>
        <Link href="/elements/calendars">
          Calendars
        </Link>
        <Link href="/elements/xpaths">
          XPaths
        </Link>
        <Link href="/elements/shadowdom">
          ShadowDOM
        </Link> 
        <Link href="/elements/fichar_tiempo">
          Fichar
        </Link>        
      </nav>                  
      <main>
      <h1>{ titulo }</h1>
      <script type="text/javascript" src="/static/jquery.min.js"></script>
        {children}
      </main>
      { titulo != "Login" && (
        <div className={styles.backToLogin}>
          <Link href="/">
            ← Volver a Login
          </Link>
        </div>
      )}
    </div>
  )
}

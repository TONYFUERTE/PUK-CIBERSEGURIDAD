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
          <a>Login</a>
        </Link>
        <Link href="/elements/checkboxes">
          <a>Checkboxes</a>
        </Link>
        <Link href="/elements/radiobuttons">
          <a>Radiobuttons</a>
        </Link>
        <Link href="/elements/comboboxes">
          <a>Comboboxes</a>
        </Link>
        <Link href="/elements/iframes">
          <a>iFrames</a>
        </Link>
        <Link href="/elements/waits">
          <a>Waits</a>
        </Link>
        <Link href="/elements/alerts">
          <a>Alerts</a>
        </Link>
        <Link href="/elements/calendars">
          <a>Calendars</a>
        </Link>
        <Link href="/elements/xpaths">
          <a>XPaths</a>
        </Link>
        <Link href="/elements/shadowdom">
          <a>ShadowDOM</a>
        </Link> 
        <Link href="/elements/fichar_tiempo">
          <a>Fichar</a>
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
            <a>← Volver a Login</a>
          </Link>
        </div>
      )}
    </div>
  )
}

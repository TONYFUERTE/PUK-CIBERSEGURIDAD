import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'



export default function Alerts() {
    
    const titulo = "Alerts";

    return (
        
        <Layout titulo={ titulo }>
        <Head>
          <title>{ titulo }</title>
          <script type="text/javascript" src="/static/alerts.js"></script>
        </Head>
        
        <div className={utilStyles.alignment}>
            <h2>Ejemplo para ALERTS</h2>	  
            <div><button id="buttonAlertSimple" >Púlsame para Alert SIMPLE</button></div>
            <div><button id="buttonAlertConfirm">Púlsame para Alert CONFIRM</button></div>
            <div><button id="buttonAlertPrompt" >Púlsame para Alert PROMPT</button></div>
            <h2>Mensaje:</h2>
            <div id="resultado"></div>
	    </div>
        </Layout>
        
    );
}
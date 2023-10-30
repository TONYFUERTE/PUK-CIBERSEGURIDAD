import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'

export default function Inception2() {
    return (
        <>
        <Head>
            <title>Inception DOS</title>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script type="text/javascript" src="/static/scripting.js"></script>
        </Head>

        <div className={utilStyles.alignment}>
            <h2>Saludo desde el iframe DOS</h2>
            <div>
            <button id="iframebutton">Botón del iframe 2</button>            
            </div>            

            <div id="iframetext" className={utilStyles.mensaje}>mensaje...</div>
        </div>
        
        
        </>
    )
}
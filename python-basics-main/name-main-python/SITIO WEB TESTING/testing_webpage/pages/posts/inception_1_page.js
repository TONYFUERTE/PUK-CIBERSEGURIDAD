import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'

export default function Inception1() {
    return (
        <>
        <Head>
            <title>Inception UNO</title>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script type="text/javascript" src="/static/scripting.js"></script>
        </Head>
        
        <div className={utilStyles.alignment}>
            <h2>Saludo desde el iframe UNO</h2>
            <div><button id="iframebutton">Botón del iframe 1</button></div>
            <div id="iframetext" className={utilStyles.mensaje}>mensaje...</div>
        </div>
        <br/>
        <div className={utilStyles.alignment}>
    
            <div className={utilStyles.iframe1contentChild}>
                
                <iframe id="inception_2" className={utilStyles.iframe2} src="/posts/inception_2_page" ></iframe> 
                        
            </div>
        </div>
        </>
    )
}
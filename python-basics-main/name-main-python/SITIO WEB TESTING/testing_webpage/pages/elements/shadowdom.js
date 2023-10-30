import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'



export default function ShadowDOM() {
    
    const titulo = "ShadowDOM";

    return (
        
        <Layout titulo={ titulo }>
        <Head>
          <title>{ titulo }</title>
          <script type="text/javascript" src="/static/shadowdom.js"></script>  
        </Head>
        
        <div className={utilStyles.alignment}>
            <h2>Ejemplo para ShadowDOM</h2>	  
            <div id="seccion1"><label>ESTE APARTADO ESTÁ EN EL ROOT DOM</label></div>
            <div><button id="boton1">Botón en ROOT DOM</button></div>
            <div id="nodoShadowHost"></div>
            
            
            <h2>Mensaje:</h2>
            <div id="resultado"></div>
	    </div>
        
        </Layout>
        
    );
}

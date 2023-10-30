import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'



export default function Xpaths() {
    
    const titulo = "Xpaths";

    return (
        
        <Layout titulo={ titulo }>
        <Head>
          <title>{ titulo }</title>
          <script type="text/javascript" src="/static/xpaths.js"></script>
        </Head>
        
        <div className={utilStyles.alignment}>
            <h2>Ejemplo para XPATH</h2>	  

            <div><p>Contenedor Inicial - Opción 115</p></div>
            <div><button value="Aceptar">Aceptar</button>		
            <button value="Cancelar">Cancelar</button></div>
            <div><br/><p>Contenedor Inicial - Opción 116</p></div>
            <div><button value="Aceptar">Aceptar</button>
            <button value="Cancelar">Cancelar</button></div>
            <div><br/><p>Contenedor Inicial - Opción 117</p></div>
            <div><button value="Aceptar">Aceptar</button>
            <button value="Cancelar">Cancelar</button></div>
            <div></div>
            <div><br/></div>
            <div><br/></div>
            <div></div>
            <div><br/><p>Contenedor Principal - Opción 115</p></div>
            <div><button value="Aceptar">Aceptar</button>
            <button value="Cancelar">Cancelar</button></div>
            <div><br/><p>Contenedor Principal - Opción 116</p></div>
            <div><button value="Aceptar">Aceptar</button>
            <button value="Cancelar">Cancelar</button></div>
            <div><p>Contenedor Principal - Opción 117</p></div>               
            <div><button value="Aceptar">Aceptar</button>
            <button value="Cancelar">Cancelar</button></div>
            

            <h2>Mensaje:</h2>
            <div id="resultado"></div>
	    </div>
        </Layout>
        
    );
}
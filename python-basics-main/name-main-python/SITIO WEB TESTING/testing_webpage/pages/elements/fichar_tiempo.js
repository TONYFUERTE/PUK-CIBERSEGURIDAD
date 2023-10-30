import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'



export default function Fichar() {
    
    const titulo = "Fichar";

    return (
        
        <Layout titulo={ titulo }>
        <Head>
          <title>{ titulo }</title>
          <script src="/static/fichar_tiempo.js"></script>
        </Head>
        
        <div className={utilStyles.alignment}>
            <h2>Aplicación de fichaje de tiempo</h2>	  

            <div><p>Fichar tiempo</p></div>
            <div><button id="entrada">Entrada</button>		
            <button id="salida">Salida</button></div>
            

            <h2>Mensaje:</h2>
            <div id="resultado"></div>
	    </div>
	    
	<footer>
        <script src="/static/fichar_tiempo.js"></script>
	</footer>
	
        </Layout>
        
    );
}

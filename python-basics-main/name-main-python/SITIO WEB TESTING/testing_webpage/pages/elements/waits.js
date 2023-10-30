import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'



export default function Waits() {
    
    const titulo = "Waits";

    return (
        <Layout titulo={ titulo }>
            <Head>
                <title>{ titulo }</title>                
                <script type="text/javascript" src="/static/wait_buttons.js"></script>
            </Head>

            <div>
                <h2>Contador</h2>                
                <div id="contador"></div>
            </div>

            <div>
                <h2>Ejemplo para IMPLICIT WAIT</h2>	  
                <div id="implicitWaitDiv"></div>		
            </div>
            
            
            <div>
                <h2>Ejemplo para EXPLICIT WAIT</h2>	  
                <div id="explicitWaitDiv"></div>		
            </div>


            <div>
                <h2>Mensaje:</h2>                
                <div id="resultado"></div>		
            </div>
            
        </Layout>
    )
}

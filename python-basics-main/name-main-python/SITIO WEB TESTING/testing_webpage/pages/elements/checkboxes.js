import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'




export default function Checkboxes() {
    
    const titulo = "Checkboxes";

    return (
        <Layout titulo={ titulo }>
             <Head>
                <title>{ titulo }</title>                
                <script type="text/javascript" src="/static/checkboxes.js"></script>
            </Head>
            <div className={utilStyles.alignment}>                        
			<h3>Lista de compra</h3>
				<div><input type="checkbox" name="listaCompra" value="verdura"/> Verdura</div>
				<div><input type="checkbox" name="listaCompra" value="pescado"/> Pescado</div>
				<div><input type="checkbox" name="listaCompra" value="carne"/> Carne</div>
				<div><input type="checkbox" name="listaCompra" value="kleenex"/> Kleenex</div>
            <div><button id="enviarCheckboxbutton">Mostrar seleccionados</button></div>
                
            <h2>Mensaje:</h2>
            <div id="resultado"></div>
                
            </div>
        </Layout>
    )
}
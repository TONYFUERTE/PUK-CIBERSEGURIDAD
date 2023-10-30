import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'




export default function Radiobuttons() {
    
    const titulo = "Radiobuttons";

    return (
        <Layout titulo={ titulo }>
             <Head>
                <title>{ titulo }</title>                
                <script type="text/javascript" src="/static/radiobuttons.js"></script>
            </Head>
            <div className={utilStyles.alignment}>            
            <h3>Bebidas:</h3>
				<div><input type="radio" name="bebida" value="refresco"/> Refresco<br/></div>
				<div><input type="radio" name="bebida" value="agua"/> Agua<br/></div>
				<div><input type="radio" name="bebida" value="cafe"/> Cafe<br/></div>
			<br/>
			<h3>Comidas:</h3>
				<div><input type="radio" name="comida1" value="solomillo"/> Solomillo<br/></div>
				<div><input type="radio" name="comida2" value="dorada"/> Dorada<br/></div>
				<div><input type="radio" name="comida3" value="pasta"/> Pasta<br/></div>

            <div><button id="enviarRadiobutton">Mostrar seleccionados</button></div>
                
            <h2>Mensaje:</h2>
            <div id="resultado"></div>
                
            </div>
        </Layout>
    )
}
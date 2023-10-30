import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'


export default function Comboboxes() {
    
    const titulo = "Comboboxes";

    return (
        <Layout titulo={ titulo }>
            <Head>
                <title>{ titulo }</title>                
                <script type="text/javascript" src="/static/comboboxes.js"></script>
            </Head>
            
            <div className={utilStyles.alignment}>
            <h2>Combobox Simple</h2>
                <div><select id="combobox1">
                    <option value="pan">Pan</option>
                    <option value="huevos">Huevos</option>
                    <option value="leche">Leche</option>
                    <option value="carne">Carne</option>
                </select></div>

            
            <h2>Combobox Múltiple</h2>
                <div><select id="combobox2" multiple>
                    <option value="manzana">Manzana</option>
                    <option value="pera">Pera</option>
                    <option value="platano">Plátano</option>
                    <option value="granada">Granada</option>
                </select></div>
                <br/>
                <br/>
            <div><button id="enviaComboboxes">Envía Comboboxes</button></div>

            <div><h2>Mensaje:</h2></div>
            <div id="resultado"></div>
            </div>
        </Layout>
    )
}
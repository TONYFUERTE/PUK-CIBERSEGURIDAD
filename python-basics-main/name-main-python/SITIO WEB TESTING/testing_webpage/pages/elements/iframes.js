import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'


export default function Iframes() {
    
    const titulo = "iFrames";

    return (
        <Layout titulo={ titulo }>

            <div className={utilStyles.alignment} >
                <h2>Saludo desde TOP</h2>
                <div>
                <iframe id="inception_1" className={utilStyles.iframe1} src="/posts/inception_1_page" ></iframe> 
                </div>
            </div>    
        </Layout>
    )
}
import Head from 'next/head'
import Link from 'next/link'
import Layout from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'




export default function Calendars() {
    
    const titulo = "Calendars";

    return (
        <Layout titulo={ titulo }>
             <Head>
                <title>{ titulo }</title>                
            </Head>
            <div className={utilStyles.alignment}>                        
			
                <h2>CALENDARIO - DATEPICKER</h2>	  
                <div><input type="datetime-local" name="fecha"/></div>
            </div>

        </Layout>
    )
}
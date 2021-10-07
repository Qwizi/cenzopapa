import type {NextPage} from 'next'
import React, { useState} from "react";
import {CenzoListPage} from '../components';




// @ts-ignore
const Home: NextPage = ({api_url}) =>
{
	const [pageIndex, setPageIndex] = useState(1);
	return (
		<div>
			<CenzoListPage api_url={api_url} index={pageIndex} setPageIndex={setPageIndex}/>
			<div style={{display: 'none'}}><CenzoListPage api_url={api_url} index={pageIndex + 1} setPageIndex={setPageIndex}/></div>
		</div>
	)
}

export const getServerSideProps = async () => {
	console.log(process.env.API_URL)
	return {
		props: {
			api_url: process.env.API_URL
		},
	}
}

export default Home

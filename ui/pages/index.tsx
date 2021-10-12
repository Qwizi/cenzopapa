import type {NextPage, GetServerSideProps, InferGetServerSidePropsType} from 'next'
import React, {useEffect, useState} from "react";
import {CenzoListPage} from '../components';
import {api} from "../utils";
import { useRouter } from 'next/router'


type Props = {
	images_data: object | null,
	error: string | null,
	page: number
}

const Home: NextPage<Props> = ({images_data, error, page}: InferGetServerSidePropsType<typeof getServerSideProps>) =>
{
	const [pageIndex, setPageIndex] = useState(page);

	return (
		<div>
			<CenzoListPage images_data={images_data} error={error} pageIndex={pageIndex} page={page} setPageIndex={setPageIndex}/>
{/*
			<div style={{display: 'none'}}><CenzoListPage api_url={api_url} index={pageIndex + 1} setPageIndex={setPageIndex}/></div>*!/
*/}
		</div>
	)
}


export const getServerSideProps: GetServerSideProps = async (context) => {
	try {
		const page = context.query.page || 1
		const response = await api.get(`/images/?page=${page}&size=10`);
		const data = await response.data;
		return {
			props: {
				images_data: data,
				error: null,
				page: page
			}
		}
	} catch (e: any) {

		return {
			props: {
				images_data: null,
				error: e.message,
			},
		}
	}

}

export default Home

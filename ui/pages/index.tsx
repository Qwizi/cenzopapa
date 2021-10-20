import type {NextPage, GetServerSideProps, InferGetServerSidePropsType} from 'next'
import dynamic from 'next/dynamic'
import React, {useState} from "react";
//import {CenzoListPage} from '../components';
import {api} from "../utils";
import {CountData, Image, ImagesData} from "../utils/typed";

const CenzoListPage = dynamic(() => import('../components/CenzoListPage.component'))


type Props = {
	images_data: ImagesData,
	error: string | null,
	page: number,
	pages_count: number,
	skip: number
}

const Home: NextPage<Props> = ({images_data, error, page, pages_count, skip}: InferGetServerSidePropsType<typeof getServerSideProps>) =>
{
	const [pageIndex, setPageIndex] = useState(page);

	return (
		<div>
			<CenzoListPage images_data={images_data} pages_count={pages_count} skip={skip} error={error} pageIndex={pageIndex} page={page} setPageIndex={setPageIndex}/>
		</div>
	)
}


export const getServerSideProps: GetServerSideProps = async (context) => {

	const getImagesCounts = async (api_url: string) => {
		try {
			const response = await api.get(`${api_url}/aimages/count`)
			if (response.status != 200) return {count: 0}
			return response.data;
		} catch (e) {
			console.log(e);
			return {count: 0}
		}
	}

	const getImages = async (api_url: string, skip: number = 0) => {
		try {
			const response = await api.get(`${api_url}/images/?skip=${skip}`);
			if (!response.status) return []
			return response.data;
		} catch(e) {
			console.log(e);
			return []
		}
	}

	try {
		const api_url = process.env.API_URL  ?? "https://api.jebzpapy.tk";
		console.log(api_url)
		const page = context.query.page || 1
		let skip: number;
		if (page == 1) skip = 0
		else skip = Number(page) * 10 - 10;

		const responses = await Promise.all([getImagesCounts(api_url), getImages(api_url, skip)]);
		return {
			props: {
				images_data: responses[1],
				pages_count: responses[0].count,
				error: null,
				page: page,
				skip: skip
			}
		}
	} catch (e: any) {
		console.log(e);
		return {
			props: {
				images_data: null,
				error: e.message,
			},
		}
	}

}

export default Home

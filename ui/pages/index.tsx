import type {NextPage, GetServerSideProps, InferGetServerSidePropsType} from 'next'
import React, {useState} from "react";
import {CenzoListPage} from '../components';
import {api} from "../utils";
import {Image, ImagesData} from "../utils/typed";


type Props = {
	images_data: ImagesData,
	error: string | null,
	page: number
}

const Home: NextPage<Props> = ({images_data, error, page}: InferGetServerSidePropsType<typeof getServerSideProps>) =>
{
	const [pageIndex, setPageIndex] = useState(page);

	return (
		<div>
			<CenzoListPage images_data={images_data} error={error} pageIndex={pageIndex} page={page} setPageIndex={setPageIndex}/>
		</div>
	)
}


export const getServerSideProps: GetServerSideProps = async (context) => {
	try {
		const api_url = process.env.API_URL  ?? "https://api.jebzpapy.tk";
		console.log(api_url)
		const page = context.query.page || 1
		const response = await api.get(`${api_url}/images/?page=${page}&size=10`);
		const data: ImagesData = await response.data;
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

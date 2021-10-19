import type {NextPage, GetServerSideProps, InferGetServerSidePropsType} from 'next'
import React, {useState} from "react";
import {CenzoListPage} from '../components';
import {api} from "../utils";
import {CountData, Image, ImagesData} from "../utils/typed";


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
	try {
		const api_url = process.env.API_URL  ?? "https://api.jebzpapy.tk";
		console.log(api_url)
		const page = context.query.page || 1
		let skip: number;
		if (page == 1) skip = 0
		else skip = Number(page) * 10 - 10;
		const countResponse = await api.get(`${api_url}/aimages/count`)
		const countData: CountData = await countResponse.data;
		const response = await api.get(`${api_url}/images/?skip=${skip}`);

		const data: ImagesData[] = await response.data;
		console.log(data);
		console.log(countData.count)
		return {
			props: {
				images_data: data,
				pages_count: countData.count,
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

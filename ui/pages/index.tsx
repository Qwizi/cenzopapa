import type {NextPage} from 'next'
import React, {useEffect, useState} from "react";
import {API_URL, fetcher} from "../utils";
import useSWR from 'swr'
import {CenzoListPage} from '../components';
import {useRouter} from "next/router";
import {CircularProgress} from "@mui/material";
import {Box} from "@mui/system";

const Home: NextPage = () =>
{
	const router = useRouter();
	const [pageIndex, setPageIndex] = useState(1);
	const { data, error } = useSWR(`${API_URL}/images/?page=${pageIndex}`, fetcher)

	useEffect(() => {
		if (router?.query?.page) {
			setPageIndex(Number(router.query.page));
		}

	}, [router.query])

	if (error) return <div>failed to load</div>
	if (!data) return (
		<Box mt={1} mb={5} style={{textAlign: "center", alignItems: "center"}}>
			<CircularProgress />
		</Box>
	)



	return (
		<div>
			<CenzoListPage error={error} data={data} pageIndex={pageIndex} setPageIndex={setPageIndex}/>
		</div>
	)
}

export default Home

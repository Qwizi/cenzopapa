import type {NextPage, GetServerSideProps, InferGetServerSidePropsType} from 'next'
import dynamic from 'next/dynamic'
import React, {useEffect, useState} from "react";
//import {CenzoListPage} from '../components';
import {api, fetcher} from "../utils";
import {CountData, Image} from "../utils/typed";
import useSWR from 'swr'
import {CenzoListPage} from '../components';
import {useRouter} from "next/router";
import {CircularProgress, Skeleton} from "@mui/material";
import {Box} from "@mui/system";
import {Head} from "next/document";


const Home: NextPage = () =>
{
	const router = useRouter();
	const [pageIndex, setPageIndex] = useState(1);
	const { data, error } = useSWR(`http://localhost:8000/images/?page=${pageIndex}`, fetcher)

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

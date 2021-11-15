import type {NextPage} from "next";
import {CenzoBox} from "../components";
import {GetServerSideProps} from "next";
import {api, fetcher} from "../utils";
import {useRouter} from "next/router";
import {Button, Box, Paper, CircularProgress} from "@mui/material";
import {Image as ImageType} from "../utils/typed";
import Error from "next/error";
import axios from "axios";
import React from "react";
import Image from "next/image";
import useSWR from "swr";

const RandomCenzo: NextPage = () => {
	const router = useRouter()

	const { data, mutate, error } = useSWR<ImageType>(`https://api.jebzpapy.tk/images/random/`, fetcher)

	if (error) return <div>failed to load</div>
	if (!data) return (
		<Box mt={1} mb={5} style={{textAlign: "center", alignItems: "center"}}>
			<CircularProgress />
		</Box>
	)
	const refreshData = () => mutate();


	return (
		<div>
			<Box mt={1} mb={5} style={{textAlign: "center", alignItems: "center"}}>
				<Paper style={{height: "100%" }} elevation={1}>
					<Image
						src={data.public_url ?? "/logo.png"}
						width={data.width}
						height={data.height}
						alt={"Cenzopapa"}
						onClick={() => router.push(`/cenzo/${data.id}`)}
					/>
				</Paper>
			</Box>
			<Box mt={1} mb={5} style={{textAlign: "center"}}>
				<Button
					variant="contained"
					size="large"
					onClick={(e) => refreshData()}>Losuj</Button>
			</Box>
		</div>

	)
}

export const getServerSideProps: GetServerSideProps = async (context) => {
	try {
		const api_url = process.env.API_URL ?? "https://api.jebzpapy.tk";
		const response = await axios.get(`${api_url}/aimages/random/`);
		console.log(response.headers);
		const data = await response.data;
		return {
			props: {
				image: data,
				error: null,
			}
		}
	} catch (e: any) {

		return {
			props: {
				image: null,
				error: e.message,
			},
		}
	}

}

export default RandomCenzo;
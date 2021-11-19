import type {NextPage} from "next";
import {API_URL, fetcher} from "../utils";
import {useRouter} from "next/router";
import {Button, Box, Paper, CircularProgress} from "@mui/material";
import {Image as ImageType} from "../utils/typed";
import React from "react";
import Image from "next/image";
import useSWR from "swr";

const RandomCenzo: NextPage = () => {
	const router = useRouter()

	const { data, mutate, error } = useSWR<ImageType>(`${API_URL}/images/random/`, fetcher)

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

export default RandomCenzo;
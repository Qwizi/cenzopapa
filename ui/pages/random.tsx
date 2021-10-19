import type {NextPage} from "next";
import {CenzoBox} from "../components";
import {GetServerSideProps} from "next";
import {api} from "../utils";
import {useRouter} from "next/router";
import {Button, Box, Paper} from "@mui/material";
import {Image as ImageType} from "../utils/typed";
import Error from "next/error";
import axios from "axios";
import ImageListItem from "@mui/material/ImageListItem";
import React from "react";
import Image from "next/image";
type Props = {
	image: ImageType,
	error: string | null
}

const RandomCenzo: NextPage<Props> = ({image}) => {
	const router = useRouter()
	const refreshData = () => router.replace(router.asPath);
	return (
		<div>
			<Box mt={1} mb={5} style={{textAlign: "center", alignItems: "center"}}>
				<Paper style={{height: "100%" }} elevation={1}>
					<Image
						src={image.public_url ?? "/logo.png"}
						width={image.width}
						height={image.height}
						alt={"Cenzopapa"}
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
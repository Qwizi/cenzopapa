import type {NextPage} from "next";
import {CenzoBox} from "../components";
import {GetServerSideProps} from "next";
import {api} from "../utils";
import {useRouter} from "next/router";
import {Button, Box} from "@mui/material";
import {Image} from "../utils/typed";
import Error from "next/error";
import axios from "axios";

type Props = {
	image: Image,
	error: string | null
}

const RandomCenzo: NextPage<Props> = ({image}) => {
	const router = useRouter()
	const refreshData = () => router.replace(router.asPath);
	return (
		<div>
			<CenzoBox public_url={image.public_url}/>
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
		const response = await axios.get(`${api_url}/images/random/`);
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
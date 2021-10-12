import type {NextPage} from "next";
import {CenzoBox} from "../components";
import {GetServerSideProps} from "next";
import {api} from "../utils";
import {useRouter} from "next/router";
import {Button, Box} from "@mui/material";

type Props = {
	image_data: object | null,
	error: string | null
}

const RandomCenzo: NextPage<Props> = ({image_data}) => {
	const router = useRouter()
	const refreshData = () => router.replace(router.asPath);

	return (
		<div>
			<CenzoBox public_url={image_data.public_url}/>
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
		const response = await api.get(`/images/random/`);
		const data = await response.data;
		return {
			props: {
				image_data: data,
				error: null,
			}
		}
	} catch (e: any) {

		return {
			props: {
				image_data: null,
				error: e.message,
			},
		}
	}

}

export default RandomCenzo;
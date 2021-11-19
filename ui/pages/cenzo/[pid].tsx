import {NextPage} from "next";
import useSWR from "swr";
import {useRouter} from "next/router";
import React from "react";
import {API_URL, fetcher} from "../../utils";
import {Box, CircularProgress, Paper} from "@mui/material";
import {Image as ImageType} from "../../utils/typed";
import Image from "next/image";

const CenzoDetail: NextPage = () =>
{
	const router = useRouter();
	const {pid} = router.query;
	const { data, error }  = useSWR<ImageType>(`${API_URL}/images/${pid}`, fetcher)


	if (error) return <div>failed to load</div>
	if (!data) return (
		<Box mt={1} mb={5} style={{textAlign: "center", alignItems: "center"}}>
			<CircularProgress />
		</Box>
	)



	return (
		<Box mt={1} mb={5} style={{textAlign: "center", alignItems: "center"}}>
			<Paper style={{height: "100%" }} elevation={1}>
				<Image
					src={data.public_url ?? "/logo.png"}
					width={data.width}
					height={data.height}
					alt={"Cenzopapa"}
				/>
			</Paper>
		</Box>
	)
}

export default CenzoDetail
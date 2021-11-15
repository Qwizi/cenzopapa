import {NextPage} from "next";
import useSWR from "swr";
import {useRouter} from "next/router";
import React, {useEffect, useState} from "react";
import {fetcher} from "../../utils";
import {CenzoListPage} from "../../components";
import {Box, CircularProgress, Paper, Skeleton} from "@mui/material";
import Image from "next/image";

const CenzoDetail: NextPage = () =>
{
	const router = useRouter();
	const [pageIndex, setPageIndex] = useState(1);
	const {pid} = router.query;
	const { data, error } = useSWR(`http://localhost:8000/images/${pid}`, fetcher)


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
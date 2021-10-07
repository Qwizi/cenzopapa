import useSWR from "swr";
import {Skeleton} from "@mui/material";
import React from "react";
import MyPagination from "./Pagination.component";
import {CenzoBox} from "./index";
import {fetcher} from '../utils';
// @ts-ignore



// @ts-ignore
const CenzoListPage = ({api_url, index, setPageIndex }) => {
	const {data, error} = useSWR(`${api_url}/images/?size=10&page=${index}`, fetcher)

	if (error) return <div>Failed load {api_url}</div>
	if (!data || !data.items) return <Skeleton variant="rectangular" width={600} height={400}/>
	return (
		<div>
			<MyPagination total={data.total} size={data.size} index={index} setPageIndex={setPageIndex}/>
			{data.items.map((img: any, i: number) =>
				<CenzoBox key={i} public_url={img.public_url} />
			)}
			<MyPagination total={data.total} size={data.size} index={index} setPageIndex={setPageIndex}/>
		</div>
	)
}



export default CenzoListPage;

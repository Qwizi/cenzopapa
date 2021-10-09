import useSWR from "swr";
import {Skeleton} from "@mui/material";
import React from "react";
import {CenzoBox, Error, MyPagination} from "./index";
import {fetcher} from '../utils';

type Props = {
	api_url: string,
	index: number,
	setPageIndex: any
}

const CenzoListPage: React.FunctionComponent<Props> = ({api_url, index, setPageIndex }) => {
	const {data, error} = useSWR(`${api_url}/images/?size=10&page=${index}`, fetcher)

	if (error) return <Error error_code={500} title={"Server error"} message={`Failed fetch ${api_url}`}/>
	if (!data || !data.items) return (
		<div>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
			<Skeleton variant="rectangular" width={800} height={400} style={{marginTop: "1px", marginBottom: "5px", padding: "15px"}}/>
		</div>

	)
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

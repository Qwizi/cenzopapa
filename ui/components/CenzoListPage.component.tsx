import {ImageList, Skeleton} from "@mui/material";
import dynamic from 'next/dynamic'
import React from "react";
import {Image, Data} from "../utils/typed";

const CenzoBox = dynamic(() => import('../components/CenzoBox.component'))
const MyPagination = dynamic(() => import('../components/Pagination.component'))

type Props = {
	error: string,
	data: Data,
	pageIndex: number,
	setPageIndex: any,
}

const CenzoListPage: React.FunctionComponent<Props> = ({data, pageIndex, setPageIndex}) => {
	return (
		<div>
			<MyPagination
				total={data.count}
				size={10}
				pageIndex={pageIndex}
				setPageIndex={setPageIndex}
			/>
			<ImageList
				sx={{ width: "100%", height: "auto" }}
				variant="quilted"
				cols={2}
			>
				{data.results.map((img: Image, i: number) =>
					<CenzoBox id={img.id} key={i} url={img.url} width={img.width} height={img.height} />
				)}
			</ImageList>
			<MyPagination
				total={data.count}
				size={10}
				pageIndex={pageIndex}
				setPageIndex={setPageIndex}
			/>
		</div>
	)
}



export default CenzoListPage;

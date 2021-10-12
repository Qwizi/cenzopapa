import {Skeleton} from "@mui/material";
import React from "react";
import {CenzoBox, Error, MyPagination} from "./index";
import {ImagesData, Image} from "../utils/typed";


type Props = {
	error: string | null,
	images_data: ImagesData | null,
	page: number,
	pageIndex: number,
	setPageIndex: any
}

const CenzoListPage: React.FunctionComponent<Props> = ({error , images_data, page, pageIndex, setPageIndex}) => {
	// @ts-ignore
	if (!images_data || !images_data.items) return (
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
			<MyPagination
				total={images_data.total}
				size={images_data.size}
				pageIndex={pageIndex}
				page={page}
				setPageIndex={setPageIndex}
			/>
			{images_data.items.map((img: Image, i: number) =>
				<CenzoBox key={i} public_url={img.public_url} />
			)}
			<MyPagination
				total={images_data.total}
				size={images_data.size}
				pageIndex={pageIndex}
				page={page}
				setPageIndex={setPageIndex}
			/>
		</div>
	)
}



export default CenzoListPage;

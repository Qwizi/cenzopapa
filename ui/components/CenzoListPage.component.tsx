import {ImageList, Skeleton} from "@mui/material";
import React from "react";
import {CenzoBox, Error, MyPagination} from "./index";
import {ImagesData, Image} from "../utils/typed";


type Props = {
	error: string,
	images_data: ImagesData[],
	page: number,
	pages_count: number,
	skip: number,
	pageIndex: number,
	setPageIndex: any,
}

const CenzoListPage: React.FunctionComponent<Props> = ({error , images_data, page, pages_count, skip, pageIndex, setPageIndex}) => {
	// @ts-ignore
	if (!images_data) return (
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
				total={pages_count}
				size={10}
				pageIndex={pageIndex}
				page={page}
				setPageIndex={setPageIndex}
			/>
			<ImageList
				sx={{ width: "100%", height: "auto" }}
				variant="quilted"
				cols={2}
			>
				{images_data.map((img: Image, i: number) =>
					<CenzoBox key={i} public_url={img.public_url} width={img.width} height={img.height} />
				)}
			</ImageList>
			<MyPagination
				total={pages_count}
				size={10}
				pageIndex={pageIndex}
				page={page}
				setPageIndex={setPageIndex}
			/>
		</div>
	)
}



export default CenzoListPage;

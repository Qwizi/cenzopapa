import {Box} from "@mui/material";
import Pagination from "@mui/material/Pagination";
import React, {useEffect, useState} from "react";
import {useRouter} from "next/router";

// @ts-ignore
const MyPagination = ({page, total, size, pageIndex, setPageIndex}) => {
	const router = useRouter();

	const handleChangePagination = (e: any, value: any) => {
		router.push({query: `page=${value}`})
		setPageIndex(value);
	}

	return (
		<Box mt={1} mb={5} style={{justifyContent: "center", display: "flex"}}>
			<Pagination count={(Math.round(total / size))} variant="outlined" defaultPage={page} shape="rounded" page={Number(pageIndex)} onChange={handleChangePagination}/>
		</Box>
	)
}

export default MyPagination;
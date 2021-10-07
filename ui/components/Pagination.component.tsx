import {Box} from "@mui/material";
import Pagination from "@mui/material/Pagination";
import React from "react";

// @ts-ignore
const MyPagination = ({index, total, size, setPageIndex}) => {
	return (
		<Box mt={1} mb={5} style={{justifyContent: "center", display: "flex"}}>
			<Pagination count={(Math.round(total / size))} variant="outlined" shape="rounded" page={index} onChange={(event, val) => setPageIndex(val)}/>
		</Box>
	)
}

export default MyPagination;
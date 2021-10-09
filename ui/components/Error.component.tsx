import {Box, Paper} from "@mui/material";
import Image from "next/image";
import React, {FunctionComponent} from "react";

type Props = {
	error_code: number,
	title: string,
	message: string
}


const Error: FunctionComponent<Props> = ({error_code, title, message}) => {
	return (
		<Box mt={1} mb={5} style={{textAlign: "center"}}>
			<Paper style={{padding: "15px"}} elevation={1}>
				<h1>{error_code} - {title}</h1>
				{message}
			</Paper>
		</Box>
	)
}
export default Error;
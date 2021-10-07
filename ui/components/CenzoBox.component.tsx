import {Box, Paper} from "@mui/material";
import Image from "next/image";
import React from "react";

// @ts-ignore
const CenzoBox = ({public_url}) => {
	return (
		<Box mt={1} mb={5} style={{textAlign: "center"}}>
			<Paper style={{padding: "15px"}} elevation={1}>
				<Image
					src={public_url}
					width={600}
					height={400}
				/>
			</Paper>
		</Box>
	)
}

export default CenzoBox;
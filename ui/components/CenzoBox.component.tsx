import {Box, Paper} from "@mui/material";
import Image from "next/image";
import Link from "next/link";
import React from "react";
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
type Props = {
	public_url: string,
	height: number
	width: number,
}

const CenzoBox: React.FunctionComponent<Props> = ({public_url, height, width}) => {
	return (
		<Box mt={1} mb={5} style={{textAlign: "center", alignItems: "center"}}>
			<Paper style={{padding: "15px", width: "100%", height: "100%"}} elevation={1}>
					{/*<Image
						src={public_url ?? "/logo.png"}
						width={width}
						height={height}
						alt={"Cenzopapa"}
					/>*/}
					<ImageListItem cols={1} rows={1}>
						<Image
							src={public_url ?? "/logo.png"}
							width={width}
							height={height}
							alt={"Cenzopapa"}
							loading={"lazy"}
						/>
					</ImageListItem>
			</Paper>
		</Box>
	)
}

export default CenzoBox;
import {Box, Paper} from "@mui/material";
import Image from "next/image";
import React from "react";
import ImageListItem from '@mui/material/ImageListItem';
import {useRouter} from "next/router";
type Props = {
	id: number,
	public_url: string,
	height: number
	width: number,
}

const CenzoBox: React.FunctionComponent<Props> = ({id, public_url, height, width}) => {
	const router = useRouter();
	return (
		<Box mt={1} mb={5} style={{textAlign: "center", alignItems: "center"}}>
			<Paper style={{padding: "15px", width: "100%", height: "100%"}} elevation={1}>
					<ImageListItem cols={1} rows={1}>
						<Image
							src={public_url ?? "/logo.png"}
							width={width}
							height={height}
							alt={"Cenzopapa"}
							loading={"lazy"}
							onClick={() => router.push(`/cenzo/${id}`)}
						/>
					</ImageListItem>
			</Paper>
		</Box>
	)
}

export default CenzoBox;
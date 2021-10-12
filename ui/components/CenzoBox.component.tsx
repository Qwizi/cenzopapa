import {Box, Paper} from "@mui/material";
import Image from "next/image";
import Link from "next/link";
import React from "react";

type Props = {
	public_url: string
}

const CenzoBox: React.FunctionComponent<Props> = ({public_url}) => {
	return (
		<Box mt={1} mb={5} style={{textAlign: "center"}}>
			<Paper style={{padding: "15px"}} elevation={1}>
				<Link href={public_url} passHref={true}>
					<Image
						src={public_url ?? "/logo.png"}
						width={600}
						height={400}
						alt={"Cenzopapa"}
					/>
				</Link>
			</Paper>
		</Box>
	)
}

export default CenzoBox;
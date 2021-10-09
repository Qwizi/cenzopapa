import type {NextPage} from "next";
import {CenzoBox} from "../components";

const RandomCenzo: NextPage = () => {
	return (
		<CenzoBox public_url={"/logo.png"}/>
	)
}

export default RandomCenzo;
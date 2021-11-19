import {useEffect} from "react";
import {API_URL} from "../utils";

const ApiDetail = () => {

	useEffect(() => {
		window.location.assign(`${API_URL}`)
	})
	return(
		<>
		</>
	)
}

export default ApiDetail
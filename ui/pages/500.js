import Error from "../components/Error.component";

export default function Custom500() {
	return <Error message={"Internal Server Error"}  error_code={500} title={"Server error"}/>
}
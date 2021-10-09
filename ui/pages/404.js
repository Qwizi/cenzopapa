import Link from 'next/link'
import Error from "../components/Error.component";

export default function FourOhFour() {
    return <>
        <Error error_code={404} title={"Not found"} message={"Page not found"}/>
    </>
}
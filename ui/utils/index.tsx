// @ts-ignore
import axios from "axios";

const fetcher = (url: string) => axios.get(url).then(res => res.data)

const API_URL = process.env.NEXT_PUBLIC_API_URL
export {fetcher, API_URL}
// @ts-ignore
import axios from "axios";

const fetcher = (url: string) => axios.get(url).then(res => res.data)
const api = axios.create({
	baseURL: process.env.API_URL
})
export {fetcher, api}
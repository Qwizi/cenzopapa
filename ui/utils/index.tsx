// @ts-ignore
import axios from "axios";

// @ts-ignore
const fetcher = (...args: any[]) => fetch(...args).then(res => res.json())

const api = axios.create({
	baseURL: process.env.API_URL
})
export {fetcher, api}
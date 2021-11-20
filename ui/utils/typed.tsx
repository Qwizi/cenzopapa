type Image = {
	id: number,
	url: string,
	posted_at: string,
	height: number,
	width: number
}
type Data = {
	count: number,
	next: string | null,
	previous: string | null,
	results: Image[]
}

type CountData = {
	count: number
}

export type {Image, Data, CountData}
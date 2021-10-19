type Image = {
	id: number,
	filename: string,
	extension: string,
	remote_image_url: string,
	public_url: string,
	created_at: string,
	height: number,
	width: number
}

type ImagesData = {
	id: number,
	filename: string,
	extension: string,
	remote_image_url: string,
	public_url: string,
	created_at: string,
	height: number,
	width: number
}

type CountData = {
	count: number
}

export type {Image, ImagesData, CountData}
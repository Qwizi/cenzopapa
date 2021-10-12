type Image = {
	id: number,
	public_url: string
}

type ImagesData = {
	size: number,
	page: number,
	total: number,
	items: Image[],
}

export type {Image, ImagesData}
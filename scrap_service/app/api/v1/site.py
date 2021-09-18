from abc import abstractmethod, ABC


class Site(ABC):
    site_name: str
    site_url: str
    session: any

    def run(self):
        images = self.scrap_images(initial_scrap=True)
        return images

    @abstractmethod
    def scrap_images(self, initial_scrap=False):
        pass
import httpx

from .wykop import Wykop


class SiteManager:
    sites = []

    def add_site(self, site_class):
        site_class.session = httpx.Client()
        self.sites.append({
            'site_name': site_class.site_name,
            'site_class': site_class
        })

    def get_site(self, site_name):
        for site in self.sites:
            if site['site_name'] == site_name:
                return site['site_class']
        return None

    def get_sites(self):
        return self.sites

    def get_scrap_images(self):
        scrap_images = []
        for site in self.sites:
            images = site['site_class'].run()
            scrap_images.append(images)

        print(scrap_images)
        return scrap_images


site_manager = SiteManager()
site_manager.add_site(Wykop())

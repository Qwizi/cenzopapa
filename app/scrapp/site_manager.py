import requests

from app.scrapp.site import Wykop


class SiteManager:
    sites = []

    def add_site(self, site_class):
        site_class.session = requests.Session()
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


site_manager = SiteManager()
site_manager.add_site(Wykop())

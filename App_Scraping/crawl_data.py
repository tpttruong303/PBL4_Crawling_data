import requests
from bs4 import BeautifulSoup
import exc_data

class Spider:

    def __init__(self, url, recent_db):
        self.main_url = f"https://{url.split('/')[2]}"
        self.db_exc = recent_db
        
    def parse(self, url):
        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            job_links = [self.main_url+link['href'] for link in exc_data.get_links(soup)]
            return job_links
        else:
            return 'Error'

    def parse_job(self, job_url):
        res = requests.get(job_url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            detail_job = exc_data.get_detail(soup)
            if detail_job != None:
                self.db_exc.add_job(exc_data.get_detail(soup), job_url)
        

            

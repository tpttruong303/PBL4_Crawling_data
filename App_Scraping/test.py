import requests
from bs4 import BeautifulSoup
import exc_data

url = 'https://www.careerlink.vn/tim-viec-lam/nhan-vien-marketing/2742914?campaign=vDYbX1FdhXPDcrnm&medium=cl_top&source=site'
res = requests.get(url)

if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    raw_careers = exc_data.get_describe(soup)['Ngành nghề']
    careers = raw_careers.replace(',', '/')
    print(careers)
from bs4 import BeautifulSoup

def get_links(soup):
    links = soup.find_all('a', class_ = 'job-link clickable-outside')
    return links

def get_title(soup):
    title = soup.find('h1', class_ = 'job-title mb-0').get_text(' ', strip=True)
    return title

def get_company(soup):
    com = soup.select('div p a')[0].find('span').get_text(' ', strip=True)
    return com

def get_salary(soup):
    sal = soup.find_all('div', class_ = 'd-flex align-items-center mb-2')[0].find('span').get_text(' ', strip = True)
    return sal

def get_experience(soup):
    exp = soup.find_all('div', class_ = 'd-flex align-items-center mb-2')[1].find('span').get_text(' ', strip = True)
    return exp

def get_posting_date(soup):
    date = soup.find('span', class_ = 'd-flex').get_text(' ', strip = True).split(' ')[-1]
    return date

def get_deadline(soup):
    dl = soup.find('div', class_ = 'day-expired d-flex align-items-center').get_text(' ', strip = True).split(':')[-1].split()
    date = ''
    for c in dl:
        date += c + ' '
    return date.strip()

def get_describe(soup):
    labels = soup.find_all('div', class_ = 'my-0 summary-label')
    details = soup.find_all('div', class_ = 'font-weight-bolder')
    ds = {}
    for i in range(len(labels)):
        lb = labels[i].get_text(' ',strip = True)
        dt = details[i].get_text(' ',strip = True)
        ds[lb] = dt
    return ds

def get_contact(soup):
    lis = soup.find_all('li', class_ = 'd-flex align-items-start')
    ct = {}
    for li in lis:
        icon = li.select_one('i')
        label = (icon['class'][0].split('cli-')[1])
        text = li.get_text(' ', strip = True)
        ct[label] = text
    return ct

def get_language(soup):
    lan = soup.find('div', class_ = 'pt-3 job-expire rounded-lg').get_text(' ', strip = True).split(':')[-1]
    return lan.strip()

def get_description(soup):
    jd = soup.find('div', id = 'section-job-description').find('div', class_ = 'rich-text-content').get_text(' ', strip = True)
    return jd

def get_skills(soup):
    skills = soup.find('div', id = 'section-job-skills').find('div', class_ = 'raw-content rich-text-content').get_text(' ', strip = True)
    return skills

def get_benefits(soup):
    benefits_div = soup.find('div', id = 'section-job-benefits')
    if benefits_div is None:
        return 'None'
    else:
        benefits_text = ''
        benefits_sub_divs = benefits_div.find_all('div', class_ = 'job-benefit-item d-flex align-items-start mb-2')
        for div in benefits_sub_divs:
            benefits_text += '-' + div.get_text(' ', strip = True)
        return benefits_text

def get_image(soup):
    img = soup.find('img', class_ = 'company-img img-thumbnail p-0 bg-white border-0')['src']
    return img

def exctract_career(raw_careers):
    careers = raw_careers.replace(',', '/')
    return careers

def get_detail(soup):
    detail = {
        'Title': get_title(soup),
        'Image': get_image(soup),
        'Company': get_company(soup),
        'Posting_date': get_posting_date(soup),
        'Deadline': get_deadline(soup),
        'Salary': get_salary(soup),
        'YOE': get_experience(soup),
        'Type': 'None',
        'Level': 'None',
        'Education': 'None',
        'Sex': 'None',
        'Career': 'None',
        'Age': 'None',
        'ID_Job': 'None',
        'Contact_with': 'None',
        'Location': 'None',
        'Note': 'None',
        'Phone_number': 'None',
        'Email': 'None',
        'Language': get_language(soup),
        'Describe_job': get_description(soup),
        'Benefits': get_benefits(soup),
        'Skills': get_skills(soup),
    }
    for key, val in get_describe(soup).items():
        if 'Loại công việc' in key:
            detail['Type'] = val
        elif 'Cấp bậc' in key:
            detail['Level'] = val
        elif 'Học vấn' in key:
            detail['Education'] = val
        elif 'Giới tính' in key:
            detail['Sex'] = val
        elif 'Ngành nghề' in key:
            detail['Career'] = exctract_career(val)
        elif 'Tuổi' in key:
            detail['Age'] = val
        elif 'Mã việc làm' in key:
            detail['ID_Job'] = val
    for key, val in get_contact(soup).items():
        if 'contact-with' in key:
            detail['Contact_with'] = val
        elif 'location' in key:
            detail['Location'] = val
        elif 'note' in key:
            detail['Note'] = val
        elif 'phone' in key:
            detail['Phone_number'] = val
        elif 'mail' in key:
            detail['Email'] = val
    return detail

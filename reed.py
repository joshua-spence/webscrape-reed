import requests
from bs4 import BeautifulSoup
from csv import writer

pages = range(1,5)

def reed(jb,lc):
    for page in pages:

        URL = 'https://www.reed.co.uk/jobs/' + jb + '-jobs-in-'+ lc + '?pageno='+ str(page)
        page = requests.get(URL)


        soup = BeautifulSoup(page.content, 'html.parser')

        # job = soup.find(class_ = 'title')
        # company = soup.find(class_ = 'gtmJobListingPostedBy') 
        # location = soup.find(class_ = 'location')

        results = soup.find('section', id= 'server-results')

        job_containers = results.find_all('article', class_='job-result')


        for job_elem in job_containers:

            title = job_elem.find('h3', class_='title')
            company =  job_elem.find('a', class_='gtmJobListingPostedBy')
            location = job_elem.find('li', class_='location')
            remove_loc = location.span 
            remove_loc.decompose()

            print(title.text.strip())
            print(company.text)
            print(location.text.strip())
            print()








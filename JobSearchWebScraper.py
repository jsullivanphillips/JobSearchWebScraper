import requests
from bs4 import BeautifulSoup
import re

substrings_to_search = ['junior developer', 'entry level', 'junior programmer', 'junior software engineer', 'junior software developer', 'junior web developer', 'junior software', 'junior programmer', 'junior software developer', 'junior software engineer']

url_list = [
    "https://members.viatec.ca/job-board",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=1&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=2&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=3&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=4&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=5&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=6&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=7&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=8&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=9&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=10&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=11&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://www.bctechjobs.ca/search-jobs?q=developer&location=#page=12&q=developer&location=&range=0&freshness=0&categoryIds=&employerTypeIds=&positionTypeIds=&memberStatusIds=&careerLevelIds=&featuredEmployersOnly=false&trainingPositionsOnly=false",
    "https://ca.indeed.com/q-junior-developer-l-victoria,-bc-jobs.html?from=relatedQueries&saIdx=2&rqf=1&parentQnorm=developer+intern&vjk=d78185945bc107ab",
    "https://ca.indeed.com/jobs?q=junior+developer&l=victoria%2C+bc&rqf=1&start=10&vjk=1a8940ea86c1202c",
    "https://ca.indeed.com/jobs?q=junior+developer&l=victoria%2C+bc&radius=50&rqf=1&start=20&vjk=6ad1b74144602094",
    "https://jobs.techtalent.ca/",
    "https://jobs.techtalent.ca/?p=2",
    "https://jobs.techtalent.ca/?p=3",
    "https://jobs.techtalent.ca/?p=4",
    "https://jobs.techtalent.ca/?p=5",
    "https://jobs.techtalent.ca/?p=6",
    "https://jobs.techtalent.ca/?p=7"
]

def job_postings_on_web():
    result = {}

    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all text in the page
        text = soup.get_text()

        # Use a regular expression to find multiple substrings in the text
        for substring in substrings_to_search:
            count = len(re.findall(substring, text, re.IGNORECASE))
            result[substring] = result.get(substring, 0) + count
            if(count > 0):
                print(substring + ": " + str(count) + " matches" + " on " + url)    

    return result

job_postings_on_web()
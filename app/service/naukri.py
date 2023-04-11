import requests
import json
from config import naukri_cookies

def fetch_naukri_job(number_of_result=100, search_keyword='', search_keyword_hyphen='', page_number=1, location=''):

    url = f"https://www.naukri.com/jobapi/v3/search?noOfResults={number_of_result}&l={location}&urlType=search_by_keyword&searchType=adv&location={location}&keyword={search_keyword}&pageNo={page_number}&k={search_keyword}&seoKey={search_keyword_hyphen}-jobs-in-{location}&src=jobsearchDesk"

    print(url)

    headers = {
      'authority': 'www.naukri.com',
      'accept': 'application/json',
      'accept-language': 'en-GB,en;q=0.7',
      'appid': '109',
      'cache-control': 'no-cache',
      'clientid': 'd3skt0p',
      'content-type': 'application/json',
      'cookie': naukri_cookies,
      'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
      'referer': f'https://www.naukri.com/{search_keyword_hyphen}-jobs-{location}?k={search_keyword}&l={location}',
      'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'sec-gpc': '1',
      'systemid': '109',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code != 200:
        print(response.text)
        return response.json()

    return [
        {
            'Title': i['title'],
            'JobID': i['jobId'],
            'Currency': i['currency'],
            'Company Logo': i.get('logoPath', ''),
            'Company Name': i['companyName'],
            'Skills': i['tagsAndSkills'],
            'Placeholders': i['placeholders'],
            'Company ID': i['companyId'],
            'Link': f"https://www.naukri.com{i['jdURL']}",
            'Review Count': i.get('ReviewsCount', 0),
            'Aggregate Rating': i.get('AggregateRating'),
            'job Description': i['jobDescription'],
            'created Date': i['createdDate']

        } 
        for i in response.json()['jobDetails']
    ]

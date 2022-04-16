import requests
from bs4 import BeautifulSoup

url = 'https://www.classcentral.com/search?q='

# Take user input and append to url
query = input('Enter a search query: ')
query = query.replace(' ', '+')
url = url + query


def get_courses(url_query):
    r = requests.get(url_query)

    soup = BeautifulSoup(r.text, 'html.parser')
    soup.prettify()

    # Find all of the courses
    courses = soup.find_all('div', class_='catalog-grid__results')
    # If the query returns no results, return None
    if len(courses) == 0:
        print("Courses not found")

    # Find all of the titles
    titles = soup.find_all(
        'h2', class_='text-1 weight-semi line-tight margin-bottom-xxsmall')

    # Find all of the links
    link = 'https://www.classcentral.com'
    courses = soup.find_all('a', class_='color-charcoal course-name')

    # Print out the titles and links
    for i in range(len(titles)):
        print(titles[i].text)
        print(link + courses[i].get('href'))
        print('\n')


get_courses(url)

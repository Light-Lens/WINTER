import requests
from bs4 import BeautifulSoup

# Set the search query
query = ['what is the current time', 'what is the capital of india', "today's weather", "today's temperature"]

def s(i):
    # Perform the search and retrieve the search results page
    response = requests.get(f'https://www.google.com/search?q={i}')

    # Parse the HTML of the search results page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the info box element on the page
    info_box = soup.find('div', class_='BNeawe iBp4i AP7Wnd')

    return info_box.text if info_box else ""

# Extract the info box information
for i in query:
    print(s(i))

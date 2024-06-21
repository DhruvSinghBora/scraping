from bs4 import BeautifulSoup
import requests

# URL of the website you want to scrape
url = 'https://' + input("ENTER WEBSITE")

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
with open('out2.txt', 'w') as s:
  s.write(f"{soup}")
#print(soup)
# Example: Extract all the headings (h1 tags) from the HTML
headings = soup.find_all('h1')

# Print the text of each heading
for heading in headings:
    print(heading.text.strip())
    with open('output.txt', 'w') as f:
      f.write(f"{heading}\n")

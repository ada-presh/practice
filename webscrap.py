# import requests
# from bs4 import BeautifulSoup
# # url = "https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html"
# ##download the entire html document
# # page = requests.get(url)
# ##parse the content using beautifulsoup
# # soup = BeautifulSoup(page.content, 'html.parser')
# ##print the parsed website content
# # print(soup.prettify())
# ##find all paragraph
# # paragraphs_first_id = soup.find_all(id="first")
# # print(paragraphs_first_id)
# # paragraphs_second_id = soup.find(id="second")
# # print(paragraphs_second_id)


# # all_paragraphs_with_inner_text_class = soup.find_all("p", class_="inner-text")
# # print(all_paragraphs_with_inner_text_class)



# import requests
# from bs4 import BeautifulSoup
# url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
# ##download the entire html document
# page = requests.get(url)
# ##parse the content using beautifulsoup
# soup = BeautifulSoup(page.content, 'html.parser')
# ##print the parsed website content
# seven_day_container = soup.find("div", id="seven-day-forecast-container")

# list_containers = seven_day_container.find_all("div", class_="tombstone-container")
# print(list_containers)


##assignment
##extract the name , price and availability
# import requests
# from bs4 import BeautifulSoup

# # Target URL
# url = "https://books.toscrape.com/"

# # Send GET request
# response = requests.get(url)

# # Parse HTML
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all books on the page
# books = soup.find_all('article', class_='product_pod')

# # Extract data
# for book in books:
#     # Get book title
#     name = book.h3.a['title']
    
#     # Get price
#     price = book.find('p', class_='price_color').text
    
#     # Get availability
#     availability = book.find('p', class_='instock availability').text.strip()
    
#     print(f"Name: {name}")
#     print(f"Price: {price}")
#     print(f"Availability: {availability}")
#     print("-" * 40)


# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# # 1. Get and parse HTML content
# def get_html_content(url):
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise Exception(f"Failed to retrieve page: {response.status_code}")
#     return BeautifulSoup(response.content, 'html.parser')

# # 2. Extract article title
# def extract_title(soup):
#     return soup.find('h1', id='firstHeading').text.strip()

# # 3. Extract article text with headings
# def extract_text_with_headings(soup):
#     content_div = soup.find('div', class_='mw-parser-output')
#     text_data = {}
#     current_heading = None

#     for tag in content_div.find_all(['h2', 'h3', 'p']):
#         if tag.name in ['h2', 'h3']:
#             heading = tag.text.replace('[edit]', '').strip()
#             current_heading = heading
#             text_data[current_heading] = []
#         elif tag.name == 'p':
#             if current_heading:
#                 text_data[current_heading].append(tag.text.strip())
#             else:
#                 text_data.setdefault('Introduction', []).append(tag.text.strip())

#     # Convert lists of paragraphs into a single string
#     for key in text_data:
#         text_data[key] = '\n'.join(text_data[key])
#     return text_data

# # 4. Extract internal Wikipedia links
# def extract_internal_links(soup):
#     base_url = "https://en.wikipedia.org"
#     links = set()
#     for a_tag in soup.find_all('a', href=True):
#         href = a_tag['href']
#         if href.startswith('/wiki/') and ':' not in href:
#             full_url = urljoin(base_url, href)
#             links.add(full_url)
#     return list(links)

# # 5. Wrapper function
# def scrape_wikipedia_page(url):
#     soup = get_html_content(url)
#     title = extract_title(soup)
#     text_sections = extract_text_with_headings(soup)
#     internal_links = extract_internal_links(soup)

#     return {
#         'title': title,
#         'text_sections': text_sections,
#         'internal_links': internal_links
#     }

# # 6. Test the function on a sample Wikipedia page
# if __name__ == "__main__":
#     test_url = "https://en.wikipedia.org/wiki/Web_scraping"
#     data = scrape_wikipedia_page(test_url)

#     print(f"Title: {data['title']}\n")
#     print("Sections and Paragraphs:")
#     for section, text in data['text_sections'].items():
#         print(f"\n== {section} ==\n{text[:300]}...")  # Show only first 300 characters

#     print(f"\nNumber of Internal Links Found: {len(data['internal_links'])}")
#     print("Sample Links:", data['internal_links'][:5])

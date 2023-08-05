from bs4 import BeautifulSoup
import requests
travel_date=input("Which year do you want travel to?(Please insert in format yyyy-month-day): ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + travel_date)


website_html=response.text
print(website_html)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

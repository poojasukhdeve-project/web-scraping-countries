import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

countries = soup.find_all("div", class_="country")

data = []

for country in countries:
    name = country.find("h3").text.strip()
    capital = country.find("span", class_="country-capital").text.strip()
    population = country.find("span", class_="country-population").text.strip()
    area = country.find("span", class_="country-area").text.strip()

    data.append([name, capital, population, area])

# Save to CSV
with open("countries.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Capital", "Population", "Area"])
    writer.writerows(data)

print("✅ Data saved to countries.csv")
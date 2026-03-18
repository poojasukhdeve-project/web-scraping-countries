from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

# Open CSV file
with open("quotes_all_pages.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    # Loop through pages 1 to 10
    for page in range(1, 11):
        url = f"https://quotes.toscrape.com/js/page/{page}/"
        driver.get(url)

        time.sleep(3)  # wait for page load

        quotes = driver.find_elements(By.CLASS_NAME, "text")
        authors = driver.find_elements(By.CLASS_NAME, "author")

        for q, a in zip(quotes, authors):
            writer.writerow([q.text, a.text])

        print(f"Page {page} scraped")

driver.quit()

print("All data saved to quotes_all_pages.csv")
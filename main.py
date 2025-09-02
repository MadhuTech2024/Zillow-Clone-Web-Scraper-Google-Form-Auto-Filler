# Tested with:
# beautifulsoup4==4.12.2
# requests==2.31.0
# selenium==4.15.1

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------- Part 1: Scraping ----------
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

# Links
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
base_url = "https://appbrewery.github.io"
all_links = [link["href"] if link["href"].startswith("http") else f"{base_url}{link['href']}" for link in all_link_elements]

# Addresses
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]

# Prices
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]

print("✅ Scraping complete!")
print(f"Found {len(all_links)} listings")

# ---------- Part 2: Filling Google Form ----------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

FORM_URL = "YOUR_GOOGLE_FORM_LINK_HERE"  # <-- Replace with your Google Form link

for n in range(len(all_links)):
    try:
        driver.get(FORM_URL)

        # Wait until form fields load
        form_fields = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
        )

        # Fill in fields
        form_fields[0].send_keys(all_addresses[n])
        form_fields[1].send_keys(all_prices[n])
        form_fields[2].send_keys(all_links[n])

        # Click Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
        submit_button.click()

        print(f"✅ Submitted form for listing {n+1}/{len(all_links)}")

    except Exception as e:
        print(f"❌ Error submitting listing {n+1}: {e}")
        continue

print("🎉 All listings processed!")

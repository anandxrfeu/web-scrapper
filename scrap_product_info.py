from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(options=Options())
driver.get("https://www.sephora.pt/maquilhagem-em-desconto/?listview=true&srule=PT_STOCK_MOST-VIEWED-PRODUCTS")
driver.find_element(By.CSS_SELECTOR, "#footer_tc_privacy_button_2").click
# data = driver.find_element(By.CSS_SELECTOR, "#search-result-items").text

data = driver.find_elements(By.CSS_SELECTOR, ".grid-tile")

for ele in data:
    print(ele.text)
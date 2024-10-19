from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# opens browser and site in question
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# local variables
continue_click = True
end_time = 300
store_items = {}
pause = 15

# clicker elements
clicker = driver.find_element(By.ID, value="cookie")
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
cookies_per_sec = driver.find_element(By.ID, value="cps")
item_ids = [item.get_attribute("id") for item in items]
for i in range(len(items)-1):
    price = items[i].find_element(By.CSS_SELECTOR, value="b")
    cost = int(((price.text).split("-")[-1].strip()).replace(",", ""))
    store_items[i] = {
        "id": item_ids[i],
        "cost": cost
    }


def check_store():
    for i in reversed(store_items):
        prix = store_items[i]["cost"]
        id_name = store_items[i]["id"]
        to_click = driver.find_element(by=By.ID, value=id_name)
        money = int((driver.find_element(By.CSS_SELECTOR,
                    value="#money").text).replace(",", ""))
        if money >= prix:
            try:
                to_click.click()
            except:
                pass
        else:
            pass


# time
START = time.time()
before = START
after = 0
time_difference = 0
start_end_diff = 0

# main
while continue_click:
    clicker.click()
    after = time.time()
    time_difference = after - before
    if time_difference >= pause:
        before = time.time()
        check_store()

    start_end_diff = after - START
    if start_end_diff >= end_time:
        print(cookies_per_sec.text)
        continue_click = False


# AFTER 5 MINUTES

# this code is based on original work by @jasonwbarnett.
# https://github.com/pyro2927/SouthwestCheckin/issues/70#issuecomment-921166994

import json
import time
import re
import sys
from pathlib import Path
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

confirmation_number = sys.argv[1]
first_name = sys.argv[2]
last_name = sys.argv[3]
output_dir = sys.argv[4]

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36')

driver = webdriver.Chrome(options=chrome_options)
driver.scopes = [ "page\/check-in" ]    # only capture request URLs matching this regex

driver.get("https://mobile.southwest.com/check-in")

# fill out the form once the form fields become available
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "recordLocator")))
element.send_keys(confirmation_number)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(last_name)

element.submit()

# give the form time to submit before checking headers
time.sleep(10)

southwest_headers = { "content-type": "application/json" }
headers = driver.requests[0].headers
for key in headers:
    if re.match("x-api-key|x-user-experience-id|x-channel-id|^\w+?-\w$", key, re.I):
        # only keep the headers we need
        southwest_headers[key] = headers[key]

# save headers
with open(output_dir + "/southwest_headers.json", "w") as json_file:
    json.dump(southwest_headers, json_file)

driver.quit()

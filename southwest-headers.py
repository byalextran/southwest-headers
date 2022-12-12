# this code is based on original work by @jasonwbarnett.
# https://github.com/pyro2927/SouthwestCheckin/issues/70#issuecomment-921166994

import json
import time
import re
import os
import random
import string
import sys
import seleniumwire.undetected_chromedriver.v2 as uc
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

confirmation_number = ''.join(random.choices(string.ascii_uppercase, k=6))
first_name = ''.join(random.choices(string.ascii_lowercase, k=random.randrange(4,10))).capitalize()
last_name = ''.join(random.choices(string.ascii_lowercase, k=random.randrange(4,10))).capitalize()
output_file = sys.argv[1] if len(sys.argv) > 1 else "southwest_headers.json"

driver = uc.Chrome(headless = True)
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

# content-type is a required header but not included in the request headers so we'll manually add it here.
southwest_headers = { "content-type": "application/json" }

headers = driver.requests[0].headers
for key in headers:
    # southwest_headers[key] = headers[key]

    if re.match("x-api-key|x-user-experience-id|x-channel-id|^[\w]+?-\w{1,2}$", key, re.I):
        # only keep the headers we need
        southwest_headers[key] = headers[key]

# save headers
with open(output_file, "w") as json_file:
    json.dump(southwest_headers, json_file)

driver.quit()

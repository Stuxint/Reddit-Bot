#--------------MADE BOT WHICH POSTS 4 ME!!!!!!!----------------------------------


import undetected_chromedriver as uc
from humancursor import WebCursor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import google.generativeai as genai
import time

prompt = """
Generate short paragraph about whether or not AI should be banned in school. Make it short and informative, and end w/ a question, on whether the user thinks if AI should be banend in school.
P.S: JUST GIVE ME THE TEXT, NOTHING ELSE!!!!!!!!!!!!!!!!
"""

web = uc.Chrome()
web.get("https://mail.google.com/mail/u/0/#sent")

genai.configure(api_key="your api key")
model = genai.GenerativeModel('gemini-2.0-flash')

#SIGN IN PART
usern = web.find_element('xpath', '//*[@id="identifierId"]')
usern.send_keys('your gmail address')
usern.send_keys(Keys.ENTER)

passw= WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
passw.send_keys('your password')
passw.send_keys(Keys.ENTER)

time.sleep(3)
web.get("https://www.reddit.com/r/ArtificialInteligence/")

#COMMENTING PART
create= WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="subgrid-container"]/div[1]/section/div/div[2]/span/create-post-entry-point-wrapper/faceplate-tracker/a/span'))
            )
create.click()


actions = ActionChains(web)

for x in range(17):
    actions.send_keys(Keys.TAB).perform()
actions.send_keys('Post 4 Today').perform()

answer = model.generate_content([prompt], stream=False)
response = answer.text.strip()

time.sleep(1)

for x in range(2):
    actions.send_keys(Keys.TAB).perform()
actions.send_keys(f'{response}').perform()

time.sleep(1)
actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
actions.send_keys(Keys.ENTER).perform()

time.sleep(1)
for x in range(6):
    actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.SPACE).perform()

time.sleep(1)
for x in range(7):
    actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.ENTER).perform()

for x in range(5):
    actions.send_keys(Keys.TAB).perform()

actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()

time.sleep(20)
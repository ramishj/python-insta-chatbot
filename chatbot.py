import sys
sys.path.append(
    '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time



def generate_chat_reply(message):
    url = "https://api.openai.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "": message}],
        "max_tokens": 5000
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": #OpenAI API key
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        return "Sorry, I couldn't generate a reply at the moment."


geckodriver_path = "geckodriver"
os.environ["PATH"] += os.pathsep + os.getcwd()
# Instagram automation code
driver = webdriver.Firefox()
# Log in to Instagram
driver.get("https://www.instagram.com/")
time.sleep(2)  # Give the page time to load

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("my usrname")
password.send_keys("Pass")

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Example reply automation
time.sleep(5)  # Wait for the Instagram homepage to load

# Find the message input element and send a message
message_input = driver.find_element_by_xpath(
    "//textarea[@placeholder='Message...']")
message_input.send_keys("Hello, how are you?")
message_input.send_keys(Keys.RETURN)

# Wait for the reply to be generated by ChatGPT API
time.sleep(2)

# Get the generated reply from ChatGPT API
generated_reply = generate_chat_reply("Hello, how are you?")
print(generated_reply)


# Send the generated reply as a message
message_input.send_keys(generated_reply)
message_input.send_keys(Keys.RETURN)

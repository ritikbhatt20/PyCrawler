import time
import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
# print(questions[0].get("id", 0))
for question in questions:
    print(question.select_one(".s-post-summary--content-title").get_text())
    print(question.select_one(".s-post-summary--stats-item-number").get_text())
    time.sleep(5)
    

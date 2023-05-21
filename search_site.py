# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By

querry = "Oracle+ORA-01805"
# service = Service(executable_path="geckodriver")
# driver = webdriver.Firefox(service=service)


def get_search(querry):
    # headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}
    # url_search = f"https://support.waters.com/Special:Search?query={querry}&type=wiki"
    # driver.get(url_search)
    # # soup = BeautifulSoup(r.text, 'html.parser')
    # # elements = driver.find_elements(By.TAG_NAME, "href")
    # print(driver.page_source)
    # # result = soup.find_all("a", {'class': "go result-spacer mt-tracked-result"})
    # # print(r.text)

    answers = ["answer_1", "answer_2", "answer_3", "answer_4", "answer_5"]

    return answers

from rabota_parser_loggin import Logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def open_jobs_list(query):
    """Initiates driver and opens jobs list"""
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    driver.get("https://rabota.ua")
    box = driver.wait.until(EC.presence_of_element_located(
        (By.ID, "ctl00_content_vacSearch_Keyword")))
    button = driver.wait.until(EC.element_to_be_clickable(
        (By.ID, "ctl00_content_vacSearch_lnkSearch")))

    box.send_keys(query)
    button.click()

    return driver

def count_pages(driver):
    pages = driver.find_elements_by_id("ctl00_content_vacancyList_gridList_ctl23_pagerInnerTable")
    pages_list = []
    for page_item in pages:
        pages_list = page_item.find_elements_by_class_name("f-always-blue")
        number_of_pages = len(pages_list)

    return number_of_pages

def parser(query):

    jobs_attributes = {'name': 'f-vacancylist-vacancytitle',
                        'city': 'f-vacancylist-characs-block',
                        'description': 'f-vacancylist-shortdescr'}

    driver = open_jobs_list(query)
    number_of_pages = count_pages(driver)

    job_info = {}
    page_counter = 3
    for i in range(number_of_pages):

        jobs =  driver.find_elements_by_class_name("f-vacancylist-vacancyblock")

        jobs_list = []
        for job in jobs:
            jobs_list.append(job)

        for job in jobs_list:
            for k,v in jobs_attributes.items():
                for job_item in job.find_elements_by_class_name(v):
                    job_info[k]=job_item.text
            Logging().log_writer(job_info)

        pages_xpath = "//dl[contains(@id, 'ctl00_content_vacancyList_gridList_ctl23_pagerInnerTable')]/dd[" + str(page_counter) + "]/a[contains(@class, 'f-always-blue')]"
        page_number = driver.find_element_by_xpath(pages_xpath)
        page_counter+= 1
        page_number.click()

    driver.quit()
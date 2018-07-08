"""Parse Rabota.com"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rabota_parser_loggin import Logger

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
    """Count pages"""
    pages = driver.find_elements_by_id("ctl00_content_vacancyList_gridList_ctl23_pagerInnerTable")
    pages_list = []
    for page_item in pages:
        pages_list = page_item.find_elements_by_class_name("f-always-blue")
        number_of_pages = len(pages_list)

    return number_of_pages

def parser(query):
    """Parser pages"""
    jobs_attributes = {'name': 'f-vacancylist-vacancytitle',
                       'city': 'f-vacancylist-characs-block',
                       'description': 'f-vacancylist-shortdescr'}

    driver = open_jobs_list(query)
    number_of_pages = count_pages(driver)

    job_info = {}
    """page_counter = 3 because the first element in list is the hiden field,
    the socond is the first page - no need to click on it.
    So we need to start clicking only from 3 page."""
    page_counter = 3
    for _i in range(number_of_pages):

        jobs = driver.find_elements_by_class_name("f-vacancylist-vacancyblock")

        jobs_list = []
        for job in jobs:
            jobs_list.append(job)

        for job in jobs_list:
            for key, value in jobs_attributes.items():
                for job_item in job.find_elements_by_class_name(value):
                    job_info[key] = job_item.text
            Logger().log_writer(job_info)
        pages_xpath_start = "//dl[contains(@id, 'ctl00_content_vacancyList_gridList_ctl23_pagerInnerTable')]/dd["
        pages_xpath_end = "]/a[contains(@class, 'f-always-blue')]"
        pages_xpath = '{}{}{}'.format(pages_xpath_start, page_counter, pages_xpath_end)
        page_number = driver.wait.until(EC.presence_of_element_located((By.ID, "ctl00_content_vacancyList_Breadcrumb1_breadcrumbs"))).find_element_by_xpath(pages_xpath)
        page_counter += 1
        page_number.click()

    driver.quit()

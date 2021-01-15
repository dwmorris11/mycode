#!/usr/bin python3
from selenium import webdriver
import requests
import time

class Crawler:
    def _parseAmazon(self, driver):
        jobIds = driver.find_elements_by_xpath("//div[@data-job-id]")
        jobTitles = driver.find_elements_by_class_name("job-title")
        jobPostingDates = driver.find_elements_by_class_name("posting-date")
        output = []
        for job in jobIds:
            output.append({"jobid": job.get_attribute("data-job-id")})
        for num, job in enumerate(jobTitles):
            output[num]['title'] = job.text
        for num, job in enumerate(jobPostingDates):
            output[num]['date'] = job.text
        return output

    def retrievePage(self, page, company):
        output = []
        driver = webdriver.Chrome("../chromedriver")
        options = driver.create_options()
        options.headless = True
        driver.get(page)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if company == "amazon":
            output = self._parseAmazon(driver)
        time.sleep(5)
        driver.quit()
        return output



#!/usr/bin python3
"""
This program webcrawls through software engineering employers websites for updates
in apprenticeship jobs
"""
from crawler import Crawler
import csv
import datetime
import time

def main():
  # Open the file if it exists.  If it doesn't create it and then open it
  try:
    storagefile = open("storage.csv", "r")
  except:
    storagefile = open("storage.csv", "x")
    storagefile.close()
    storagefile = open("storage.csv", "r")
  # Read the old contents of the file into a dictionary
  oldStorage = csv.DictReader(storagefile, dialect="excel", fieldnames=["company", "jobs"])
  storage = {rows["company"]: rows["jobs"] for rows in oldStorage}
  storagefile.close()
  # Retrieve the new data from the crawler and  store it in the file
  # Then compare the changes to make sure there is no change if so, provide an alert
  with open("storage.csv", "w+", newline='') as storagefile:
    storageWriter = csv.DictWriter(storagefile, dialect="excel", fieldnames=["company", "jobs"])
    crawler = Crawler()
    amazon = crawler.retrievePage('https://www.amazon.jobs/en/landing_pages/mil-apprentice', 'amazon')
    storageWriter.writerow({"company": "amazon","jobs": amazon})
    if str(amazon)==storage.get('amazon'):
      print("no change")
    else:
      print("Changed at: ", datetime.datetime.now())

if __name__ == '__main__':
    main()

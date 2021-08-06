#importing all the necesaary dependancies

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# Selecting path for the web driver

chrome_path = r"C:\Users\harsh\PycharmProjects\Scraper\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
sleep(1)
driver.get("https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365")
sleep(5)

# using 'Expected condition' library locating "See all reviews" by link_text and performing click operation
wait = WebDriverWait(driver, 5)
all_review = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'See all reviews')))
action = ActionChains(driver)
action.move_to_element(all_review).click().perform()
sleep(2)

#Selecting "newest to oldest" category from "Sort by" Drop down
cat=wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'field-input')))
catDD = Select(cat)
catDD.select_by_visible_text('newest to oldest')
sleep(2)






Review_list = []
#Iterating to 24'th page using for loop. At the end of the loop, clicking next button to get to the next page
for i in range (24):
    # In "reviews" we are storing container through which we are going to fetch all the elements
    reviews = driver.find_elements_by_xpath('//div[@class="Grid-col customer-review-body"]')
    # iterator named "review" to traverse through "reviews"
    for review in reviews:
        names = review.find_element_by_xpath(
            './/span[@class="review-footer-userNickname"]').text if review.find_elements_by_xpath(
            './/span[@class="review-footer-userNickname"]') else "NA"
        titles = review.find_element_by_xpath('.//h3[@itemprop="name"]').text if review.find_elements_by_xpath(
            './/h3[@itemprop="name"]') else "NA"
        dates = review.find_element_by_xpath(
            './/span[@class="review-date-submissionTime"]').text if review.find_elements_by_xpath(
            './/span[@class="review-date-submissionTime"]') else "-"
        body = review.find_element_by_xpath('.//div[@class="review-text"]').text if review.find_elements_by_xpath(
            './/div[@class="review-text"]') else "NA"
        stars = review.find_element_by_class_name("seo-avg-rating").text if review.find_element_by_class_name(
            "seo-avg-rating") else "NA"
        # After interating through container and storing it to variables, created a dictonary for all the fetched data
        review_item = {
            'Reviewer name': names,
            'Review Date': dates,
            'Review Title': titles,
            'Ratings': stars,
            'Review Description': body
        }
        # All the key value pair in dictonary are appending to list named"Review_list"
        Review_list.append(review_item)
    sleep(1)
    # Clicking the next page button using ActionChains,EC and Select
    next = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'paginator-btn-next')))
    action = ActionChains(driver)
    action.move_to_element(next).click().perform()
    sleep(5)
# Using "pandas" created a DataFrame and giving columns names
df=pd.DataFrame(Review_list,columns=['Reviewer name','Review Date','Review Title','Ratings','Review Description'])
# Storing all fetched data from DataFrame object "df" to csv
df.to_csv('scraper.csv')
# Closing WebDriver
driver.close()
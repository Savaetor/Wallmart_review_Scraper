

*********************************************************************************************************************
A Python Script to Scrap the Review-Section-Data from "Wallmart" using selenium and python

Please install/import all the required dependencies which includes selenium,pandas and python 3.9.5

Please do not open .csv file in excel as it'll show some random data( use libre office to view original csv)

*********************************************************************************************************************


First of all I'll thank you for giving me such an interesting assignment. By going through the making phase of "scraper" I learned alot about selenium ,DOM of E-commerce website and much more


**********************************************************************************************************************


a) I've implemented this scraper using selenium and python.

    - Firstly, I'd to study about scrapers as I did not have hands on experience on scrapers through which I get to know about their functionality, how they work, various frameworks regarding scrapers.
    - After that understanding DOM and extracting required features was also very fascinating to learn
    - Using selenium through Python was easy as I have knowledge about python
    - Talking about difficulties the main hurdle was accessing the element, as <div> component on website didn't have much clear hooks by which we can access elements. I overcome that by understanding DOM structure. Also got to know about the chrome extention named "XPath helper"
    It was quite genuinly helpful while searching for specific element using Xpath in selenium.
    - Second difficult task was to understand crawlers and and adjusting their timings.My first approach on this assignment was by using find_element_by_Xpath/class/etc. But it wasn't working properly and code was always showing "no such element" error.
    I was finally able to overcome this by using "explicit wait" and "sleep"concept. 
    - By continuous trial and error I was able to achieve the model which I desired.

b)
    - To improve my scraper I would like to add condition while pagination and make it stop at desired time. Beacause of Deadline I was not able to do that. Also during the process I studied about many scrapers, I also want to scale my scraper for all the wallmart/amazon/flipkart products. Scraper could play a major role in data science for building various kinds of Machine Learning models and algorithms.

c)
    - Yes, we can obviously make it work on other retailers as well by some customisation in this model which includes sending keys to input field, make a search and scrape all the required data.

    
 ************************************************************************************************************************   

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the input actor name from the user
actor_name = input("Enter an actor's name: ")

# set up the Chrome webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# find the search box and enter the actor's name
search_box = driver.find_element_by_name("q")
search_box.send_keys(actor_name + " filmography" + Keys.RETURN)

# find the "See results about" link and click it
see_results_about_link = driver.find_element_by_xpath("//a[contains(text(), 'See results about')]")
see_results_about_link.click()

# find the "Filmography" section and get the list of films
filmography_section = driver.find_element_by_xpath("//span[contains(text(), 'Filmography')]/ancestor::div")
films = filmography_section.find_elements_by_xpath(".//ul//li")

# print the list of films in descending order
for film in reversed(films):
    print(film.text)

# close the webdriver
driver.quit()

from tkinter import Select
from selenium import webdriver

browser = webdriver.Chrome()

# heading to the site
browser.get("https://jupiter.cloud.planittesting.com/#/")

# 1. Clicking the Login botton
login = browser.find_element_by_link_text("Login")
login.click()

# 2. Testing the user name filed
username = browser.find_element_by_id("loginUserName")
username.send_keys("Guled Ali")

# 3. Testing the Password filed
password = browser.find_element_by_id("loginPassword")
password.send_keys("I don't know")

password.submit()

# 4. Testing if the user name is displayed on the page
assert "Guled Ali" in browser.page_source


# 7. Testing the cart button
# the reason I'm using find_element_by_link_text is there is no specific class name or ID

cart = browser.find_element_by_link_text("Cart")
cart.click()


# 6. Testing the Forename filed
first_name = browser.find_element_by_id("forename")
first_name.send_keys("Guled")


# 7. Testing the Email filed
buy = browser.find_element_by_id("email")
buy.send_keys("hello@gamil.com")


# 8. Testing the address filed

address = browser.find_element_by_id("address")
address.send_keys("123 Brisbane QLD 114 Australia")

# 9. Testing the card Type dropdwon list and selecting by index

card_type = browser.find_element_by_id("cardType")
cardType = Select(card_type)
cardType.select_by_index(1)

# 10. Testing the card number filed

card = browser.find_element_by_id("card")
card.send_keys("1234567890")

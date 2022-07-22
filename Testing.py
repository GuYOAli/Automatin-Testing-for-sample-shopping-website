from selenium import webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()

# heading to the site
browser.get("https://jupiter.cloud.planittesting.com/#/")

# 1. Click the log in Button
login = browser.find_element("id", "nav-login")
login.click()

# Testing the Login form
# 2. User name "Guled Ali"
user_name = browser.find_element("id", "loginUserName")
user_name.send_keys("Guled Ali")

# 3. Password
password = browser.find_element("id", "loginPassword")
password.send_keys("Hello123")

# Submit the form
password.submit()

# 4. Testing if the user name is displayed on the page
assert "Guled Ali" in browser.page_source

# 5. Testing the cart button

cart = browser.find_element("id", "nav-cart")
cart.click()

# 6. Testing the Forename filed
forename = browser.find_element("id", "forename")
forename.send_keys("Guled")

# 7. Testing the Email filed

email = browser.find_element("id", "email")
email.send_keys("hello@gmail.com")

# 8. Testing the address filed

address = browser.find_element("id", "address")
address.send_keys("123 Brisbane 419 QLD Australia")

# 9. Testing the card Type and selecting by index

card_type = browser.find_element("id", "cardType")
select = Select(card_type)
select.select_by_index(1)

# 10. Testing card number filed

card_number = browser.find_element("id", "card")
card_number.send_keys("0123456789")

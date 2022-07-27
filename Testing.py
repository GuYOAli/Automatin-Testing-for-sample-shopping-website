from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class Test:

    try:

        def __init__(self):
            self.browser = webdriver.Chrome()  # intializing our driver

            # heading to the site
            self.browser.get("https://jupiter.cloud.planittesting.com/#/")

        # 1. Click the log in Button
        def login(self):
            login = self.browser.find_element("id", "nav-login")
            login.click()

        def contact(self):
            login = self.browser.find_element("id", "nav-contact")
            login.click()

        # Testing the Login form
        def login_form(self):
            # 2. User name
            user_name = self.browser.find_element("id", "loginUserName")
            user_name.send_keys("Guled Ali")

            # 3. Password
            password = self.browser.find_element("id", "loginPassword")
            password.send_keys("Hello123")

            # Submit the form
            password.submit()

        # 4. Testing if the user name is displayed on the page
        def assertion(self):
            assert "Guled Ali" in self.browser.page_source

        # 5. Testing the cart button
        def cart(self):
            cart = self.browser.find_element("id", "nav-cart")
            cart.click()

        # 6. Testing the Forename filed
        def forename(self):
            forename = self.browser.find_element("id", "forename")
            forename.send_keys("Guled")

        # 7. Testing the Email filed
        def email(self):
            email = self.browser.find_element("id", "email")
            email.send_keys("hello@gmail.com")

        # 8. Testing the address filed
        def address(self):
            address = self.browser.find_element("id", "address")
            address.send_keys("123 Brisbane 419 QLD Australia")

        # 9. Testing the card Type and selecting by index
        def cardType(self):
            card_type = self.browser.find_element("id", "cardType")
            select = Select(card_type)
            select.select_by_index(1)

        # 10. Testing card number filed
        def card_number(self):
            card_number = self.rowser.find_element("id", "card")
            card_number.send_keys("0123456789")

        # Closing the browser
        def quite(self):
            self.browser.quit()

    except NoSuchElementException:
        print("Please enter valid element ID or class name ")


if __name__ == "__main__":
    try:

        test = Test()

        test.contact()
        test.email()
        test.quite()

    except NoSuchElementException:
        print("Please enter valid element ID or class name ")


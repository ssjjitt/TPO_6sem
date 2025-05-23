from selenium.webdriver.common.by import By
from .BasePage import BasePage
from realization2.Locators.ProductPageLocators import ProductPageLocators

class ProductPage(BasePage):
    FIRST_PRODUCT_BUTTON = (By.XPATH, "(//button[contains(@class,'btn_inventory')])[1]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, browser):
        super().__init__(browser)

    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.FIRST_PRODUCT_BUTTON).click()

    def get_cart_count(self):
        return self.browser.find_element(*ProductPageLocators.CART_ICON).text

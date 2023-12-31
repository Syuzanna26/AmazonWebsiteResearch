from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__addToCartButtonLocator = (By.ID, "add-to-cart-button")
        self.__productNameLocator = (By. ID, "title")
        self.__productPriceLocator = (By. ID, "corePrice_feature_div")

    def click_on_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(self.__addToCartButtonLocator)
        self._click(addToCartButtonElement)

    def get_product_name(self):
        productNameElement = self._find_element(self.__productNameLocator)
        return self._get_element_text(productNameElement)

    def get_product_price(self):
        productPriceElement = self._find_element(self.__productPriceLocator)
        return self._get_element_text(productPriceElement)

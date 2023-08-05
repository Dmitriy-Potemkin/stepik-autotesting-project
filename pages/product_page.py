from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_product_value(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text[1:]

    def should_be_correct_bought_item(self, item):
        bought_item = self.browser.find_element(*ProductPageLocators.BOUGHT_ITEM_NAME).text
        assert str(item) == bought_item, "Bought item is incorrect"
    
    def should_be_correct_bought_value(self, value):
        bought_value = self.browser.find_element(*ProductPageLocators.BOUGHT_ITEM_PRICE).text[1:]
        assert float(value) == float(bought_value), "Basket price is incorrect"

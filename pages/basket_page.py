from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
           "Items are in basket, but should not be"

    def basket_shoud_have_items(self):
        assert self.browser.find_element(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Basket is empty, but should not be"
    
    def should_be_empty_basket_text(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text, \
            "Basket is empty, but no text is present"
    
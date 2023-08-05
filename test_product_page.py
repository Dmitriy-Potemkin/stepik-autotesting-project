from pages.product_page import ProductPage


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()

# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     item_name = page.get_product_name()
#     item_value = page.get_product_value()
#     page.add_to_basket()
#     page.should_be_correct_bought_item(item_name)
#     page.should_be_correct_bought_value(item_value)

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    item_name = page.get_product_name()
    item_value = page.get_product_value()
    page.add_to_basket()
    page.should_be_correct_bought_item(item_name)
    page.should_be_correct_bought_value(item_value)
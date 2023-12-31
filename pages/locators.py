from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name=login_submit]")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    BOUGHT_ITEM_NAME = (By.CSS_SELECTOR, "div#messages div.alertinner strong")
    BOUGHT_ITEM_PRICE = (By.CSS_SELECTOR, "div#messages div.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "div.content div#content_inner>p:only-child")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div.content form#basket_formset")

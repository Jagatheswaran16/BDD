from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import base
import green
from behave import *

class homepage:
    __search= '//input[@type="search"]'
    __addcart_button='//button[normalize-space()="ADD TO CART"]'
    __cart= "//a[@class='cart-icon']/img"
    __checkout="//button[text()='PROCEED TO CHECKOUT']"
    __material= "Free Access to InterviewQues/ResumeAssistance/Material"
    def my_search(self, Vegitable):
        base.driver.find_element(By.XPATH, self.__search).send_keys(Vegitable)
        time.sleep(1)
    def my_Add_a_product_to_cart(self):
        base.driver.find_element(By.XPATH, self.__addcart_button).click()
        time.sleep(1)
    def my_Go_to_the_cart(self):
        base.driver.find_element(By.XPATH, self.__cart).click()
        ele = base.driver.find_element(By.XPATH, self.__checkout)
        time.sleep(1)
        actions = ActionChains(base.driver)
        actions.double_click(ele).perform()
        time.sleep(1)
    def my_material(self):
        time.sleep(1)
        return base.driver.find_element(By.LINK_TEXT, self.__material).text
home=homepage()

class Cart_page:
    product_name= "//p[@class='product-name']"
    promocode= '.promoCode'
    promo_apply= '.promoBtn'
    promo_info= ".promoInfo"
    discount_amt= "//span[@class='discountAmt']"
    place_order= "//button[normalize-space()='Place Order']"

    def my_Verify_Product_name(self):
       return base.driver.find_element(By.XPATH, self.product_name).text

    def my_Promocode_is_applied(self, rahul):
        base.driver.find_element(By.CSS_SELECTOR, self.promocode).send_keys(rahul)
        base.driver.find_element(By.CSS_SELECTOR, self.promo_apply).click()

    def my_Promocode_code_sucessfull_message_should_be_displayed(self):
        wait = WebDriverWait(base.driver, 30)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.promo_info)))
        return base.driver.find_element(By.CSS_SELECTOR, self.promo_info).text

    def my_Dicount_must_be_applied(self):
        return base.driver.find_element(By.XPATH, self.discount_amt).text

    def my_Promocode2_is_applied(self, rahul):
        self.my_Promocode_is_applied(rahul)
        self.my_Promocode_code_sucessfull_message_should_be_displayed()

    def my_Place_order_button_is_pressed(self):
        base.driver.find_element(By.XPATH, self.place_order).click()

Cart=Cart_page()

class countrypage:

    country_drp= "//div[@class='wrapperTwo']//div//select"
    tc= "Terms & Conditions"
    proceed= "//button[normalize-space()='Proceed']"
    warrning_msg= "//b[normalize-space()='Please accept Terms & Conditions - Required']"
    checkbox= "//input[@type='checkbox']"

    def my_country_is_selected(self, country):
        drp = Select(base.driver.find_element(By.XPATH, self.country_drp))
        drp.select_by_visible_text(country)

    def my_Terms_Conditions_is_not_selected(self):
        return base.driver.find_element(By.LINK_TEXT, self.tc).text

    def my_Proceed_button_is_clicked(self):
        base.driver.find_element(By.XPATH, self.proceed).click()

    def my_Terms_Conditions_warning_message_is_displayed(self):
        return base.driver.find_element(By.XPATH, self.warrning_msg).text

    def my_check_box(self):
        base.driver.find_element(By.XPATH, self.checkbox).click()
        time.sleep(2)

country=countrypage()


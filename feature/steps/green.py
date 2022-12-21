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
import variables
import POM
from behave import *

@given(u'Open Greenkart website')
def step_impl(context):
    context.driver = base.driver
    context.driver.get(base.URL)

@when(u'Search product name')
def Search_product_name(context):
    POM.home.my_search(variables.veg)

@when(u'Add a product to Cart')
def Add_a_product_to_cart(context):
    POM.home.my_Add_a_product_to_cart()

@when(u'Go to the cart')
def Go_to_the_cart(context):
    POM.home.my_Go_to_the_cart()

@then(u'Verify Product name')
def Verify_Product_name(context):
    k = POM.Cart.my_Verify_Product_name()
    assert k == "Cucumber - 1 Kg"

@when(u'Promocode is applied')
def Promocode_is_applied(context):
    POM.Cart.my_Promocode_is_applied(variables.promo)

@then(u'Promocode code sucessfull message should be displayed')
def Promocode_code_sucessfull_message_should_be_displayed(context):

    l = POM.Cart.my_Promocode_code_sucessfull_message_should_be_displayed()
    assert l == variables.promo_verify

@then(u'Dicount must be applied')
def Dicount_must_be_applied(context):

    a = POM.Cart.my_Dicount_must_be_applied()
    assert a == variables.promo_amt_verify

@when(u'Promocode2 is applied')
def Promocode2_is_applied(context):

    POM.Cart.my_Promocode_is_applied("rahulshettyacademy")
    l=POM.Cart.my_Promocode_code_sucessfull_message_should_be_displayed()
    assert l == variables.promo_verify

@when(u'Place order button is pressed')
def Place_order_button_is_pressed(context):
    POM.Cart.my_Place_order_button_is_pressed()

@when(u'country is selected')
def country_is_selected(context):
    POM.country.my_country_is_selected()

@when(u'Terms & Conditions is not selected')
def Terms_Conditions_is_not_selected(context):
    terms=POM.country.my_Terms_Conditions_is_not_selected()
    assert terms== variables.TC

@when(u'Proceed button is clicked')
def Proceed_button_is_clicked(context):
    POM.country.my_Proceed_button_is_clicked()

@then(u'Terms & Conditions warning message is displayed')
def Terms_Conditions_warning_message_is_displayed(context):
    waarmsg= POM.country.my_Terms_Conditions_warning_message_is_displayed()
    assert waarmsg== variables.warrning_message

@then(u'promocode3 is applied and country and Terms & Conditions is selected')
def step_impl(context):
    POM.Cart.my_Promocode_is_applied(variables.promo)
    l=POM.Cart.my_Promocode_code_sucessfull_message_should_be_displayed()
    assert l == variables.promo_verify
    POM.Cart.my_Place_order_button_is_pressed()
    POM.country.my_country_is_selected()
    POM.country.my_check_box()
    POM.country.my_Proceed_button_is_clicked()
    a = POM.home.my_material()
    assert a == variables.homepage_link


































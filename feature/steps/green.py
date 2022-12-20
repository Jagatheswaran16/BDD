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

from behave import *


@given(u'Open Greenkart website')
def step_impl(context):
    context.driver = base.driver
    context.driver.maximize_window()
    context.driver.get(base.URL)
    context.driver.implicitly_wait(10)


@when(u'Search product name')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Cucumber")
    time.sleep(1)


@when(u'Add a product to Cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='ADD TO CART']").click()


@when(u'Go to the cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='cart-icon']/img").click()
    time.sleep(3)
    ele = context.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    actions = ActionChains(context.driver)
    actions.double_click(ele).perform()
    time.sleep(3)


@then(u'Verify Product name')
def step_impl(context):
    k = context.driver.find_element(By.XPATH, "//p[@class='product-name']").text
    print(k)
    assert k == "Cucumber - 1 Kg"


@when(u'Promocode is applied')
def step_impl(context):

    context.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
    context.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()


@then(u'Promocode code sucessfull message should be displayed')
def step_impl(context):
    wait = WebDriverWait(context.driver, 30)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
    time.sleep(1)
    l = context.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
    assert l == 'Code applied ..!'


@then(u'Dicount must be applied')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//span[@class='discountAmt']").text
    assert a == '43.2'


@when(u'Promocode2 is applied')
def step_impl(context):

    context.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
    context.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
    wait = WebDriverWait(context.driver, 30)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
    time.sleep(1)
    l = context.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
    assert l == 'Code applied ..!'

@when(u'Place order button is pressed')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()


@when(u'country is selected')
def step_impl(context):
    drp=Select(context.driver.find_element(By.XPATH,"//div[@class='wrapperTwo']//div//select" ))
    drp.select_by_visible_text("India")




@when(u'Terms & Conditions is not selected')
def step_impl(context):
    terms=context.driver.find_element(By.LINK_TEXT, "Terms & Conditions").text
    assert terms== 'Terms & Conditions'


@when(u'Proceed button is clicked')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()


@then(u'Terms & Conditions warning message is displayed')
def step_impl(context):
    waarmsg=context.driver.find_element(By.XPATH, "//b[normalize-space()='Please accept Terms & Conditions - Required']").text
    assert waarmsg== 'Please accept Terms & Conditions - Required'


@then(u'promocode3 is applied and country and Terms & Conditions is selected')
def step_impl(context):

    context.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
    context.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
    wait = WebDriverWait(context.driver, 30)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
    time.sleep(1)
    l = context.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
    assert l == 'Code applied ..!'
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
    drp1 = Select(context.driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
    drp1.select_by_visible_text("Aruba")
    context.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()
    time.sleep(2)
    a = context.driver.find_element(By.LINK_TEXT, 'Free Access to InterviewQues/ResumeAssistance/Material').text
    time.sleep(1)
    assert a == 'Free Access to InterviewQues/ResumeAssistance/Material'
    print(a)

































from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')


URL="https://rahulshettyacademy.com/seleniumPractise/#/"

driver.implicitly_wait(5)
from behave import *
from selenium import webdriver


def before_scenario(context, scenario):
    print(" Starting new scenario...")
    context.driver = webdriver.Chrome()
    
def after_scenario(context, scenario):
    print(" Finishing scenario...")
    context.driver.quit()
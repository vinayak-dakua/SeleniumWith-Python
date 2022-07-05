import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser=="ff":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    else:
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#  Pytest HTML Report #
#add enviroment

def pytest_configure(config):
    config._metadata['Project Name'] = 'non Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Vinayak'

@pytest.mark.optionalhook
def pytesr_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Pluging", None)



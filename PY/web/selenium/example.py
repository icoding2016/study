from selenium import webdriver



def test():
    driver = webdriver.Firefox()
    driver.get('https://www.selenium.dev')
    print(driver.title)
    print(driver.page_source)


test()    
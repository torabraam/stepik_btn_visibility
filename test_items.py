import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_visibility(browser):
    browser.get(link)
    #time.sleep(20) #for checking --language=fr
    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(button) > 0, "button is not visible"
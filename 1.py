#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://passport.jd.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fwww.jd.com%2F%3Futm_source%3Dmedia%26utm_medium%3Dcpc%26utm_campaign%3D%26utm_term%3Dmedia_8_58871498_s9373548f9a17397b48.46781421")
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("suhaihong2008@126.com")
driver.find_element_by_id("nloginpwd").clear()
driver.find_element_by_id("nloginpwd").send_keys("Cmd200819860")
driver.find_element_by_id("loginsubmit").click()
driver.maximize_window()
driver.find_element_by_link_text("话费").click()
nowhandle=driver.current_window_handle
allhandles=driver.window_handles
for handle in allhandles:
    if handle !=nowhandle:
        driver.switch_to_window(handle)
        driver.switch_to_frame("iframeRecharge")
        driver.find_element_by_id("txtPn").clear()
        driver.find_element_by_id("txtPn").send_keys("18612830372")     
        driver.find_element_by_id("submit").click()
        driver.close()
driver.switch_to_window(nowhandle)
for handle in allhandles:
    if handle != nowhandle:
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_id("submit").click()


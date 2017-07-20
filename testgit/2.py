#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://passport.jd.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fwww.jd.com%2F%3Futm_source%3Dmedia%26utm_medium%3Dcpc%26utm_campaign%3D%26utm_term%3Dmedia_8_58871498_s9373548f9a17397b48.46781421")
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("suhaihong2008@126.com")
driver.find_element_by_id("nloginpwd").clear()
driver.find_element_by_id("nloginpwd").send_keys("Cmd200819860")
driver.find_element_by_id("loginsubmit").click()
driver.maximize_window()
PlaneTicket = driver.find_element_by_link_text("机票")
ActionChains(driver).move_to_element(PlaneTicket).perform()
##driver.switch_to_fram
driver.switch_to_frame(driver.find_Element_By_xpath("//iframe[contains(@src,'http://jipiao.jd.com/htm/iframeTrip.html')]"))
InChina = driver.find_element_by_link_text("国际")
ActionChains(driver).move_to_element(InChina).perform()
    
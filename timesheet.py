from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
import time
# we import the Twilio client from the dependency we just installed
from twilio.rest import TwilioRestClient

# the following line needs your Twilio Account SID and Auth Token
client = TwilioRestClient("xx", "xx")

today = date.today().strftime("%m/%d/%Y")
weekday = date.today().isoweekday()
print(today)
print(weekday)
driver = webdriver.Firefox()
driver.get('https://example.ghg.com')

""" Input "email" and "pass" here change based on websites page source """
username = driver.find_element_by_name("j_username")
password = driver.find_element_by_name("j_password")

login = driver.find_element_by_id("loginBtn-btnEl")

time.sleep(0.5)

""" Enter both username and password """

username.send_keys("xx")
password.send_keys("xx")
login.click()
time.sleep(1)

""" Going to extension link where timesheet will be insert """

website = 'https://example.ghg.com'
next_page = website + '/timesheet/view.do?role=Employee'
driver.get(next_page)

# """ Adding previous timesheet Charge Code instead of reselecting each everyweek. """
# element = driver.find_element_by_xpath("//*[contains(text(), 'Add previous timesheet Charge Code')]")
# element.click()
# time.sleep(5)

""" Clicking on monday cell and type time and save"""
if weekday == 1:
    """ Adding previous timesheet Charge Code instead of reselecting each everyweek. """
    element = driver.find_element_by_xpath("//*[contains(text(), 'Add previous timesheet Charge Code')]")
    element.click()
    time.sleep(5)

    monday = driver.find_element_by_xpath("//td[@class=' x-grid-cell x-grid-cell-gridcolumn-1109   ']")
    monday.click()
    time.sleep(3)

    monday_time = driver.find_element_by_name(today)
    monday_time.send_keys(8)
    time.sleep(1)
    monday_time.send_keys(Keys.ENTER)
    time.sleep(3)


    # save = driver.find_element_by_id("saveBtn-btnEl")
    # save.click()
    # driver.close()

#""" Clicking on Tuesday cell and inserting time and save"""

elif weekday == 2:
    tuesday = driver.find_element_by_xpath("//td[@class=' x-grid-cell x-grid-cell-gridcolumn-1110   ']")
    tuesday.click()
    time.sleep(5)

    tuesday_time = driver.find_element_by_name(today)
    tuesday_time.send_keys(8)
    time.sleep(1)
    tuesday_time.send_keys(Keys.ENTER)

    save = driver.find_element_by_id("saveBtn-btnEl")
    save.click()
    driver.close()


#""" Clicking on Wednesday cell and inserting time and save"""
elif weekday == 3:

    wednesday = driver.find_element_by_xpath("//td[@class=' x-grid-cell x-grid-cell-gridcolumn-1111   ']")
    wednesday.click()
    time.sleep(5)

    wednesday_time = driver.find_element_by_name(today)
    wednesday_time.send_keys(8)
    time.sleep(1)
    wednesday_time.send_keys(Keys.ENTER)

    save = driver.find_element_by_id("saveBtn-btnEl")
    save.click()
    driver.close()


#""" Clicking on Thursday cell and inserting time and save"""
elif weekday == 4:

    thursday = driver.find_element_by_xpath("//td[@class=' x-grid-cell x-grid-cell-gridcolumn-1112   ']")
    thursday.click()
    time.sleep(5)

    thursday_time = driver.find_element_by_name(today)
    thursday_time.send_keys(8)
    time.sleep(1)
    thursday_time.send_keys(Keys.ENTER)

    save = driver.find_element_by_id("saveBtn-btnEl")
    save.click()
    driver.close()


#""" Clicking on Friday cell and inserting time and save"""
elif weekday == 5:
    friday = driver.find_element_by_xpath("//td[@class=' x-grid-cell x-grid-cell-gridcolumn-1113   ']")
    friday.click()
    time.sleep(5)

    friday_time = driver.find_element_by_name(today)
    friday_time.send_keys(8)
    time.sleep(1)
    friday_time.send_keys(Keys.ENTER)


    save = driver.find_element_by_id("saveBtn-btnEl")
    save.click()


    #""" When it's Friday it will submit the timesheet after saving."""
    submit = driver.find_element_by_id("submitBtn-btnEl")
    submit.click()

    # Now checking Total time and sending text message with Total hours submitted
    record = driver.find_element_by_xpath(
        "//td[@class='disabled-cell x-grid-cell x-grid-cell-gridcolumn-1052   x-grid-cell-first']")
    record_element = record.text
    record_time = record.get_attribute("value")
    print(record_element)
    client.messages.create(to="+xx", from_="+xx",
                           body="You have submit {} hours".format(record_element))
    driver.close()

else:
    print("done")
    driver.close()



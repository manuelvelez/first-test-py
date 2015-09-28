from lettuce import *
from lettuce_webdriver.util import assert_false  
from lettuce_webdriver.util import AssertContextManager 
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

@step(u'Given ikabo is opened')
def given_ikabo_is_opened(step):
	time.sleep(2)

@step(u'When I configure valo with "([^"]*)"')
def when_i_configure_valo_with_group1(step, group1):
	valoUrl = world.driver.find_element_by_css_selector('[data-type=valoURL]')
	valoUrl.clear()
	valoUrl.send_keys(group1);

@step(u'And I Configure the tenant with "([^"]*)"')
def and_i_configure_the_tenant_with_group1(step, group1):
	valoTenant = world.driver.find_element_by_css_selector('[data-type=valoTenant]')
	valoTenant.clear()
	valoTenant.send_keys(group1);

@step(u'And click start button')
def and_click_start_button(step):
	world.driver.find_element_by_css_selector('[data-type=save-config]').click()

@step(u'Then I can see the main screen with "([^"]*)" and "([^"]*)"')
def then_i_can_see_the_main_screen_with(step, url, tenant):
	time.sleep(1)

	configElement = world.driver.find_element_by_xpath('//*[@id="mod-user-1"]/div[@data-id="profile"]').text
	assert configElement == url + " " + tenant

	streamLists = world.driver.find_elements_by_css_selector("[class=description]")
	assert len(streamLists) > 0


 
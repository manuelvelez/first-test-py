from lettuce import before, world, after  
from selenium import webdriver  
import selenium.webdriver.chrome.service as service
import lettuce_webdriver.webdriver  
 
@before.all  
def setup_browser(): 
	chrome_path="/opt/ikabo_releases/IKABO-1.0.0-linux-x64-caa40496/IKABO-1.0.0" 

	opts = webdriver.ChromeOptions()
	opts.binary_location = chrome_path

	world.driver = webdriver.Chrome(chrome_options=opts)

@after.all
def close_browser(total):
	world.driver.close()
	print "Congratulations, %d of %d scenarios passed!" % (
    total.scenarios_ran,
    total.scenarios_passed
    )


Feature: Sarah opens ikabo  
  
Scenario: open ikabo  
  Given ikabo is opened
  When I configure valo with "192.168.34.244:8888"
  And I Configure the tenant with "twitter0"
  And click start button
  Then I can see the main screen with "192.168.34.244:8888" and "twitter0"
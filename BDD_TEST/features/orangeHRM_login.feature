Feature:OrangeHRM Logo
 Scenario: Logo presence on OrangeHRM home page
    Given launch chrome browser
    When Open OrangeHRM homepage
    And Enter username "admin" and password "admin123"
    And click on login button  
    Then user must login succesfully to the homepage 
    
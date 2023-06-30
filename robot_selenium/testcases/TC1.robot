*** Settings ***
Library  SeleniumLibrary
Suite Setup     Initialise the browser
Suite Teardown      close browser

*** Variables ***
${url}  https://rahulshettyacademy.com/AutomationPractice/
${radio}        //*[contains(text(),'Option4')]

*** Keywords ***
Initialise the browser
    OPEN BROWSER    ${url}   chrome
    maximize browser window

Open new window demo
    Click Element    //button[@id='openwindow']
    Click Element    //button[@id='openwindow']
    Click Element    //button[@id='openwindow']
#    Switch Window   new
    Get Window Handles
    Wait Until Element Is Visible    //a[normalize-space()='Access all our Courses']
    Click Element    //a[normalize-space()='Access all our Courses']

LoginToApplication
    click element    xpath://input[@id='checkBoxOption1']
    input text  xpath://input[@id='name']   Devendra
    select checkbox  checkBoxOption2




*** Test Cases ***

LoginTest
    LoginToApplication
    click element    xpath://input[@value='radio1']
    ${isExist}=  Run Keyword And Return Status    Element Should Be Visible    ${radio}
    Log To Console    ${isExist}

Demo switch window
    LoginToApplication
    Open new window demo


Select element from dropdown list
    sleep  2
    select from list by label  dropdown-class-example   Option1
    sleep   2
    select from list by index  dropdown-class-example   3
    sleep  2
    
    
Enter value into textbox and handle alert
    Input Text    //input[@id='name']    Devendra Sing Shakya
    Sleep    2
    Click Element    //input[@id='alertbtn']
    Sleep    2
#    Handle Alert    accept
#    Handle Alert    dismiss
    Handle Alert    leave
    sleep   2

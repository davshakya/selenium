***setting***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections
Library    SeleniumLibrary
Library    Process


*** Variables ***
${url}    http://universities.hipolabs.com/search?
${param}    country=India
${uri_demo}    https://reqres.in/api/users


*** Keywords ***




*** Test Cases ***

Do get request and validate data
    Create Session  mysession  https://reqres.in     verify=true
    # ${get_uri}    Catenate       ${url}      ${param}
    ${response}=  GET On Session  mysession  ${uri_demo}      
    Log To Console    "########"+${response.json()}
    Status Should Be  200  ${response}  #Check Status as 200
    





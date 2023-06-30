***setting***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections
Library    SeleniumLibrary
Library    Process
Library    Telnet
Suite Setup         Start session
Suite Teardown      Close Session


*** Variables ***
${uri}    http://universities.hipolabs.com/search?
${param}    country=India
${uri_demo}    https://reqres.in/api/users


*** Keywords ***
Start session
        Create Session  mysession  https://reqres.in     verify=true

Close Session
    Delete All Sessions

*** Test Cases ***

Do get request and validate data
    # ${get_uri}    Catenate       ${url}      ${param}
    ${response}=  GET On Session  mysession  ${uri_demo}
    Log To Console    >> ${response.json()}[data][0][email]
    ${id}   Get Value From Json    ${response.json()}    data[0][email]
    Log To Console      >> ${id}
    Status Should Be  200  ${response}  #Check Status as 200





*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  uusi
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  uusi
    Set Password  lyhyt
    Set Password Confirmation  lyhyt
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Fail With Message  Username already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

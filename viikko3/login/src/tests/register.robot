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

Register With Password That Contains Letters And Numbers
    Set Username  uusi
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password That Contains Letters And Special Character
    Set Username  uusi
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password And Confirmation
    Set Username  uusi
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Different Password And Confirmation
    Set Username  uusi
    Set Password  kalle123
    Set Password Confirmation  kalle124
    Click  button >> text=Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Password That Contains Only Letters
    Set Username  uusi
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password can not consist only of letters

Register With Password That Contains Only Uppercase Letters
    Set Username  uusi
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password can not consist only of letters

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

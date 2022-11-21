*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  aarni
    Set Password  aarni123
    Set Password Confirmation  aarni123
    Submit Credentials
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  aarni123
    Set Password Confirmation  aarni123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  aarnii
    Set Password  a1
    Set Password Confirmation  a1
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  aarniii
    Set Password  aarni123
    Set Password Confirmation  aarni1234
    Submit Credentials
    Register Should Fail With Message  Passwords must match

Login After Successful Registration
    Set Username  aarnipaarni
    Set Password  aarni123
    Set Password Confirmation  aarni123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  aarnipaarni
    Set Password  aarni123
    Submit Login
    Login Should Succeed


Login After Failed Registration
    Set Username  aarnipaarni123
    Set Password  aarni123
    Set Password Confirmation  aarni123
    Submit Credentials
    Register Should Fail With Message  Invalid username
    Go To Login Page
    Set Username  aarnipaarni123
    Set Password  aarni123
    Submit Login
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Login
    Click Button  Login

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

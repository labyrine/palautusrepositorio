*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  hyvanimi
    Set Password  huonosalasana123
    Validate Password  huonosalasana123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  hy
    Set Password  huonosalasana123
    Validate Password  huonosalasana123
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 letters long

Register With Valid Username And Too Short Password
    Set Username  hyvanimi
    Set Password  huonos8
    Validate Password  huono8
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 letters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  hyvanimi
    Set Password  huonosalasana
    Validate Password  huonosalasana
    Submit Registration
    Registration Should Fail With Message  Password has to contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  hyvanimi
    Set Password  huonosalasana123
    Validate Password  huonosalasana124
    Submit Registration
    Registration Should Fail With Message  Passwords have to be the same

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  huonosalasana123
    Validate Password  huonosalasana123
    Submit Registration
    Registration Should Fail With Message  Username is used already

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Validate Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
# ...
    Set Username  testi
    Set Password  testitesti1
    Set Password Confirmation  testitesti1
    Submit Credentials
    Registration Should Succeed


Register With Too Short Username And Valid Password
# ...
    Set Username  te
    Set Password  testitesti1
    Set Password Confirmation  testitesti1
    Submit Credentials
    Registration Should Fail With Message  Username must be at least 3 characters long.

Register With Valid Username And Too Short Password
# ...
    Set Username testi
    Set Password testi1
    Set Password Confirmation testi1
    Submit Credentials
    Registration Should Fail With Message  Password must be at least 8 characters long.

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
# ...
    Set Username testi
    Set Password testitesti
    Set Password Confirmation testitesti
    Submit Credentials
    Registration Should Fail With Message  Password must contain at least one non-letter character.

Register With Nonmatching Password And Password Confirmation
# ...
    Set Username testi
    Set Password testitesti1
    Set Password Confirmation testitesti2
    Submit Credentials
    Registration Should Fail With Message  Passwords do not match.


Register With Username That Is Already In Use
#
    Set Username testi
    Set Password testitesti1
    Set Password Confirmation testitesti1
    Submit Credentials
    Registration Should Succeed
    Reset Application Create User  testi  testitesti1

    Set Username testi
    Set Password testitesti1
    Set Password Confirmation testitesti1
    Submit Credentials
    Registration Should Fail With Message  Username is already in use.

Reset Application Create User And Go To Register Page
    Reset Application Create User
    Go To Register Page



*** Keywords ***
#...
Registration Should Succeed
    Page Should Contain    Welcome to Ohtu Application!





Reset Application Create User And Go To Register Page
    Reset Application Create User
    Go To Register Page


Reset Application Create User
    Reset Application
    Create User  testi    testitesti1

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
    Input Text  password_confirmation  ${password_confirmation}
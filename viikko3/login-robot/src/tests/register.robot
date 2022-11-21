*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input Credentials  matti  matti1234
    Output Should Contain  Username already exists


Register With Too Short Username And Valid Password
    Input Credentials  a  matti1234
    Output Should Contain  Username should be longer than 2 characters


Register With Valid Username And Too Short Password
    Input Credentials  aarni  a1
    Output Should Contain  Password should be longer than 8 characters


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  aarni  aarniaarni
    Output Should Contain  Password can't only contain letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  matti  matti1234

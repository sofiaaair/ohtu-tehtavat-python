*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Creating User  kayttajanen  salasana1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Creating User  heppatytto  salasana1
    Output Should Contain  Username already exist

Register With Too Short Username And Valid Password
    Creating User  mo  salasana1
    Output Should Contain  Username must contain at least 3 characters

Register With Valid Username And Too Short Password
    Creating User  gamerforlife  m01
    Output Should Contain  Password must contain at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Creating User  newuser  sanojavain
    Output Should Contain  Password must contain numbers

*** Keywords ***

Create User And Input New Command
    Create User  heppatytto  salasana1
    Input New Command

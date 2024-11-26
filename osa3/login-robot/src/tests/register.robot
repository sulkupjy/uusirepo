*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Create User  jari  jari12345
    Input Login Command

Register With Already Taken Username And Valid Password
    Create User  kari  kari12345
    Input Login Command
    Run Keyword And Expect Error    User with username kari already exists    Create User    kari    kari12345

Register With Too Short Username And Valid Password
    Run Keyword And Expect Error    UserInputError: tunnus liian lyhyt tai virheellinen    Create User    k    kari12345

Register With Enough Long But Invalid Username And Valid Password
    Run Keyword And Expect Error    UserInputError: tunnus liian lyhyt tai virheellinen    Create User    k456    kari12345

Register With Valid Username And Too Short Password
    Run Keyword And Expect Error    UserInputError: salasana liian lyhyt tai virheellinen    Create User    kari    kar1

Register With Valid Username And Long Enough Password Containing Only Letters
    Run Keyword And Expect Error    UserInputError: salasana liian lyhyt tai virheellinen    Create User    kari    karikari


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

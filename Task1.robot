*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.myntra.com/

*** Test Cases ***
Myntra Automation
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Mouse Over    xpath=//a[@data-group="women"]
    Sleep  2s
    Click Element    xpath=//a[contains(@href,'lehenga-choli')]
    Sleep    2s


    Scroll Element Into View    xpath=//span[text()="Color"]
    Sleep  2s


    Click Element    xpath=//span[@data-colorhex="purple"]
    Sleep    2s

    ${name}=  Get Text    xpath=//h3[text()="JOVK DESIGN"]
    Log To Console    ${name}

    Sleep    3s

    Close Browser




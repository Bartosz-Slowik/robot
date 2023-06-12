*** Settings ***
Documentation    UE Manager Application Keywords and Variables
Library           Telnet

*** Variables ***
${HOST}           pk-robot.ddns.net
${PORT}           8000

*** Keywords ***
Connect to UE Manager
    Open Connection    ${HOST}    ${PORT}
    Login              username    password

Attach UE
    [Arguments]       ${ue_id}
    Write             attach ${ue_id}
    Read Until         prompt

Detach UE
    [Arguments]       ${ue_id}
    Write             detach ${ue_id}
    Read Until         prompt

Start Traffic
    Write             start_traffic
    Read Until         prompt

Stop Traffic
    Write             stop_traffic
    Read Until         prompt

Verify UE Attached
    [Arguments]       ${ue_id}
    Write             show_status ${ue_id}
    Read Until         prompt
    Should Contain     ${output}    Attached

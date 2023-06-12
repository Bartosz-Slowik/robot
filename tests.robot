*** Settings ***
Documentation    UE Manager Application Tests
Resource         keywords.resource

*** Test Cases ***
Attach UE and Verify Attachment
    Connect to UE Manager
    ${ue_id}=    Set Variable    UE001
    Attach UE    ${ue_id}
    Verify UE Attached    ${ue_id}
    Disconnect

Detach UE and Verify Detachment
    Connect to UE Manager
    ${ue_id}=    Set Variable    UE001
    Attach UE    ${ue_id}
    Verify UE Attached    ${ue_id}
    Detach UE    ${ue_id}
    Verify UE Not Attached    ${ue_id}
    Disconnect

Start and Stop Traffic
    Connect to UE Manager
    Start Traffic
    # Perform necessary checks or verifications during traffic
    Stop Traffic
    Disconnect

*** Settings ***
Library    ./keywords.py

*** Test Cases ***
Build FPGA Image
    [Tags]    implementation
    Run Synthesis and Implementation

Signoff FPGA Image
    [Tags]    implementation
    Parse Synthesis Report for Errors
    Parse DRC Report for Errors
    Parse CDC Report for Errors
    Perform Timing Analysis

Deploy FPGA Image
    [Tags]    Deploy
    Run Deployment

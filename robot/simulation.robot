*** Settings ***
Library      ./keywords.py
Test Tags    simulation

*** Test Cases ***
Test A
    ${output}=    Run Simulation    testmame=test_a
    Parse Output For Errors    ${output}
    Parse Output For Pass    ${output}    Test passed!


Test B
    ${output}=    Run Simulation    testmame=test_b
    Parse Output For Errors    ${output}
    Parse Output For Pass    ${output}    Test passed!

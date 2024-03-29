## Executive Summary

Organizations use industrial control systems to automate processes that make their day-to-day operations possible.  The "brains" of these systems are programmable logic controllers, miniature computers, that run the programs to execute the processes.  Attacks are typically designed to target controllers to cause physical damage by compromising their functionality or availability.  This research focuses on the low-cost Click C0-10DD1E-D PLC manufactured by Koyo Electronics Industries and sold by AutomationDirect.  Low-cost controllers used by organizations with budget constraints typically lack security features of their more expensive counterparts. Objectives of this research is to develop network-based attacks including:

  - Connect to the controller bypassing any authentication
  - Force the controller to be in stop cpu mode in order to prevent program execution
  - Manipulate the system time settings on the controller
  - Manipulate the network settings on the controller
  - Manipulate variable values in the controller's program
  - Create a denial of service that prevents any communication to the controller
  - Fuzz the controller to produce unexpected behavior
  - Download a blank program to the controller without the programming software 
  
Understanding the weaknesses of the Click C0-10DD1E-D PLC leads to a better understanding of how to reduce the risk of attacks. Successful attacks can be documented and reported to the vendor, Koyo, to assist them in improving the security of their product. Knowledge of potential attacks will assist current users of the controller to protect their assets.  Successful testing scripts may be integrated into a new SCADA security class being added at the University of Nebraska-Omaha's College of IS&T to train future security professionals.

## Proposed Project Timeline

![Alt text](/gantChart.PNG?raw=true "Project Timeline")

## Project-oriented Risk List

|Risk name (value)  | Impact     | Likelihood | Description |
|-------------------|------------|------------|-------------|
|Destruction of device firmware(16) | 8 | 2 | Device could be passed bad parameters that damages the firmware. Unknown at this time if it can be flashed with new firmware. |
| Electrocution(18) | 9 | 2 | A person could be severely injured or killed by incorrectly connecting the PLC. Caution must be taken before changing configuration on the device. |
| Power Surge(24) | 8 | 3 | Device could be destroyed with  a powersurge. We must ensure that the PLC is connected to the correct power supply and that the PLC is connected to a surge protector. |
| Dropping the device(24) | 8 | 3 | Device could be dropped and damaged. Mitigation is the design and building of some display to protect the device. |
| Theft of the PLC(32) | 8 | 4 | The device could be stolen if not secured. Mitigation controls include securing the device in the SCADA lab or in STEAL3. |


## Application Requirements

### User Stories
1. As a programmer/engineer, I want to set and send a password to authenicate and communicate securely.
  - Acceptance Criteria:
    - Password and subsequent data is encrypted in transit

2. As a programmer/engineer, I want to securely update hardware settings to fit changing network requirements.
  - Acceptance Criteria:
    - Controller authenticates requests to change hardware settings
    - Hardware settings data is encrypted during transmission

3. As a non-technical employee, I want to want to use an HMI or the programming software to interact with the program on the controller.
 - Acceptance Criteria:
    - Memory locations for variables are not writable by replaying commands.
    - Controller contains mechanisms to prevent denial of service.

4. As a non-technical employee, I want to put the controller cpu in run mode to for its programming to be executed.
  - Acceptance Criteria:  
    - Controller cpu mode cannot be manipulated.
  
5. As a programmer/engineer, I want to retrieve diagnostic and error data to troubleshoot problems.
 - Acceptance Criteria:
    - Controller contains mechanisms to prevent diagnostic and error log data manipulation.
  

### Use-Misuse Diagram
https://www.lucidchart.com/invitations/accept/c0173837-b4e0-4fa4-a2eb-2afb866eff68

## Resources/Technology Needed

|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|----------|------------------|---------------------------|-------------|
|Click C0-10DD1E-D PLC | No | Gary | The PLC that will be investigated |
|24v Power Cord | No | Gary | A cord to wire into the PLC to provide power |
|Click Programming Software | No | Gary | The programming software to configure and interact with the Click PLC |
|Click HMI Software| No | Gary | The HMI creation software to interact with the Click PLC |
|Windows 7 Virtual Machine | No | Gary | The virtual environment to host the programming software |
|Kali Linux Virtual Machine| No | Gary | The virtual environment from which to launch attack scripts |

## Trello Board
https://trello.com/b/l3p1jstX/project-requirement-elicitation

# Milestone 2

### Architectural Diagram
https://www.lucidchart.com/invitations/accept/d9a953e0-7dd6-427e-8d44-1d9d7f5d9fbf

### Activity Diagram
https://www.lucidchart.com/documents/edit/c4497c3b-4cea-4afe-941b-a1c6e8d6f948#

### User Story 1 Testing
#### Test Case: Secure Communication
[Report](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/secureCommunication.md)

[Test Script](https://github.com/groth001/Capstone/blob/master/test%20scripts/password.py)

### User Story 2 Testing
#### Test Case: Network Settings
[Report](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/Network%20Settings.md)

[Test Script](https://github.com/groth001/Capstone/blob/master/test%20scripts/changeip.py)

#### Test Case: Time Settings
[Report](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/Time%20Settings.md)

[Test Script](https://github.com/groth001/Capstone/blob/master/test%20scripts/changetime.py)

### User Story 3 Testing
#### Test Case: Memory Manipulation
[Report](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/Memory%20Manipulation.md)

[Test Script](https://github.com/groth001/Capstone/blob/master/test%20scripts/writecoil.py)


# Milestone 3

### [Activity Diagrams](https://www.lucidchart.com/documents/edit/c4497c3b-4cea-4afe-941b-a1c6e8d6f948#)

### User Story 4 Testing
#### Test Case: Stop CPU Flood Attack
[Report](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/denialOfService.md)

[Test Script](https://github.com/groth001/Capstone/blob/master/test%20scripts/cpumode.py)

### User Story 5 Testing
#### Test Case: Password Attempt Logging
[Report](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/LoggingMechanisms.md)

### Results
[Assessment & Threat Landscape Summaries](https://github.com/groth001/Capstone/blob/master/Results/Assessment%20Activities%20%26%20Threat%20Landscape.md)

[Assessment Findings](https://github.com/groth001/Capstone/blob/master/Results/Assessment%20Findings.md)

[Final Report](https://github.com/groth001/Capstone/blob/master/Results/Final%20Report.md)


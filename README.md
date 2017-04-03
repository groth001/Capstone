## Executive Summary

#### Problem Statement
Organizations use industrial control systems to automate processes that make their day-to-day operations possible.  The "brains" of these systems are programmable logic controllers, miniature computers, that run the programs to execute the processes.  Attacks are typically designed to target controllers to cause physical damage by compromising their functionality or availability.  This research focuses on the low-cost Click C0-10DD1E-D PLC manufactured by Koyo Electronics Industries and sold by AutomationDirect.  Low-cost controllers used by organizations with budget constraints typically lack security features of their more expensive counterparts. Objectives of this research is to develop network-based attacks including:

  - Connect to the controller bypassing any authentication
  - Force the controller to be in stop cpu mode in order to prevent program execution
  - Manipulate the system time settings on the controller
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
1. As a programmer/engineer, I want to remote access the controller to download a new program.
  - Acceptance Criteria:  
    - Controller authenicates requests to change programming. 
    - Intercepted traffic does not contain sensitive information and commands are not subject to replay attacks.
    - Controller contains mechanisms to prevent denial of service.

2. As a programmer/engineer, I want to securely update hardware settings to fit changing network requirements.
  - Acceptance Criteria:
    - Controller authenticates requests to change hardware settings
    - Hardware settings data is encrypted during transmission

3. As a programmer/engineer, I want to set and send a password to authenicate and communicate securely.
  - Acceptance Criteria:
    - Password and subsequent data is encrypted in transit
  
4. As a programmer/engineer, I want to retrieve diagnostic and error data to troubleshoot problems.
 - Acceptance Criteria:
    - Controller contains mechanisms to prevent diagnostic and error log data manipulation.
  
5. As a non-technical employee, I want to want to use an HMI to interact with the program on the controller.
 - Acceptance Criteria:
    - Memory locations for variables mapped to HMI components are not writable by replaying commands.
    - Controller contains mechanisms to prevent denial of service.

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

### User Story – Communicating Securely

#### Which components were tested in the architecture?
The communications between the PLC and the programing software is what was tested.

#### What was the purpose of the test?
The purpose of this test was to see if communication could be done securely. Without encryption and a password, any commands sent could likely be sniffed and replayed. This essentially means an attacker listening on the network could replay any command he has previously captured. While an attacker may not be able to run arbitrary commands, chances would be good at least one command captured could be used to launch a DoS attack.

#### Testing/Results
We conducted this test by first viewing the traffic without a password being set. We tried to see if these commands could be rep It was not encrypted, and commands could be replayed. This was true for both the custom protocol used to communicate between the PLC and the programming software, and Modbus. After we set a password, we looked at the traffic again, and it was still not encrypted. This time commands could no longer be replayed. While its certainly positive that commands were blocked after a password set, this was still easily circumventable.

We decided to see if we could find the password in the traffic between the controller and programming software. We were able to see the password in plaintext. We captured this packet, replayed it, and replayed our other commands, which then worked once again. After more digging into this, we realized that if you have multiple PLCs communicating, they cannot have passwords. If a PLC has a password and then receives a command, it ignores it. If someone builds out a system with multiple Click PLCs that need to communicate with each other, chances are good that at least some of them don’t have passwords.


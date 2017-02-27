
# PLC Hacking Capstone Project

<b>Executive Project Summary</b>

This project consists of developing attacks on a programmable logic controller, a device used to control a process in Supervisory Control and Data Acquistion (SCADA) systems. Research is being focused on a Click C0-10DD1E-D PLC with Ethernet sold by AutomationDirect. Intelligence reports in the past few years have indicated that attacks on SCADA systems are continuing to increase [1]. These systems represent functions of critical infrastructure for a nation that citizens directly depend on. The goal of these attacks is typically to cause physical damage by compromising the availability of the system. For example, on December 23, 2015, an attack on a Ukrainian power grid left around 225,000 residents without electricity, and call centers were flooded such that customers could not report the outages [2]. Understanding the weaknesses of SCADA equipment leads to a better understanding of how to reduce the risk of attacks. Any successful attacks and knowledge gained could be integrated into the new SCADA security class being added at the University of Nebraska-Omaha's College of IS&T to train future security professionals. Any serious vulnerabilities should be reported to the vendor.

References<br>
[1] https://securityintelligence.com/news/annual-threat-report-pos-https-and-scada-attacks-on-the-rise/ <br>
[2] https://ics-cert.us-cert.gov/alerts/IR-ALERT-H-16-056-01

<b>Proposed Project Timeline</b>
![Alt text](/gantChart.PNG?raw=true "Project Timeline")

<b>Project-oriented Risk List</b>

|Risk name (value)  | Impact     | Likelihood | Description |
|-------------------|------------|------------|-------------|
|Destruction of device firmware(16) | 8 | 2 | Device could be passed bad parameters have the software damaged. Unknown at this time if it can be flashed with new firmware. |
| Power Surge(24) | 8 | 3 | Device could be destroyed with  a powersurge. We must insure that the PLC is connected to the correct power supply and that the PLC is connected to a surge protector. |
| Dropping the device(24) | 8 | 3 | Device could be dropped and damaged. Mitigation is the design and building of some display to protect the device |
| Theft of the PLC(32) | 8 | 4 | the device could be stolen if not secured. Mitigation controls include securing the device in the SCADA lab or in STEAL3 |
| Electrocution(81) | 9 | 9 | A person could be severely injured or killed by incorrectly connecting the PLC. Caution must be taken before changing configuration on the device |

<b>Application Requirements</b>

- User Story 1<br>
  As a programmer/engineer, I want to remote access the controller to download a new program.<br>
  Acceptance Criteria: 

- User Story 2<br>
  As a programmer/engineer, I want to remote access the controller to update hardware settings.<br>
  Acceptance Criteria:

- User Story 3<br>
  As a programmer/engineer, I want to remote access the controller to update the system time.<br>
  Acceptance Criteria:
  
- User Story 4<br>
  As a maintenance technician, I want to have physical access to wire in new IO hardware.<br>
  Acceptance Criteria:
  
 - User Story 5<br>
   As a non-technical employee, I want to want to use an HMI to interact with the program on the controller.<br>
   Acceptance Criteria:

- Use-Misuse Diagram
https://www.lucidchart.com/invitations/accept/c0173837-b4e0-4fa4-a2eb-2afb866eff68

<b>Resources/Technology Needed</b>

|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|----------|------------------|---------------------------|-------------|
|Click C0-10DD1E-D PLC | No | Gary | The PLC that will be investigated. |
|24v Power Cord | No | Gary | A cord to wire into the PLC to provide power |
|Click Programming Software | No | Gary | The programming software to configure and interact with the Click PLC |
|Windows 7 Virtual Machine | No | Gary | The virtual environment to host the programming software |
|Kali Linux Virtual Machine| No | Gary | The virtual environment from which to launch attack scripts |

<b>Trello Board</b>

https://trello.com/b/l3p1jstX/project-requirement-elicitation

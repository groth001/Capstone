## Final Report: Koyo Click C0-10DD1E-D PLC

#### Executive Summary

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

#### Summary of Assessment Activities

Our assessment activities throughout the project revolved around our user stories for a Koyo Click C0-10DD1E-D Programmable Logic Controller. Our first user story was wanting to be able to securely communicate with and authenticate to the PLC. This is one of the most basic criteria for a modern networked system. We used Wireshark to examine data communicated between the PLC and programming software, and that data was unencrypted, and any passwords sent were in plain text. We later discovered that sending a certain packet will force the PLC to send the last entered password, which is extremely likely the be the correct one.

Our second user story requested the ability to securely change hardware settings. Since we had already broken the authentication mechanism, any user can change this. This sort of logic worked many of the remaining user stories as well. For example, since there is no longer a secure authentication mechanism, the third user story, which requests a secure way to change memory bits in order to turn I/O devices on or off, is also broken.

The fourth user story sought mechanisms to prevent a denial of service attack. With no authentication beyond a broken password mechanism, anyone can send a flood of packets forcing the PLC’s cpu into stop mode. In addition to preventing the execution of the program, the PLC is so busy responding to the flood that it cannot respond to any legitimate communication.

The final user story was seeking some sort of logging mechanism. The only logging mechanism on the PLC appears to be one that logs incorrect password attempts, but this only happens when an incorrect attempt is made from the programming software. Incorrect attempts sent programmatically are not logged.

#### Summary of Threat Landscape

The threat landscape on this PLC is difficult to accurately define. This PLC is extremely vulnerable, so describing the threat landscape is more of a matter of where and how these are used. The biggest threat is likely to be malicious insiders who know about the PLC. This is because these PLCs are likely not connected to critical infrastructure or internet facing. These insiders can either anonymously attack the PLC themselves, or tell others about the PLC. The PLC is easily discoverable by a broadcast message however, so any person on the internal network cannot be ruled out.

It then becomes a matter of what this is connected to. If its coffee machines or climate control for trucks, then the PLCs may not be on anyone’s list of targets. If it’s a somewhat realistic scenario of an elevator, then hacking the PLC may be able to cause physical harm to individuals.

#### Assessment Findings

|User Story  | Test Case | Description | Test Result |
|------------|-----------|-------------|-------------|
| 1. Secure Communication | [Password](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/secureCommunication.md) | Passwords should be encrypted in transit | Failed |
| 2. Hardware Configuration | [Network Settings](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/Network%20Settings.md) | The IP address should not be able to be manipulated | Failed |
| 2. Hardware Configuration | [Time Settings](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/Time%20Settings.md) | The PLC system time should not be able to be manipulated | Failed |
| 3. I/O Devices | [Memory Manipulation](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/Memory%20Manipulation.md) | Variables in memory should not be able to be maipulated to the status of an I/O device | Failed |
| 4. Denial of Service | [Stop CPU Flood](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/denialOfService.md) | The controller should have mechanisms to prevent a denial of service attack | Failed |
| 5. Logging Mechanisms | [Password Logging](https://github.com/groth001/Capstone/blob/master/Assessment%20Reports/LoggingMechanisms.md) | The controller should log all attempts to enter passwrods | Failed |

#### Artifacts

##### [Testing Scripts](https://github.com/groth001/Capstone/tree/master/test%20scripts)

##### [Architectural Diagram](https://www.lucidchart.com/invitations/accept/d9a953e0-7dd6-427e-8d44-1d9d7f5d9fbf)

##### [Activity Diagrams](https://www.lucidchart.com/documents/edit/c4497c3b-4cea-4afe-941b-a1c6e8d6f948#)

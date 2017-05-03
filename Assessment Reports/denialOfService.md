## User Story 4: Denial of Service

#### Component Focus
This assessment test focuses on the Click C0-10DD1E-D PLC's cpu mode.

#### Purpose
This assessment test checks to verify if it is possible to force the cpu to be in stop mode while preventing a legitmate user from returning it to run mode.

#### Test Procedure
A single Click C0-10DD1E-D PLC was installed on a private local area network within the University of Nebraska at Omaha’s Critical Infrastructure Lab via a Netgear 24-Port Hub.  The programming software for the controller, Click Programming Software V2.0, was installed on a VMware Fusion virtual machine running Windows 7 Professional.  Factory default network settings were replaced with an IP address of 192.168.0.101, a subnet mask of 255.255.255.0, and gateway of 192.168.0.244 to match the requirements for the LAN.  Wireshark was used to capture the commands to change the cpu mode to run and stop.  A Python script was written to replay the captured packets while a connected fan was running.  This was done similarly with and without a password on the controller.

#### Test Results
The run cpu and stop cpu commands consist of one packet each using the Click's custom communciations protocol.  With a password set on the controller, the packets were rejected.  After submitting the correct password (or with the password protection disabled), both the run cpu and stop cpu commands are executed when sent a Python script outside of the legitimate programming software.  Putting the cpu in stop mode prevents execution of the program and as such the fan turns off.  If the controller's cpu is put back into run mode, the fan immediately started running again.  This confirmed that the none of the variable values are lost upon the cpu being changed to stop mode.  The program was simply paused.  Replaying the stop cpu command packet on a continious loop prevented the controller from being returned to run mode.  While the stop cpu flood was in effect, the programming software showed a message that communication with the controller had been lost even while still connected.  The function in the programming to change the cpu mode was disabled.  The controller was so busy repsonding to the flood of stop cpu command packets that it could not respond to any packets being sent from the programming software.  A denial of service is created as long as the attacker can maintain the stop cpu flood.  Once the attack ended, normal functionality was restored to programming software.

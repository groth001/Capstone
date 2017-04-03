# Click C0-10DD1E-D PLC Security Assessment Report

#### Component Focus
Network settings

#### Purpose
This assessment test checks to verify if it is possible to manipulate the network settings on the controller including IP address, subnet mask, and gateway.

#### Test Procedure
A single Click C0-10DD1E-D PLC was installed on a private local area network within the University of Nebraska at Omaha’s Critical Infrastructure Lab via a Netgear 24-Port Hub.  The programming software for the controller, Click Programming Software V2.0, was installed on a VMware Fusion virtual machine running Windows 7 Professional.  Factory default network settings were replaced with an IP address of 192.168.0.101, a subnet mask of 255.255.255.0, and gateway of 192.168.0.244 to match the requirements for the LAN.  Wireshark was used to capture the commands required to edit these settings using the programming software with and without a password set on the controller.  A Python script was written to replay the captured packets to modify the network settings outside of the programming software.  This was done similarly with and without a password on the controller.

#### Test Results
Updating the network settings on a Click PLC requires two packets broadcasted to the entire local area network.  The packets use a custom communications protocol developed by Koyo which ride on top of UDP.  The first packet prepares the controller to receive the new settings, and the second contains the new settings. Without a password, previously captured packets that were replayed from a Python script were accepted by the PLC and the network settings were updated according per the data in the packet.  With a password set, these replayed packets were rejected.  It was noted that with a password set, a legitimate user also cannot change the network settings from the programming software.  Submitting the correct password from a Python script would not do an attacker any good in this instance.  

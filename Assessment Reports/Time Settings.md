Click C0-10DD1E-D PLC Security Assessment Report

Component Focus
Time settings

Purpose
This assessment test checks to verify if it is possible to manipulate the time settings on the controller.

Test Procedure
A single Click C0-10DD1E-D PLC was installed on a private local area network within the University of Nebraska at Omaha’s Critical Infrastructure Lab via a Netgear 24-Port Hub.  The programming software for the controller, Click Programming Software V2.0, was installed on a VMware Fusion virtual machine running Windows 7 Professional.  Factory default network settings were replaced with an IP address of 192.168.0.101, a subnet mask of 255.255.255.0, and gateway of 192.168.0.244 to match the requirements for the LAN.  Wireshark was used to capture the command required to edit the controller time using the programming software with and without a password set on the controller.  A Python script was written to replay the captured packets outside of the programming software.  This was done similarly with and without a password on the controller.

Test Results
Updating the time settings on a Click PLC requires a single packet sent directly to the controller.  The packet use a custom communications protocol developed by Koyo which ride on top of UDP.  The data must specify new values for the day of the week (Sunday, Monday, etc.), the month, day, year, hour, minutes, and seconds. Without a password, previously captured packets that were replayed from a Python script were accepted by the PLC and the time settings were updated according per the data in the packet.  The custom communications protocol has a two-byte security check that changes based on the data in the packet. These two bytes are not random, but are tied to the data within the packet. Without knowing how these two bytes are calculated, the attacker could still precapture the packets off of another controller before executing the attack.  With a password set, these replayed packets were rejected.  It was noted that with a password set, a legitimate user cannot view or change the time settings from the programming software.  Submitting the correct password from a Python script would not do an attacker any good in this instance.  

# Click C0-10DD1E-D PLC Security Assessment Report

### Component Focus
This assessment test focuses on controller memory.

### Purpose
This assessment test checks to verify if it is possible to manipulate the value of a ladder logic program variable stored in memory on the controller.

### Test Procedure
A single Click C0-10DD1E-D PLC was installed on a private local area network within the University of Nebraska at Omaha’s Critical Infrastructure Lab via a Netgear 24-Port Hub.  The programming software for the controller, Click Programming Software V2.0, was installed on a VMware Fusion virtual machine running Windows 7 Professional.  Factory default network settings were replaced with an IP address of 192.168.0.101, a subnet mask of 255.255.255.0, and gateway of 192.168.0.244 to match the requirements for the LAN.  A computer tower fan was wired into an output address on the controller.  The controller was then programmed with a simple ladder logic program in which a boolean variable stored in memory controlled whether the fan was turned on or off.  A Python script was written to send a packet to the controller using Modbus protocol to change the value of the variable controlling the fan.

### Test Results
Despite using a custom protocol  

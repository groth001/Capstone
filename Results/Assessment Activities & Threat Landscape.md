#### Summary of Assessment Activities

Our assessment activities throughout the project revolved around our user stories for a Koyo Click C0-10DD1E-D Programmable Logic Controller. Our first user story was wanting to be able to securely communicate with and authenticate to the PLC. This is one of the most basic criteria for a modern networked system. We used Wireshark to examine data communicated between the PLC and programming software, and that data was unencrypted, and any passwords sent were in plain text. We later discovered that sending a certain packet will force the PLC to send the last entered password, which is extremely likely the be the correct one.

Our second user story requested the ability to securely change hardware settings. Since we had already broken the authentication mechanism, any user can change this.  This sort of logic worked many of the remaining user stories as well. For example, since there is no longer a secure authentication mechanism, the third user story, which requests a secure way to change memory bits in order to turn I/O devices on or off, is also broken.

The fourth user story sought mechanisms to prevent a denial of service attack.  With no authentication beyond a broken password mechanism, anyone can send a flood of packets forcing the PLC’s cpu into stop mode.  In addition to preventing the execution of the program, the PLC is so busy responding to the flood that it cannot respond to any legitimate communication. 

The final user story was seeking some sort of logging mechanism. The only logging mechanism on the PLC appears to be one that logs incorrect password attempts, but this only happens when an incorrect attempt is made from the programming software. Incorrect attempts sent programmatically are not logged.

#### Summary of Threat Landscape

The threat landscape on this PLC is difficult to accurately define. This PLC is extremely vulnerable, so describing the threat landscape is more of a matter of where and how these are used. The biggest threat is likely to be malicious insiders who know about the PLC. This is because these PLCs are likely not connected to critical infrastructure or internet facing.  These insiders can either anonymously attack the PLC themselves, or tell others about the PLC. The PLC is easily discoverable by a broadcast message however, so any person on the internal network cannot be ruled out.

It then becomes a matter of what this is connected to. If its coffee machines or climate control for trucks, then the PLCs may not be on anyone’s list of targets. If it’s a somewhat realistic scenario of an elevator, then hacking the PLC may be able to cause physical harm to individuals.

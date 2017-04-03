## User Story – Communicating Securely

####  Which components were tested in the architecture?

The communications between the PLC and the programing software is what was tested.

#### What was the purpose of the test?

The purpose of this test was to see if communication could be done securely. Without encryption and a password, any commands sent could likely be sniffed and replayed. This essentially means an attacker listening on the network could replay any command he has previously captured. While an attacker may not be able to run arbitrary commands, chances would be good at least one command captured could be used to launch a DoS attack.

#### Testing/Results

We conducted this test by first viewing the traffic without a password being set. We tried to see if these commands could be rep It was not encrypted, and commands could be replayed. This was true for both the custom protocol used to communicate between the PLC and the programming software, and Modbus. After we set a password, we looked at the traffic again, and it was still not encrypted. This time commands could no longer be replayed. While its certainly positive that commands were blocked after a password set, this was still easily circumventable.

We decided to see if we could find the password in the traffic between the controller and programming software. We were able to see the password in plaintext whenever someone authenticated to it. We captured this packet, replayed it, and replayed our other commands, which then worked once again. We recognized that whenever someone did authenticate, the PLC would echo back the password entered. It turns out that this is the result of a PLC receiving a command that can be executed at any time. This means you do not have to sit and wait inside a network to obtain the password. It can be obtained at any time. 

After more digging more into passwords, we realized that if you have multiple PLCs communicating, they cannot have passwords. If a PLC has a password and then receives a modbus command, it ignores it. No functinoality for PLCs to authenticate to other PLCs is built in to the programming software. If someone builds out a system with multiple Click PLCs that need to communicate with each other, chances are good that at least some of them don’t have passwords.

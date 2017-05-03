## User Story 5: Logging Mechanisms

#### Which components were tested in the architecture?
The logging features available with the PLC and programming software are what were tested.

#### What was the purpose of the test?
The purpose of the test was to determine if we could identify an intrusion, based on an of the data the 
PLC logs.  

#### Testing Procedure 
The CLICK PLC has an option to log asswords. We enabled this setting through the programing 
software. We then ran a variety of tests on this logging mechanism. We tried to log in with correct and 
incorrect credentials both through the programming software and through python scripts. After 
completing these tasks, we checked the log data to see what was recorded. This appeared to be the only s
ecurity relevant logging mechanism, so no additional tests were conducted.

#### Testing Results
The logging mechanism only records the last sixteen incorrect passwords attempts. For each attempt, 
the time and the attempted password are shown. You can view this information even without entering 
the password in the programming software. This can potentially pose a problem if a user with the 
password mistypes that password while authenticating. In this case, if logging is enabled, anyone can 
connect to the PLC and view a string that is very similar to the password. This may allow them to guess 
the password without having to replay any commands. 

Incorrect attempts sent programmatically using the replay attack are not shown. This is likely because 
the programming software sends another command to the PLC when an incorrect password is entered. 
This script does not send this command. This is an issues as it makes brute force attempts impossible to 
detect from the PLC itself. 

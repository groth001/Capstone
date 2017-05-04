## Executive Summary

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


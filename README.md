# robot

EXERCISE
1. Using Robot Framework create a set of tests to validate the UE manager application. Tests
should check the following actions:
a. attach
b. detach
c. start traffic
d. stop traffic
Example test should contain:
- Attach UE
- Verify if the UE is attached
You should use commands from UE manager app to attach and check the status of UEs.
2. UE manager application is available online: pk-robot.ddns.net:PORT where PORT is[8000, 8009];
3. To connect and interact with the application you can use python/robot libraries:
- telnetlib
- socket
4. Create resource files – for robot/python keywords, variables etc.
Hints:
- To decode/encode responses from application you can use string.decode()/encode()
methods
- If you want to check application out, test it manually try using putty with connection type
set to Telnet. Example output: 
## Lab 1.1 - Environment Orientation
#### Objectives
1. Understand the lab environment for the course
2. Preview labs for the course
3. VM review
### Lab Environment 
This course will stress the importance of redirecting traffic from the target environment to our command-and-control servers.
- Although we are attached to the target environment via the VPN, we want to ensure we logically separate the assets belonging to the target (red space) from our redirectors in our attack infrastructure (gray space) and our C2 servers and VMs (blue space).

- Red space encompasses anything owned by the target.
- Gray space is anything that is owned by a 3rd party like redirectors in our attack infrastructure  and not associated with the target nor the Red Team.
- Blue space is anything that is owned/registered to the Red Team, any friendly assets like VMs and C2 servers.
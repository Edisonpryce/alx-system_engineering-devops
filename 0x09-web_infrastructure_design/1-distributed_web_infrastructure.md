Description
This is a web infrastructure designed to to reduce the traffic of the primary server by sharing some of the load to a replica server with the aid of a load balancer(haproxy).

This infrastructure specifics
. Why add load balancer(HAPROXY)?
I added a load balancer to reduce the work load of the primary server and share it wit the replica. In this challenge Haproxy is used to do this task.

. Why add another server?
The server added is a replica server that is designed to accept some of the trafics directed to it from the load balancer.

. What distribution algorithm your load balancer is configured with and how it works?
The Haproxy load balancer can be configured to different algorithm depending on the developer. Each algorithm has its advantages. I worked with Round Robin distribution algorithm. The algorithm works by using each server in turns, matching towards equal distibution

. Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. In an Active-Active setup, the load balancer distributes workloads across all nodes in order to prevent any single node from getting overloaded. Because there are more nodes available to serve, there will also be a marked improvement in throughput and response times. On the other hand, in an Active-Passive setup, not all nodes are going to be active (capable of receiving workloads at all times). In the case of two nodes, for example, if the first node is already active, the second node must be passive or on standby. The second or the next passive node can become an active node if the preceding node is inactive.

. How a database Primary-Replica (Master-Slave) cluster works
A Primary-Replica setup configures one server to act as the Primary server and the other server to act as a Replica of the Primary server. However, the Primary server is capable of performing read/write requests whilst the Replica server is only capable of performing read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.

. What is the difference between the Primary node and the Replica node in regard to the application
The Primary node is responsible for all the write operations the site needs whilst the Replica node is capable of processing read operations, which decreases the read traffic to the Primary node.

Where are SPOF
There are multiple SPOF in the infrastructure. Example can be the Primary MySQL database server. Since we are running a Primary-Replica cluster works when the server(primary) is down, the entire site would be unable to make changes to the site.
The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.

Security issues (no firewall, no HTTPS)
Hackers can spy on the network been transmitted over the network because it is not encrypted using the SSL certificate. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.

No monitoring.
We have no way of knowing the status of each server since they're not being monitored.

Introduction
The simple web stack focus on a simple web infracture of a single server. The website www.foobar.com has no firewalls or SSL certificates for protecting the servers network. I designed this project in such a way that, the web server(nginx), the application server and the database ( mysql) share the same resources. In other words i used my local machine as the server. And my local machine is running on the linux OS.


This infrastructure specifics
. What is a server?
    A server can be a computer hardware or software that provides services to other computers, which are usally referred to as clients/users.

. The role of the domain name.
    The domain name, in this challenge www.foobar.com, can be describe as the human representative name for an assinged IP address(eg. 8.8.8.8). The Domain Name System(DNS) is responsible for the mapping.

. The type of DNS record www is in www.foobar.com
    www can be classified as a subdomain and can also be classified under CNAME records. CNAME records are eventually matched to A or (AAAA) records where host names (fooobar.com) are mapped to the IP address, either IPV4 or IPV6. it can also be classifed under A records directory it all depends on the configuration.

. The role of the web server.
    The web server is a software(nginx)/hardware that accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error messsage.

. The role of the application server.
    To install, operate and host applications and associated services for end users, IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications

. The role of the database.
    To maintain a collection of organized information that can easily be accessed, managed and updated

. What the server uses to communicate with the client (computer of the user requesting the website).
    TCP/IP protocol suite is responsible for the communication between the client and the server over the internet network.




Issues With This Infrastructure
. There are number of SPOF (Single Point Of Failure) in this simple web stack infrastructure.
Like, if the Application server/MySQL database server is down, the entire site would be down.

. Downtime when maintenance needed.
When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.
Downtime when maintenace needed on any component is highly possible due to the limitation with available components. In some cases servers may have to be shutdown or restarted to deploy some changes.

. Cannot scale if there's too much incoming traffic.
The server would be hard to scale looking at the components the application is runnning on, in this case single server. When there is high traffic the server can easily run out of resources and can eventually shutdown or slow down.


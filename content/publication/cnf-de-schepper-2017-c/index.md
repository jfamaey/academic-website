---
title: "A transparent load balancing algorithm for heterogeneous local area networks"
date: 2017-01-01
publishDate: 2020-07-18T15:35:17.642943Z
authors: ["Tom De Schepper", "Steven Latré", "Jeroen Famaey"]
publication_types: ["1"]
abstract: "Today's local area networks (LANs) consist of a plethora of heterogeneous consumer devices, equipped with the ability to connect to the Internet using a variety of different network technologies (e.g., Ethernet, Power-Line, 2.4 and 5GHz Wi-Fi). Nevertheless, devices generally opt to statically connect using a single technology, based on predefined priorities. This static behaviour does not allow the network to unlock its full potential, which becomes increasingly more important as the requirements of services, in terms of latency and throughput, grow. To address this issue, we present a load balancing algorithm that dynamically selects a suitable interface and path through the network for each flow, based on service requirements, bandwidth availability and current link quality. The goal of the algorithm is to find an optimal path configuration for all the flows across the network that maximizes the global throughput. It dynamically adapts to changing network conditions, the arrival and departure of flows and link failures. The problem is formulated as a Mixed Integer Linear Program (MILP) and its solution, as well as that of a faster heuristic algorithm, is extensively tested in a series of ns-3 simulations with different network topologies and flow configurations. We differentiate from existing work by estimating flow rates and dynamic network conditions using real-time monitoring information, taking into account the shared medium of wireless networks and the specific fairness behaviour of TCP. Results show an increase in throughput up to 70% in heterogeneous LANs under dynamic network conditions."
featured: false
publication: "*IFIP/IEEE International Symposium on Integrated Network Management*"
doi: "10.23919/INM.2017.7987276"
---


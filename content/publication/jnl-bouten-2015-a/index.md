---
title: "QoE-driven in-network optimization for Adaptive Video Streaming based on packet sampling measurements"
date: 2015-04-22
publishDate: 2020-07-18T15:35:17.573905Z
authors: ["Niels Bouten", "Ricardo de O Schmidt", "Jeroen Famaey", "Steven Latré", "Aiko Pras", "Filip De Turck"]
publication_types: ["2"]
abstract: "HTTP Adaptive Streaming (HAS) is becoming the de-facto standard for adaptive streaming solutions. In HAS, a video is temporally split into segments which are encoded at different quality rates. The client can then autonomously decide, based on the current buffer filling and network conditions, which quality representation it will download. Each of these players strives to optimize their individual quality, which leads to bandwidth competition, causing quality oscillations and buffer starvations. This article proposes a solution to alleviate these problems by deploying in-network quality optimization agents, which monitor the available throughput using sampling-based measurement techniques and optimize the quality of each client, based on a HAS Quality of Experience (QoE) metric. This in-network optimization is achieved by solving a linear optimization problem both using centralized as well as distributed algorithms. The proposed hybrid QoE-driven approach allows the client to take into account the in-network decisions during the rate adaptation process, while still keeping the ability to react to sudden bandwidth fluctuations in the local network. The proposed approach allows improving existing autonomous quality selection heuristics by at least 30%, while outperforming an in-network approach using purely bitrate-driven optimization by up to 19%."
featured: false
publication: "*Computer Networks*"
doi: "10.1016/j.comnet.2015.02.007"
---

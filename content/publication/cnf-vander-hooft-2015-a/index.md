---
title: "A Learning-Based Algorithm for Improved Bandwidth Awareness of Adaptive Streaming Clients"
date: 2015-05-11
publishDate: 2020-07-18T15:35:17.658553Z
authors: ["Jeroen van der Hooft", "Stefano Petrangeli", "Maxim Claeys", "Jeroen Famaey", "Filip De Turck"]
publication_types: ["1"]
abstract: "HTTP Adaptive Streaming (HAS) is becoming the de-facto standard for Over-The-Top video streaming. A HAS video consists of multiple segments, encoded at multiple quality levels. Allowing the client to select the quality level for every segment, a smoother playback and a higher Quality of Experience (QoE) can be perceived. Although results are promising, current quality selection heuristics are generally hard coded. Fixed parameter values are used to provide an acceptable QoE under all circumstances, resulting in suboptimal solutions. Furthermore, many commercial HAS implementations focus on a video-on-demand scenario, where a large buffer size is used to avoid play-out freezes. When the focus is on a live TV scenario however, a low buffer size is typically preferred, as the video play-out delay should be as low as possible. Hard coded implementations using a fixed buffer size are not capable of dealing with both scenarios. In this paper, the concept of reinforcement learning is introduced at client side, allowing to adaptively change the parameter configuration for existing rate adaptation heuristics. Bandwidth characteristics are taken into account in the decision process, thus allowing to improve the client's bandwidth-awareness. Focus in this paper is on actively reducing the average buffer filling, evaluating results for two heuristics: the Microsoft IIS Smooth Streaming heuristic and the QoE-driven Rate Adaptation Heuristic for Adaptive video Streaming by Petrangeli et al. We show that using the proposed learning-based approach, the average buffer filling can be reduced by 8.3% compared to state of the art, while achieving a comparable level of QoE."
featured: false
publication: "*In proceedings of the 14th IFIP/IEEE International Symposium on Integrated Network Management (IM)*"
doi: "10.1109/INM.2015.7140285"
---

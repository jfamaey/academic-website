---
title: "Multi-objective surrogate modeling for real-time energy-efficient station grouping in IEEE 802.11ah"
date: 2019-07-01
publishDate: 2020-07-18T15:35:17.542653Z
authors: ["Le Tian", "Michael Mehari", "Serena Santi", "Steven Latré", "Eli De Poorter", "Jeroen Famaey"]
publication_types: ["2"]
abstract: "The Restricted Access Window (RAW) mechanism proposed by IEEE 802.11ah promises to address one of the major problems of the Internet of Things (IoT): high channel contention in large-scale densely deployed sensor networks. The RAW feature allows the Access Point (AP) to divide stations into different groups, with only the stations in the same group being allowed to access the channel simultaneously. Existing station grouping strategies only support homogeneous scenarios, where all sensor stations have the same fixed data transmission interval, modulation and coding scheme (MCS) and packet size. In this paper, we present two contributions to address this issue. First, we propose a surrogate modeling methodology to predict RAW performance for both throughput and energy efficiency given specific network conditions and RAW configuration parameters. The models are fast to train and can be solved in real-time. Second, we extend the original version of Model-Based RAW Optimization Algorithm (MoROA) which only focused on throughput. The extended MoROA uses the surrogate models to determine the optimal RAW configuration for both throughput and energy efficiency in real-time through multi-objective optimization. We compare the accuracy of our surrogate model to simulation results. Performance of MoROA is compared to existing RAW optimization algorithms and traditional 802.11 channel access methods. The results show that the trained surrogate models can accurately predict RAW performance with a relative error less than 7% and 10% for 90% and 95% of the RAW configurations respectively. Compare to the traditional 802.11 channel access functions, by using the objective weight and assigning stations into homogeneous groups, MoROA achieves either 65% higher throughput, or 96% less energy consumption, or a weighted solution in between, in dense heterogeneous networks."
featured: false
publication: "*Pervasive and Mobile Computing*"
doi: "10.1016/j.pmcj.2019.04.007"
---


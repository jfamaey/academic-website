---
title: "Regression-based Estimation of Individual Errors in Fingerprinting Localization"
date: 2019-03-08
publishDate: 2020-07-18T15:35:17.542653Z
authors: ["Filip Lemic", "Vlado Handziski", "Michiel Aernouts", "Thomas Janssen", "Rafael Berkvens", "Adam Wolisz", "Jeroen Famaey"]
publication_types: ["2"]
abstract: "Practical location estimation is never ideal, and each location estimate is burdened with a certain level of error. In many use-case scenarios, knowing the magnitude of these errors can significantly improve the usability of the location estimates. The localization errors for different localization approaches are currently assessed using static performance benchmarks. These benchmarks typically provide aggregate metrics that statistically characterize the localization errors across the entire deployment environment. Due to the potentially dynamic nature and spatial heterogeneity of the environment, this characterization can be too generic to be really useful from the point of view of an individual location estimate. To address this issue for fingerprinting-based localization, we propose a regression-based procedure for estimating the individual (i.e., per-location estimate) localization errors. We use the received signal strength (RSS) values from various locations in an environment, as well as the observed localization errors in case the location estimates are generated using these RSS values, for training a number of contemporary regression models. Using the trained models, we are able to estimate the localization error of a location estimate at a new location using only RSS values collected at that location. Both by simulation and experimentally, we demonstrate the feasibility of the proposed procedure for Wi-Fi-based indoor and LoRa- and SigFox-based outdoor fingerprinting approaches. We do that by showing that the proposed procedure can, in the best-case scenario, yield more than 50% more accurate estimation than the reference procedure based on the average localization errors derived from the static performance benchmarks."
featured: false
publication: "*IEEE Access*"
doi: "10.1109/ACCESS.2019.2903880"
---


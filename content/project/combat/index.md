---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "COMBAT"
summary: "Energy-aware computing on battery-less IoT devices (UA IOF, 2020-2021)"
authors: []
tags: ["Current"]
categories: []
date: 2020-07-13T18:04:52+02:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---
*Title:* Energy-aware computing on battery-less IoT devices
*Funding:* University of Antwerp (UA) Industry Research Fund (IOF)
*Start date:* January 1, 2020
*Project duration:* 2 years

The Internet of Things (IoT) is largely powered by batteries. This poses significant challenges for its sustainability and longevity, as batteries are short-lived, bulky and polluting. To overcome this problem, we posit the vision of a battery-less IoT network, where devices are powered by energy harvesting and tiny long-lived capacitors. However, such devices often run out of power, resulting in intermittent on-off behavior. Traditional static sequential applications cannot handle such behavior, as they lose forward progress. This problem can be solved with task-based applications, consisting of a chain of interconnected tasks. Each task performs some atomic function, and its output is saved in non-volatile memory after it successfully completes. This allows the application to ensure forward progress in face of frequent power failures. Optimally scheduling the execution of such tasks, in face of the specific behavior of various energy harvesters, as well as the capacitor, and given extremely constrained resources of battery-less devices, is non-trivial. In this project, we propose a novel task scheduler that takes these aspects, as well as the deadline of tasks into account.
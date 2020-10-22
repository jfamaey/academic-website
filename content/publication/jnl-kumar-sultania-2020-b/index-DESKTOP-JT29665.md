---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Enabling Low-Latency Bluetooth Low Energy on Energy Harvesting Batteryless Devices Using Wake-Up Radios"
authors: ["Ashish Kumar Sultania", "Carmen Delgado", "Jeroen Famaey"]
date: 2020-09-10
doi: "10.3390/s20185196"

# Schedule page publish date (NOT publication's date).
publishDate: 2020-09-14T09:11:12+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "*MDPI Sensors*"
publication_short: ""

abstract: "With the growth of the number of IoT devices, the need for changing batteries is becoming cumbersome and has a significant environmental impact. Therefore, batteryless and maintenance-free IoT solutions have emerged, where energy is harvested from the ambient environment. Energy harvesting is relevant mainly for the devices that have a low energy consumption in the range of thousands of micro-watts. Bluetooth Low Energy (BLE) is one of the most popular technologies and is highly suitable for such batteryless energy harvesting devices. Specifically, the BLE friendship feature allows a Low Power Node (LPN) to sleep most of the time. An associated friend node (FN) temporarily stores the LPN’s incoming data packets. The LPN wakes up and polls periodically to its FN retrieving the stored data. Unfortunately, the LPNs typically experience high downlink (DL) latency. To resolve the latency issue, we propose combining the batteryless LPN with a secondary ultra-low-power wake-up radio (WuR), which enables it to always listen for an incoming wake-up signal (WuS). The WuR allows the FN to notify the LPN when new DL data is available by sending a WuS. This removes the need for frequent polling by the LPN, and thus saves the little valuable energy available to the batteryless LPN. In this article, we compare the standard BLE duty-cycle based polling and WuR-based data communication between an FN and a batteryless energy-harvesting LPN. This study allows optimising the LPN configuration (such as capacitor size, polling interval) based on the packet arrival rate, desired packet delivery ratio and DL latency at different harvesting powers. The result shows that WuR-based communication performs best for high harvesting power (400 μW and above) and supports Poisson packet arrival rates as low as 1 s with maximum PDR using a capacitor of 50 mF or more."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

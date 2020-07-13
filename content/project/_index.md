---
title: Projects

# View.
#   1 = List
#   2 = Compact
#   3 = Card
#   4 = Citation
view: 2

 # Filter toolbar (optional).
  # Add or remove as many filters (`[[content.filter_button]]` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove toolbar, delete/comment all instances of `[[content.filter_button]]` below.
  
  # Default filter index (e.g. 0 corresponds to the first `[[filter_button]]` instance below).
  filter_default = 0
  
   [[content.filter_button]]
     name = "All"
     tag = "*"
  
   [[content.filter_button]]
     name = "Current"
     tag = "Current Projects"
  
   [[content.filter_button]]
     name = "Past"
     tag = "Past Projects"

# Optional header image (relative to `static/img/` folder).
header:
  caption: ""
  image: ""
---

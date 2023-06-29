graph [
  node [
    id 0
    label "1"
    IP "127.0.0.1"
    sites "_networkx_list_start"
    sites "https://www.youtube.com/"
  ]
  node [
    id 1
    label "2"
    IP "127.0.0.2"
    sites "_networkx_list_start"
    sites "https://www.facebook.com/"
  ]
  node [
    id 2
    label "3"
    IP "127.0.0.3"
    sites "_networkx_list_start"
    sites "https://www.figma.com/"
  ]
  node [
    id 3
    label "4"
    IP "127.0.0.4"
    sites "_networkx_list_start"
    sites "https://www.youtube.com/"
  ]
  node [
    id 4
    label "5"
    IP "127.0.0.5"
    sites "_networkx_list_start"
    sites "https://www.facebook.com/"
  ]
  node [
    id 5
    label "6"
    IP "127.0.0.6"
    sites "_networkx_list_start"
    sites "https://www.figma.com/"
  ]
  node [
    id 6
    label "7"
    IP "127.0.0.7"
    sites "https://www.youtube.com/"
    sites "https://www.figma.com/"
    sites "https://www.facebook.com/"
  ]
  edge [
    source 0
    target 1
    vitesse 1.5
  ]
  edge [
    source 0
    target 2
    vitesse 2
  ]
  edge [
    source 1
    target 3
    vitesse 5
  ]
  edge [
    source 1
    target 4
    vitesse 3
  ]
  edge [
    source 2
    target 3
    vitesse 4
  ]
  edge [
    source 2
    target 5
    vitesse 2.1
  ]
  edge [
    source 3
    target 4
    vitesse 1
  ]
  edge [
    source 3
    target 5
    vitesse 2
  ]
  edge [
    source 4
    target 6
    vitesse 0.5
  ]
  edge [
    source 5
    target 6
    vitesse 0.4
  ]
]

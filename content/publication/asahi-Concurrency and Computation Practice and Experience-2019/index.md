---
title: "Overlapping communications in gyrokinetic codes on accelerator\u2010based\
  \ platforms"
subtitle: ''
summary: ''
authors:
- Yuuichi Asahi
- Guillaume Latu
- Julien Bigot
- S. Maeyama
- V. Grandgirard
- Yasuhiro Idomura
tags: []
categories: []
date: '2019-11-22'
lastmod: '2025-09-18T15:25:29.206231'
featured: false
draft: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
publishDate: '2025-09-18T15:25:29.206235'
publication_types:
- '1'
abstract: "Summary Communication and computation overlapping techniques have been\
  \ introduced in the five\u2010dimensional gyrokinetic codes GYSELA GKV. In order\
  \ to anticipate some of exa\u2010scale requirements, these were ported modern accelerators,\
  \ Xeon Phi KNL Tesla P 100 GPU. On a serial version on GKV GPU are respectively\
  \ 1.3\xD7 7.4\xD7 faster than those single Skylake processor (a socket). For scalability,\
  \ we measured performance from 16 512 KNLs (1024 32k cores) 32 256 GPUs. their parallel\
  \ versions, transpose communication semi\u2010Lagrangian solver or Convolution kernel\
  \ turned out be main bottleneck. This indicates that exa\u2010scale, network constraints\
  \ would critical. mitigate costs, pipeline task\u2010based implemented codes. The\
  \ 2D advection has achieved 33% 92% speed up, convolution factor 2 up with pipelining.\
  \ approach gives 11% 82% gain derivative electrostatic potential GYSELA. We shown\
  \ pipeline\u2010based is applicable presence symmetry, while can more general situations."
publication: Concurrency and Computation Practice and Experience
doi: https://doi.org/10.1002/cpe.5551
---

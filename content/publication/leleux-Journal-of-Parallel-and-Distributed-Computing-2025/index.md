---
title: Complexity analysis and scalability of a matrix-free extrapolated geometric
  multigrid solver for curvilinear coordinates representations from fusion plasma
  applications
subtitle: ''
summary: ''
authors:
- Philippe Leleux
- Christina Schwarz
- "Martin J. K\xFChn"
- Carola Kruse
- "Ulrich R\xFCde"
tags: []
categories: []
date: '2025-07-03'
lastmod: '2026-05-01T06:19:06.688430'
featured: false
draft: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
publishDate: '2026-05-01T06:19:06.688436'
publication_types:
- '1'
abstract: Tokamak fusion reactors are promising alternatives for future energy production.
  Gyrokinetic simulations important tools to understand physical processes inside
  tokamaks and improve the design of plants. In gyrokinetic codes such as Gysela,
  these involve at each time step solution a Poisson equation defined on disk-like
  cross sections. The authors [KKR21,KKR22] proposed discretize simplified differential
  using symmetric finite differences derived from resulting functional use an implicitly
  extrapolated geometric multigrid scheme tailored problems in curvilinear coordinates.
  &#13;\nIn this article, we extend discretization more realistic partial demonstrate
  optimal linear complexity solver, terms computation memory. We provide general framework
  analyze flops memory usage matrix-free approaches stencil-based operators. Finally,
  give efficient implementation fo considered solver exploiting task-based multithreaded
  parallelism which takes advantage disk-shaped geometry problem.&#13;\nWe parallel
  efficiency size up 50 million unknowns.
publication: Journal of Parallel and Distributed Computing
doi: https://doi.org/10.1016/j.jpdc.2025.105143
---

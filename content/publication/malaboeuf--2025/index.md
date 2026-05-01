---
title: Porting a Fortran plasma simulation to Exascale on AMD GPUs using both OpenMP
  and Kokkos
subtitle: ''
summary: ''
authors:
- Etienne Malaboeuf
- Kevin Obrejan
- Mathieu Peybernes
- Julien Bigot
- Emily Bourne
- Virginie Grandgirard
tags: []
categories: []
date: '2025-11-07'
lastmod: '2026-05-01T06:19:06.690173'
featured: false
draft: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
publishDate: '2026-05-01T06:19:06.690177'
publication_types:
- '1'
abstract: "This paper presents the 2-step work undertaken to port Gysela, a petascale\
  \ Fortran simulation code for turbulence in tokamak plasmas, GPUs. The initial porting\
  \ process using OpenMP offloading allowed good performance most of with speedups\
  \ ranging from \xD7 1 12.5, exception collision operator, which became major bottleneck.\
  \ critical operator was then rewritten C++ Kokkos. new version is known as KoLiOp,\
  \ and one modules largest relative CPU baseline. We explain our strategy both phases\
  \ development provide an in-depth analysis how we leveraged each framework overall\
  \ performance. techniques detailed are applicable other codes seeking use portability\
  \ layer. Finally, present comparative benchmark run on (AMD Genoa), GPU (MI250X)\
  \ APU (MI300A) partitions Adastra machine."
publication: ''
doi: https://doi.org/10.1145/3731599.3768148
---

---
title: 'Gyselalib++: A Portable C++ Library for Semi-Lagrangian Kinetic and Gyrokinetic
  Simulations'
subtitle: ''
summary: ''
authors:
- Emily Bourne
- Virginie Grandgirard
- Yuuichi Asahi
- Julien Bigot
- Peter Donnel
- Alexander Hoffmann
- Abdelhadi Kara
- Philipp Krah
- Baptiste Legouix
- Etienne Malaboeuf
- Yann Munschy
- Kevin Obrejan
- Thomas Padioleau
- Matthieu Protais
- Pauline Vidal
tags: []
categories: []
date: '2025-09-09'
lastmod: '2026-01-13T19:09:24.365025'
featured: false
draft: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
publishDate: '2026-01-13T19:09:24.365053'
publication_types:
- '1'
abstract: "Gyselalib++ provides the mathematical building blocks to construct kinetic\
  \ or gyrokinetic plasma simulation codes in C++, simulating a distribution function\
  \ discretised phase space on fixed grid. It relies Discrete Domain Computation (DDC)\
  \ library (Padioleau et al., 2025) statically type discretisation dimensions, thus\
  \ preventing many common sources of errors. Via DDC, also leverages Kokkos framework\
  \ (Trott 2022), ensuring performance portability across various CPU and GPU architectures.\
  \ The variety tools including semi-Lagrangian advection operators, quadrature rules,\
  \ solvers for elliptic hyperbolic partial differential equations (PDEs). majority\
  \ operators are designed work non-orthonormal coordinate systems; those that don\u2019\
  t use static typing raise compiler errors their misuse."
publication: The Journal of Open Source Software
doi: https://doi.org/10.21105/joss.08582
---

---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Gyrokinetic Semi-Lagrangian Parallel Simulation using a Hybrid OpenMP/MPI programming
subtitle: ''
summary: ''
authors:
- G. Latu
- N. Crouseilles
- Virginie Grandgirard
- Eric Sonnendrücker
tags: []
categories: []
date: '2007-01-01'
lastmod: 2021-03-18T23:39:19+01:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2021-03-18T22:39:19.572065Z'
publication_types:
- '1'
abstract: This paper describes a parallel implementation of a numerical solver for
  the Vlasov equation. The solver is based on a kinetic model describing the motion
  of charged particles in a plasma. The evolution of the distribution of particles
  in phase space is computed with an explicit method, and we take into account the
  self-consistent electric field through the coupling with a Poisson type equation.
  In this paper, we focus on a recently developed 5D parallel numerical application
  dedicated to gyrokinetic simulation of tokamak systems and ITG turbulence simulation.
  A semi-Lagrangian Vlasov solver is used. A specific cubic spline interpolation allows
  us to formulate a domain decomposition method. A hybrid MPI/OpenMP paradigm was
  used to benefit from a large number of processors while reducing communication costs.
publication: '*Recent Advances in Parallel Virtual Machine and Message Passing Interface*'
url_pdf: http://hal.archives-ouvertes.fr/hal-00605748
doi: '10.1007/978-3-540-75416-9 '
---

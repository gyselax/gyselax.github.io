---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Scalable Quasineutral solver for gyrokinetic simulation
subtitle: ''
summary: ''
authors:
- Guillaume Latu
- Virginie Grandgirard
- Nicolas Crouseilles
- Guilhem Dif-Pradalier
tags:
- '"Quasineutrality solver"'
- '"Gyrokinetics"'
- '"MPI"'
- '"OpenMP"'
categories: []
date: '2012-05-01'
lastmod: 2021-03-18T23:39:18+01:00
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
publishDate: '2021-03-18T22:39:18.194191Z'
publication_types:
- '4'
abstract: 'Modeling turbulent transport is a major goal in order to predict confinement
  issues in a tokamak plasma. The gyrokinetic framework considers a computational
  domain in five dimensions to look at kinetic issues in a plasma. Gyrokinetic simulations
  lead to huge computational needs. Up to now, the gyrokinetic code GYSELA performed
  large simulations using a few thousands of cores. The work proposed here improves
  GYSELA onto two points: memory scalability and execution time. The new solution
  allows the GYSELA code to scale well up to 64k cores.'
publication: ''
url_pdf: http://hal.inria.fr/inria-00590561
---

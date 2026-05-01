---
title: Contributions to the Optimization of a Hierarchical Parallel Pattern on GPU
  for Performance, Portability, and Productivity
subtitle: ''
summary: ''
authors:
- Aymeric Millan
tags: []
categories: []
date: '2025-11-13'
lastmod: '2026-05-01T06:19:06.713142'
featured: false
draft: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
publishDate: '2026-05-01T06:19:06.713146'
publication_types:
- '1'
abstract: "Contributions \xE0 l'optimisation d'un motif algorithmique parall\xE8le\
  \ hi\xE9rarchique sur GPU pour la performance, portabilit\xE9 et productivit\xE9\
  \ Cette th\xE8se s'inscrit dans le contexte du calcul haute performance (HPC) l'\xE8\
  re de l'exascale, o\xF9 les supercalculateurs reposent des architectures h\xE9t\xE9\
  rog\xE8nes domin\xE9es par GPU. Le d\xE9fi majeur est concilier (les \xAB 3P \xBB\
  ) d\xE9veloppement d'applications scientifiques, sans sacrifier g\xE9n\xE9ricit\xE9\
  \ ni durabilit\xE9 code.Nous identifions un r\xE9current bas\xE9 parall\xE9lisme\
  \ avec allocations m\xE9moire, d\xE9fini comme Batched Kernels with Memory Allocations\
  \ (BKMA). Ce appara\xEEt nombreux contextes, allant simulation num\xE9rique l'inf\xE9\
  rence mod\xE8les d'intelligence artificielle. L'objectif proposer une impl\xE9mentation\
  \ r\xE9utilisable, performante portable, dot\xE9e d'une API productive ind\xE9pendante\
  \ d\xE9tails mat\xE9riels ou applicatifs, afin simplifier exascale.Notre approche\
  \ repose C++ moderne mod\xE8le programmation SYCL, qui permet code unique plusieurs\
  \ architectures. Apr\xE8s avoir analys\xE9 constructions parall\xE8les SYCL leurs\
  \ limites BKMA, nous introduisons optimisations exploitant propri\xE9t\xE9s mat\xE9\
  rielles certaines hypoth\xE8ses algorithmiques. Une contribution directe au standard\
  \ \xE9galement propos\xE9e, renfor\xE7ant pertinence ce travail communaut\xE9 HPC\
  \ ouvrant voie adoption large.Nous m\xE9thode originale d'\xE9valuation simplicit\xE9\
  \ d'utilisation (``productivit\xE9''), comparer objectivement notre proposition\
  \ approches existantes. La validation s'appuie exp\xE9riences concr\xE8tes, incluant\
  \ l'advection semi-lagrangienne l'application GYSELA noyau convolution 1D, compar\xE9\
  s aux impl\xE9mentations PyTorch oneDNN, d\xE9montrant fois approche.En conclusion,\
  \ cette apporte contributions m\xE9thodologiques techniques conception biblioth\xE8\
  ques g\xE9n\xE9riques durables en HPC."
publication: ''
doi: https://doi.org/10.70675/f61695aaz92f6z4d79z8432zc947a3b37264
---

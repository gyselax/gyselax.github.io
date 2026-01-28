---
widget: blank
weight: 20
headless: true
design:
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns: '1'
---

The **Gysela-X** project consists in the development of a series of gyrokinetic codes with the main aim to allow exascale simulations of tokamak plasma turbulence and transport including a X-point geometry.

The legacy Fortran code **GYSELA** (for GYrokinetic SEmi-LAgrangian)[^1] has been developed at [CEA/IRFM](http://irfm.cea.fr/) for over 20 years through national and international collaborations with a strong interaction between physicists, mathematicians and computer scientists. It is a global full-f nonlinear gyrokinetic code that simulates plasma turbulence and transport in the core of Tokamak devices, including electromagnetic effects. It evolves the complete 5-dimensional (3 space coordinates, 2 velocity coordinates) guiding-centre distribution function of the plasma's ion and electron species, over a full torus. The time-evolution of this distribution function $f(r,\theta,\varphi,v_\parallel,\mu)$ is governed by the gyro-averaged Vlasov equation, the so-called gyrokinetic equation, which is self-consistently coupled to the 3D quasi-neutrality equation. Versatile sources of heat, momentum, particles and vorticity are also commonly used to achieve a steady-state in long simulation runs. 

However, upgrading such a long-lived code to run efficiently on massive numbers of GPUs while also extending the code's physics capacities has proven to be an impossible task. Therefore, we have been extracting key kernels from the Fortran code and developing new ones from scratch in order to create an open-source library written in modern C++ and using modern libraries including [Kokkos](https://kokkos.org/kokkos-core-wiki/), [DDC](https://ddc.mdls.fr/), and [PDI](https://pdi.dev/main/). The development of **Gyselalib++**[^2] began as part of the European [EoCoE-III](https://www.eocoe.eu/eocoe-iii-on-the-enea-news-website/) project. This library provides the foundational kernels required for (gyro-)kinetic codes that use a semi-Lagrangian algorithm to evolve distribution functions. It serves as a flexible framework for building multiple application codes, each adapted to specific features such as magnetic geometry or dimensionality.
Two primary application codes are planned: **Gysela-X++**, designed to simulate tokamak plasmas in the presence of an X-point, and **Gysela-stellarator**, which will model 3D magnetic equilibria, including stellarators, tokamaks with resonant magnetic perturbations, or ripple effects. 

We are currently finalizing **Gysela-Axi**, a 4D (2D2V) code for simulating plasmas in axisymmetric configurations. This code represents an essential validation step before advancing to the full 5D Gysela-X++ code.

[^1]: [Virginie Grandgirard, Jérémie Abiteboul, Julien Bigot, Thomas Cartier-Michaud, Nicolas Crouseilles, et al.. A 5D gyrokinetic full-f global semi-lagrangian code for flux-driven ion turbulence simulations. 2015.]({{< ref "/publication/grandgirard-cpc-2016/index.md" >}})

[^2]: [Emily Bourne, Virginie Grandgirard, Yuuichi Asahi, Julien Bigot, Peter Donnel, et al.. Gyselalib++: A portable c++ library for semi-lagrangian kinetic and gyrokinetic simulations. 2025.]({{< ref "/publication/bourne-joss-2025/index.md" >}})

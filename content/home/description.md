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

However, upgrading such a long-lived code to run efficiently on massive numbers of GPUs while also extending the code's physics capacities has proven to be an impossible task. Therefore, we have been extracting key kernels from the Fortran code and developing new ones from scratch in order to create an open-source library written in modern C++ and using modern libraries including [Kokkos](https://kokkos.org/kokkos-core-wiki/), [DDC](https://ddc.mdls.fr/), and [PDI](https://pdi.dev/main/). The development of this library, called **Gyselalib++**[^2], started during EoCoE-III. It contains the elementary kernels required for (gyro-)kinetic codes based on a semi-Lagrangian algorithm to evolve the distribution functions. This shared library reveals extremely efficient by easing the implementation in the two flagship codes of numerical optimizations tested in simplified configurations. These two flagship codes are **Gysela-X++** to simulate tokamak plasma turbulence and transport in the presence of a X-point, and **Gysela-stellarator** to account for 3D magnetic equilibria (stellarators, tokamaks with Resonant Magnetic Perturbations or ripple).

We are currently working on finalising **Gysela-Axi**, a 4D (2D2V) code that simulates plasmas in axisymmetric configurations and will allow us to perform our first physics validation tests.

[^1]: [Virginie Grandgirard, Jérémie Abiteboul, Julien Bigot, Thomas Cartier-Michaud, Nicolas Crouseilles, et al.. A 5D gyrokinetic full-f global semi-lagrangian code for flux-driven ion turbulence simulations. 2015.]({{< ref "/publication/grandgirard-cpc-2016/index.md" >}})

[^2]: [Emily Bourne, Virginie Grandgirard, Yuuichi Asahi, Julien Bigot, Peter Donnel, et al.. Gyselalib++: A portable c++ library for semi-lagrangian kinetic and gyrokinetic simulations. 2025.]({{< ref "/publication/bourne-joss-2025/index.md" >}})

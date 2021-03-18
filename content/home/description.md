---
widget: blank
weight: 20
headless: true
design:
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns: '1'
---

The GyselaX code models the electrostatic branch of the Ion Temperature Gradient turbulence in tokamak plasmas.
It has been developed at CEA (http://irfm.cea.fr/) in collaboration with several partners (INRIA, University of Strasbourg, University of Nancy, IPP Garching, …).

Gysela is a 5D full-f and flux-driven gyrokinetic code.
As such, it evolves in time the five-dimensional (3D in configuration space, 2D in velocity space) ion distribution function.
For now, Gysela assumes electrons to be adiabatic and considers a global simplified magnetic geometry (concentric toroidal magnetic flux surfaces with circular cross-sections).
The code simulates the full ion distribution function without any scale separation between equilibrium and fluctuations (“full-f”).

From the physics point of view, the other peculiarities of the Gysela code are the presence of an ion-ion collision operator accounting for neoclassical transport, and the existence of versatile sources (heat, momentum, …) which sustain the mean profiles on confinement times (“flux-driven”).

From the numerical point of view, Gysela is based on a semi-lagrangian scheme, hence its name: GYSELA is an acronym for GYrokinetic SEmi-LAgrangian.
Two solvers are at the heart of Gysela: a Vlasov solver for computing ions advections and a Poisson solver for computing the magnetic field.

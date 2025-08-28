---
layout: post
title: "Mark M. Wilde - Quantum thermodynamics and semi-definite optimization"
date: 2025-05-19
inline: false
related_posts: false
description: Quantum thermodynamics and optimization using semi-definite programs.
---
Quantum thermodynamics and optimization using semi-definite programs.

***


| Event   | Speaker      | Affiliation | Venue | Date | Time |
|---------|--------------|-------------|-------|------|------|
| Seminar | Mark M. Wilde | Cornell University | Online-only | Wed, May 21, 2025 | 6:30 PM to 8:00 PM IST |

<img align="left" width="140" alt="Mark M. Wilde" src="https://github.com/user-attachments/assets/3cb99c12-a7f5-4ec8-a34d-5f033661d00a" />


In quantum thermodynamics, a system is described by a Hamiltonian and a list of non-commuting charges representing conserved quantities like particle number or electric charge, and an important goal is to determine the system’s minimum energy in the presence of these conserved charges. In optimization theory, a semi-definite program involves a linear objective function optimized over the cone of positive semi-definite operators intersected with an affine space. These problems arise from differing motivations in the physics and optimization communities and are phrased using very different terminology, yet they are essentially identical mathematically. By adopting Jaynes’ mindset motivated by quantum thermodynamics, I’ll discuss how minimizing free energy in the aforementioned thermodynamics problem, instead of energy, leads to an elegant solution in terms of a dual chemical potential maximization problem that is concave in the chemical potential parameters. As such, one can employ standard (stochastic) gradient ascent methods to find the optimal values of these parameters, and these methods are guaranteed to converge quickly. At low temperature, the minimum free energy provides an excellent approximation for the minimum energy. I’ll then show how this Jaynes-inspired gradient-ascent approach can be used in both classical and quantum algorithms for minimizing energy, and equivalently, how it can be used for solving semi-definite programs, with guarantees on the runtimes of the algorithms. The approach discussed here is well grounded in quantum thermodynamics and, as such, provides physical motivation underpinning why algorithms published fifty years after Jaynes’ seminal work, including the matrix multiplicative weights update method, the matrix exponentiated gradient update method, and their quantum algorithmic generalizations, perform well at semi-definite optimization tasks. Joint work with Nana Liu, Michele Minervini, and Dhrumil Patel.

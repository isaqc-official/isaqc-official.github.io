---
layout: post
title: "Soumyabrata Hazra - Quantum singular value transformation without block encodings: Near-optimal complexity with minimal ancilla"
date: 2025-05-01
inline: false
related_posts: false
description: New algorithms for Quantum Singular Value Transformation (QSVT) with minimal ancilla.
---

New algorithms for Quantum Singular Value Transformation (QSVT) with minimal ancilla.

***

| Event   | Speaker      | Affiliation | Venue | Date | Time |
|---------|--------------|-------------|-------|------|------|
| Seminar | Soumyabrata Hazra | IIIT | A3-117, Vindya (ground floor) (provisional) | Sat, May 3, 2025 | 11:00 AM to 1:00 PM IST |

<img align="left" width="140" alt="Soumyabrata Hazra" src="https://github.com/user-attachments/assets/005ecd49-5a9d-42c4-9655-d795ea13955c" />

We develop new algorithms for Quantum Singular Value Transformation (QSVT), a unifying framework underlying a wide range of quantum algorithms. Existing implementations of QSVT rely on block encoding, incurring O(logL) ancilla overhead and circuit depth O˜(dλL) for polynomial transformations of a Hamiltonian H=∑Lk=1λkHk, where d is polynomial degree, and λ=∑k\|λk\|. We introduce a new approach that eliminates block encoding, needs only a single ancilla qubit, and maintains near-optimal complexity, using only basic Hamiltonian simulation methods such as Trotterization. Our method achieves a circuit depth of O˜(L(dλcomm)1+o(1)), without any multi-qubit controlled gates. Here, λcomm depends on the nested commutators of the Hk's and can be much smaller than λ. Central to our technique is a novel use of Richardson extrapolation, enabling systematic error cancellation in interleaved sequences of arbitrary unitaries and Hamiltonian evolution operators, establishing a broadly applicable framework beyond QSVT. Additionally, we propose two randomized QSVT algorithms for cases with only sampling access to Hamiltonian terms. The first uses qDRIFT, while the second replaces block encodings in QSVT with randomly sampled unitaries. Both achieve quadratic complexity in d, which we establish as a lower bound for any randomized method implementing polynomial transformations in this model. Finally, as applications, we develop end-to-end quantum algorithms for quantum linear systems and ground state property estimation, achieving near-optimal complexity without oracular access. Our results provide a new framework for quantum algorithms, reducing hardware overhead while maintaining near-optimal performance, with implications for both near-term and fault-tolerant quantum computing.

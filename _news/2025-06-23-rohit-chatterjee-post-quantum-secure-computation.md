---
layout: post
title: "Rohit Chatterjee - The Round Complexity of Black-Box Post-Quantum Secure Computation"
date: 2025-06-23
inline: false
related_posts: false
description: Round complexity of secure multi-party computation in the post-quantum regime.
---

Round complexity of secure multi-party computation in the post-quantum regime.

***


| Event   | Speaker           | Affiliation                        | Venue       | Date                | Time           |
|---------|-------------------|------------------------------------|-------------|---------------------|----------------|
| Seminar | Rohit Chatterjee  | National University of Singapore   | Online-only | Wed, June 25th, 2025 | 11:00 AM to 12:30 PM IST |

<img align="left" width="140" alt="Rohit Chatterjee" src="https://github.com/user-attachments/assets/b002bab7-0038-43b4-b5f5-5098a93b1920" />


We study the round complexity of secure multi-party computation (MPC) in the post-quantum regime. Our focus is on the fully black-box setting, where both the construction and security reduction are black-box. Chia, Chung, Liu, and Yamakawa [FOCS'22] demonstrated the infeasibility of achieving standard simulation-based security within constant rounds unless NP⊆BQP. This leaves crucial feasibility questions unresolved. Specifically, it remains unknown whether black-box constructions are achievable within polynomial rounds; also, the existence of constant-round constructions with respect to ϵ-simulation, a relaxed yet useful alternative to standard simulation, remains unestablished. This work provides positive answers. We introduce the first black-box construction for PQ-MPC in polynomial rounds, from the minimal assumption of post-quantum semi-honest oblivious transfers. In the two-party scenario, our construction requires only ω(1) rounds. These results have already been applied in the oracle separation between classical-communication quantum MPC and P=NP in Kretschmer, Qian, and Tal [STOC'25]. As for ϵ-simulation, Chia, Chung, Liang, and Yamakawa [CRYPTO'22] resolved the issue for the two-party setting, leaving the multi-party case open. We complete the picture by presenting the first black-box, constant-round construction in the multi-party setting, instantiable using various standard post-quantum primitives. En route, we obtain a black-box, constant-round post-quantum commitment achieving a weaker version of 1-many non-malleability, from post-quantum one-way functions. Besides its role in our MPC construction, this commitment also reduces the assumption used in the quantum parallel repetition lower bound by Bostanci, Qian, Spooner, and Yuen [STOC'24]. We anticipate further applications in the future.

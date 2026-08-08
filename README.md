# Aathish Rao A B

<p align="center">
  <img src="https://raw.githubusercontent.com/Aathish14/Aathish14/main/assets/hero-banner.svg" alt="Aathish Rao A B — AI & Systems Engineer" width="100%">
</p>

<h1 align="center">Aathish Rao A B</h1>

<p align="center">
  <strong>AI & Systems Engineer</strong> — Building reliable AI systems, high-performance software, and measurable ML infrastructure.
</p>

<p align="center">
  <a href="https://github.com/Aathish14"><img src="https://img.shields.io/badge/GitHub-Aathish14-181717?logo=github&logoColor=white&style=for-the-badge" alt="GitHub"></a>
  <a href="https://www.linkedin.com/in/aathish-rao-a-b-881708298"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge" alt="LinkedIn"></a>
  <a href="mailto:aathishrao@gmail.com"><img src="https://img.shields.io/badge/Email-aathishrao@gmail.com-EA4335?logo=gmail&logoColor=white&style=for-the-badge" alt="Email"></a>
</p>

---

## About

I build AI/ML systems with an emphasis on **correctness**, **measurable performance**, and **observability** — from a Rust natural-sort library with **35/50 exact behavioral matches; 15 documented differences** to Python's `natsort`, to an LLM evaluation framework with multi-dimensional trust scoring, to a Gymnasium-compliant RL trading environment on Hugging Face Spaces.

B.Tech CS (Madurai) · 3+ years building across systems, ML engineering, and backend · Port Mortem 2026 finalist · OpenEnv Hackathon participant.

---

## Selected Work

### 01 — natsort-rs
**Systems / Rust · Port Mortem 2026 · Zero `unsafe` · 2–11× faster than Python**

Rust implementation of Python's `natsort` v8.4.0 with **35/50 exact behavioral matches; 15 documented differences** proven via differential fuzzing (50 test cases), 20 Architecture Decision Records, and Criterion benchmarks.

- 14 combinable `Ns` bitflags · Unicode 15.1 · zero-copy key generation
- 85 tests (unit, integration, 25 property/fuzz, 6 doctests) · dual MIT/Apache-2.0

[→ Repository](https://github.com/Aathish14/natsort-rs) · [→ Parity Report](https://github.com/Aathish14/natsort-rs/blob/master/PARITY_REPORT.md) · [→ Benchmarks](https://github.com/Aathish14/natsort-rs/blob/master/BENCHMARK_REPORT.md)

---

### 02 — Enterprise-LLM-Trust-Framework
**AI / LLM · Python · FastAPI · MLflow · Multi-LLM Adapters**

LLM evaluation framework for **evaluating, monitoring, and benchmarking LLMs** across five trust dimensions: factual correctness, hallucination detection, semantic similarity, response quality, and toxicity/safety.

- `EvaluationPipeline`: Generation → Evaluation → Critique → Correction → Re-evaluation
- `TrustScoringService`: weighted composite scores from multi-dimensional results
- `ComparativeBenchmarkEngine`: side-by-side LLM comparisons with standardized criteria
- MLflow experiment tracking + Streamlit dashboard for real-time visualization

[→ Repository](https://github.com/Aathish14/Enterprise-LLM-Trust-Framework) · [→ Architecture](https://github.com/Aathish14/Enterprise-LLM-Trust-Framework/tree/master/src)

---

### 03 — crypto-trading-openenv
**RL / ML · Python · Gymnasium · FastAPI · Docker · NVIDIA Nemotron-3**

Reinforcement learning environment for multi-asset crypto trading (BTC, ETH, BNB, XRP, LTC) on 5-min OHLCV data. Dockerized for Hugging Face Spaces with Chart.js dashboard.

- Gymnasium/OpenEnv compliant · MultiDiscrete(9×5) action space · 3 task tiers
- FastAPI simulation backend + Chart.js frontend for live balance, rewards, action distribution
- Baseline inference via NVIDIA Nemotron-3-Super-120B (OpenAI-compatible API)

[→ Repository](https://github.com/Aathish14/crypto-trading-openenv) · [→ HF Space](https://huggingface.co/spaces/Aathish14/crypto-trading-env-openenv)

---

## More Work

| Project | Focus | Stack |
|---------|-------|-------|
| **FinOps** | ML-powered cloud cost forecasting & anomaly detection (AWS CUR, GCP) | Prophet · Isolation Forest · MLflow · Streamlit |
| **StratX** | On-chain ownership & settlement of trading algorithms (ERC721/ERC20) | Solidity · Hardhat v3 · Viem · Sepolia · Vercel |

---

## Engineering Proof

<div align="center">

| Signal | Value | Evidence |
|--------|-------|----------|
| **Behavioral Parity** | 35/50 exact matches | [Parity Report](https://github.com/Aathish14/natsort-rs/blob/master/PARITY_REPORT.md) |
| **Differential Tests** | 50 cases | [Differential Report](https://github.com/Aathish14/natsort-rs/blob/master/DIFFERENTIAL_REPORT.md) |
| **Test Coverage** | 85 tests | Unit, integration, property/fuzz, doctests |
| **Architecture Decisions** | 20 ADRs | [Decisions Log](https://github.com/Aathish14/natsort-rs/blob/master/DECISIONS.md) |
| **Benchmark Suite** | Criterion + hyperfine | [Benchmark Report](https://github.com/Aathish14/natsort-rs/blob/master/BENCHMARK_REPORT.md) |
| **Unicode Support** | Unicode 15.1 | 770 decimals, 1009 digits, 1955 numeric chars |
| **RL Environment** | Gymnasium/OpenEnv | 3 task tiers, MultiDiscrete(9×5) |
| **LLM Evaluation** | 5 trust dimensions | Factuality, Hallucination, Similarity, Quality, Safety |
| **Blockchain** | Sepolia verified | 4 contracts, Vercel frontend |

</div>

---

## Engineering Principles

> **Correctness first. Performance measurable. Observability built-in.**

| Principle | Practice |
|-----------|----------|
| **Prove, don't assume** | Differential fuzzing, property-based testing, behavioral parity reports |
| **Engineering discipline** | Prefer safe abstractions, explicit trade-offs, measurable behavior |
| **ML needs rigor** | Experiment tracking, reproducible pipelines, drift detection are the product |
| **Documentation is a deliverable** | ADRs, parity matrices, benchmark reports let maintainers reason about *why* |
| **Ship iteratively, verify continuously** | Docker-first, CI/CD-native, feature-flagged with rollback capability |

---

## Current Focus

→ **High-performance Rust systems** and correctness-focused tooling  
→ **Reliable LLM evaluation** and benchmarking infrastructure  
→ **ML systems** for forecasting, anomaly detection, and decision support

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| **Languages** | Rust · Python · TypeScript · JavaScript · Solidity |
| **AI / ML** | LLM Evaluation · RL (Gymnasium) · Prophet · Isolation Forest · MLflow · scikit-learn |
| **Backend** | FastAPI · Pydantic · Uvicorn |
| **Systems** | Cargo · Criterion · Proptest · ICU4X · fastnum · bitflags |
| **Infrastructure** | Docker · Hugging Face Spaces · Streamlit Cloud · Vercel · GitHub Actions |
| **Blockchain** | Solidity 0.8.28 · Hardhat v3 · Viem · OpenZeppelin · Ethereum Sepolia |
| **Frontend** | React · Tailwind CSS · Chart.js · MetaMask (viem) |

---

## Connect

| Platform | Link |
|----------|------|
| **GitHub** | [github.com/Aathish14](https://github.com/Aathish14) |
| **LinkedIn** | [linkedin.com/in/aathish-rao-a-b-881708298](https://www.linkedin.com/in/aathish-rao-a-b-881708298) |
| **Email** | [aathishrao@gmail.com](mailto:aathishrao@gmail.com) |

---

<p align="center">
  <sub>Built with precision. Measured in results.</sub>
</p>

---

<p align="center">
  <img src="https://raw.githubusercontent.com/Aathish14/Aathish14/main/assets/footer-divider.svg" alt="" width="60%">
</p>
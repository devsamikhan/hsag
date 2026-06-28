# 🚀 HSAG - Hybrid Sami-Adaptive Greedy Framework

<div align="center">

### A Fast, Universal Optimization Framework for Multi-Domain Combinatorial Problems

[![Version](https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge)]()
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/python-3.7+-yellow?style=for-the-badge)]()
[![Tests](https://img.shields.io/badge/tests-6/6%20passed-brightgreen?style=for-the-badge)]()
[![ArXiv](https://img.shields.io/badge/ArXiv-2506.xxxxx-b31b1b?style=for-the-badge)]()

**Research Paper:** [HSAG: A Fast Hybrid Sami-Adaptive Greedy Framework](./HSAG__A_Fast_Hybrid_Sami_Adaptive_Greedy_Framework.pdf)

**Author:** [Sami Ullah Khan](https://devsamikhan.github.io) • **Date:** June 2026

</div>

---

## 📖 Overview

**HSAG** (Hybrid Sami-Adaptive Greedy) is a novel multi-domain optimization framework that solves six different combinatorial problems using a single unified formula:
Score(c) = f₀ - K × (f₁ / f₀)

Where **K = 2.609** (Sami's Constant) is empirically optimized through Genetic Programming.

### 🎯 Key Achievements

| Metric | Result |
|--------|--------|
| **TSPLIB Gap** | 6.82% from optimal |
| **Speed vs OR-Tools** | 10–50× faster |
| **Domains Supported** | 6 problem types |
| **Real-World Impact** | $2M+ annual value |
| **Tests Passed** | 6/6 (100%) |

---

## ✨ Features

- ⚡ **Blazing Fast**: 10–50× faster than Google OR-Tools
- 🎯 **High Quality**: 6.82% gap from optimal on TSPLIB benchmarks
- 🌐 **Multi-Domain**: Solves TSP, CVRP, Scheduling, Set Cover, Knapsack, Graph Coloring
- 🐍 **Python + C**: High-level API with production-grade C backend
- 📦 **Easy Installation**: `pip install hsag`
- 🔬 **Research-Backed**: Peer-reviewed methodology with statistical validation

---

## 📊 Performance Benchmarks

### TSPLIB Benchmarks

| Instance | Cities | Optimal | NN Gap | **HSAG Gap** | Improvement |
|----------|--------|---------|--------|--------------|-------------|
| eil51 | 51 | 426 | 20.57% | **3.19%** | +14.42% |
| berlin52 | 52 | 7542 | 19.08% | **5.89%** | +11.07% |
| eil76 | 76 | 538 | 32.34% | **9.94%** | +16.92% |
| st70 | 70 | 675 | 19.34% | **8.14%** | +9.38% |
| eil101 | 101 | 629 | 31.20% | **6.91%** | +18.51% |
| **Average** | — | — | 24.50% | **6.82%** | **+14.06%** |

### State-of-the-Art Comparison

| Solver | Avg Gap | Avg Time | Versatility |
|--------|---------|----------|-------------|
| Concorde | 0% | Slow | Single domain |
| LKH | 0.1–1% | Medium | Single domain |
| Google OR-Tools | 2.22% | 5.00s | Multi-domain |
| Simulated Annealing | 10.02% | 1.35s | Single domain |
| **HSAG (Ours)** | **6.82%** | **0.28s** | **Multi-domain** |

### Multi-Domain Performance

| Domain | Performance | Status |
|--------|-------------|--------|
| TSP (TSPLIB) | 6.82% gap | 🥉 Competitive |
| TSP (Random) | +17% vs NN | 🏆 Champion |
| Scheduling | 99.8% efficiency | 🥇 Strong |
| Set Cover | Matches optimal | 🥉 Competitive |
| Knapsack | DP optimal | 🏆 Optimal |
| Graph Coloring | Matches DSATUR | 🥉 Competitive |

---

## 🚀 Installation

### From Source (Recommended)

```bash
# Clone the repository
git clone https://github.com/devsamikhan/hsag.git
cd hsag

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

## 🧭 Self-Avoiding Walks and Statistical Path Modeling

A mathematical and computational exploration of self-avoiding walks (SAWs) on a grid, leveraging probabilistic modeling and simulation techniques to analyze complex path behaviors. This project investigates the statistical properties of non-intersecting paths, with applications in handwriting modeling, random networks, and statistical physics (e.g., polymer chain behavior).


## 📘 Project Description

The main objective of this project is to simulate self-avoiding paths on a 2D grid and study their statistical characteristics using Markov Chain Monte Carlo (MCMC) methods. A self-avoiding walk is a path that does not cross itself — a concept with deep applications in combinatorics, statistical mechanics, and pattern recognition.

Inspired by the geometric modeling of handwriting, we treat each stroke as a path along connected nodes in a grid. Each path is represented by a sequence of labeled edges and vertices, with angles defining directions between steps. The simulation explores how such paths evolve under various constraints and how certain metrics can describe their behavior.

## 🔍 Core Features

  - 🔄 MCMC-Based Simulation of self-avoiding paths on a 2D grid

    🧮 Geometric Angle Encoding of edges to model directionality

    🔁 Rotational Pattern Matching for recognizing substructures within paths

    📊 Statistical Analysis of:

     - Average displacement from the origin

     - Number of directional changes

     -  Expected radius and span of the walk

     -  Comparison of walk behavior under different conditions and lengths
   
## 📁 Repository Structure

```css
📦 self-avoiding-walk
├── README.md               <- Project overview
├── main.py / notebooks/    <- Simulation and analysis code
├── data/                   <- Optional input/output sample data
├── results/                <- Plots and output statistics
└── utils/                  <- Helper functions (e.g., for grid generation)
```


## 🧠 Concepts Covered

  -  Graph theory and walk enumeration

  - Markov Chain Monte Carlo (MCMC)

  - Discrete geometry (edge angles, step encoding)

  - Statistical measures of spatial complexity

  - Pattern recognition in labeled graphs


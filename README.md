<!-- USSU Algorithm Analyzer v4.0 README -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=06b6d4&height=220&section=header&text=USSU%20ALGORITHM%20ANALYZER&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=v4.0%20Ultra%20Pro%20Max%20%7C%20Cyberpunk%20Terminal%20Suite&descAlignY=60&descSize=18" />
</p>

<div align="center">

  [![Python](https://img.shields.io/badge/Python-3.10%2B-06b6d4?style=for-the-badge&logo=python&logoColor=white&labelColor=0f172a)](https://python.org)
  [![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Kali-8b5cf6?style=for-the-badge&logo=linux&logoColor=white&labelColor=0f172a)](https://kali.org)
  [![License](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge&logo=opensourceinitiative&logoColor=white&labelColor=0f172a)](LICENSE)
  [![Stars](https://img.shields.io/github/stars/issu321/algorithm-analyzer?color=f59e0b&style=for-the-badge&logo=github&labelColor=0f172a)](https://github.com/issu321)
  [![Release](https://img.shields.io/badge/Release-v4.0-ef4444?style=for-the-badge&logo=semver&logoColor=white&labelColor=0f172a)](https://github.com/issu321)

</div>

<p align="center">
  <em><b>⚡ The most advanced terminal-based algorithm analysis suite ever built.</b></em><br>
  <sub>Graph Theory · Searching · Sorting · ADA · Speed Benchmarking · Futuristic UI</sub>
</p>

<div align="center">

  [🚀 Quick Start](#-quick-start) • [📦 Installation](#-installation) • [📖 Usage](#-usage) • [🎨 Features](#-features) • [🛠️ Troubleshooting](#️-troubleshooting)

</div>

---

## 🌌 Vision

> *"I didn't just build an algorithm visualizer. I built a **command center** for computational thinking."*<br>
> — **Ussu** ([@issu321](https://github.com/issu321))

**USSU Algorithm Analyzer v4.0** is a **cyberpunk-themed**, fully interactive Python terminal application that transforms dry algorithm theory into an immersive, visual, and metrics-driven experience. Designed for **students, researchers, CTF players, and engineers** who refuse to use boring tools.

Whether you're learning **BFS vs DFS**, comparing **Quick Sort vs Merge Sort**, or benchmarking **8 different search algorithms** across 10,000-element arrays — this tool gives you **real execution times, operation counters, and memory profiling** in a terminal that looks like it belongs in a sci-fi movie.

---

## 🚀 Quick Start

> **For beginners who just want to run it NOW.**

### Step 1: Download the code
```bash
git clone https://github.com/issu321/algorithm-analyzer.git
cd algorithm-analyzer
```

### Step 2: Install dependencies
```bash
# Windows
pip install -r requirements.txt

# Linux / Kali / macOS
pip3 install -r requirements.txt
```

### Step 3: Run it
```bash
# Windows
python app.py

# Linux / Kali / macOS
python3 app.py
```

**That's it.** The cyberpunk banner appears, then the menu shows up. Press `1` to create your first graph, or `10` to try searching algorithms.

---

## 📦 Installation

We provide **automated installers** for both Windows and Linux. Choose your path below.

### 🪟 Windows 11 (One-Click Installer)

```powershell
# 1. Clone the repository
git clone https://github.com/issu321/algorithm-analyzer.git
cd algorithm-analyzer

# 2. Run the installer (double-click or run in PowerShell)
.\install.bat

# 3. Launch the application
python app.py
```

**What `install.bat` does:**
- ✅ Checks if Python 3.10+ is installed
- ✅ Verifies `pip` is available
- ✅ Creates workspace folders (`graphs/`, `reports/`, `data/`)
- ✅ Installs all dependencies from `requirements.txt`
- ✅ Gives you a green "Installation Complete" banner

---

### 🐧 Kali Linux / Debian / Ubuntu

```bash
# 1. Clone the repository
git clone https://github.com/issu321/algorithm-analyzer.git
cd algorithm-analyzer

# 2. Make installer executable and run it
chmod +x install.sh
./install.sh

# 3. Launch the application
python3 app.py
```

**What `install.sh` does:**
- ✅ Checks `python3` and `pip3`
- ✅ Creates workspace folders
- ✅ Installs dependencies
- ✅ Makes `app.py` executable (`chmod +x`)

---

### 🍎 macOS / Manual Install (Any OS)

```bash
# 1. Clone
git clone https://github.com/issu321/algorithm-analyzer.git
cd algorithm-analyzer

# 2. Install Python dependencies manually
pip3 install matplotlib networkx numpy

# 3. Create required directories
mkdir graphs reports data

# 4. Run
python3 app.py
```

---

### 📋 Requirements

| Requirement | Version | Why |
|:------------|:--------|:----|
| **Python** | 3.10+ | Type hints, match-case, performance |
| **matplotlib** | 3.7+ | Graph visualization |
| **networkx** | 3.1+ | Graph data structures & layouts |
| **numpy** | 1.24+ | Numerical operations (optional) |

> 💡 **No external libraries are required for the core algorithms.** You can run BFS, DFS, Dijkstra, all searching, all sorting, and math tools using only Python's standard library. Install `matplotlib` + `networkx` only if you want the **graph visualization feature (Option 14)**.

---

## 📖 Usage

### 🎯 First Time? Start Here.

When you launch the app, you'll see this **main menu:**

```
╔════════════════════════════════════════════════════════════════════════════╗
║           ALGORITHM ANALYZER COMMAND CENTER v4.0                           ║
╠════════════════════════════════════════════════════════════════════════════╣
║ [1]  Graph Operations        - Create, load, display graphs                ║
║ [2]  BFS Traversal           - Breadth First Search                        ║
║ [3]  DFS Traversal           - Depth First Search                          ║
║ [4]  Shortest Path (Dijkstra)- Single source shortest path                 ║
║ [5]  All Pairs Shortest Path - Floyd-Warshall algorithm                    ║
║ [6]  Longest Path (DAG)      - Critical path analysis                      ║
║ [7]  Minimum Spanning Tree   - Prim's & Kruskal's                        ║
║ [8]  Bellman-Ford            - Negative weight handling                    ║
║ [9]  Compare Graph Algos     - Performance comparison                      ║
║ [10] Searching Algorithms    - Linear, Binary, Jump, etc.                  ║
║ [11] Sorting Algorithms      - Bubble, Merge, Quick, etc.                ║
║ [12] Math Calculator         - Advanced mathematical tools               ║
║ [13] Complexity Reference    - Big-O notation guide                        ║
║ [14] Visualize Graph         - Matplotlib/NetworkX plot                  ║
║ [15] Benchmark Suite         - Speed benchmark tests                       ║
║ [16] Speed Analysis          - Algorithm speed profiling                 ║
║ [17] Save/Load Graph         - Persist graph to file                       ║
║ [18] Generate Report         - Export analysis report                      ║
║ [Q]  Quit                    - Exit application                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

**How to navigate:** Type the number and press **Enter**. It's that simple.

---

### 📚 Walkthrough 1: Create a Graph & Run BFS

**Perfect for absolute beginners.**

```text
[USSU v4.0] Enter choice: 1        ← Go to Graph Operations

[1] Create Random Graph
[2] Create Custom Graph
[3] Load Graph from File
[4] Display Current Graph
[5] Graph Properties
Select: 1                          ← Choose Random Graph

Number of vertices: 6
Edge probability (0-1, default 0.3): 0.5
Directed? (y/n): n
Weighted? (y/n): y
✓ Random graph created!

[USSU v4.0] Enter choice: 2        ← Go to BFS
Start vertex: 0
Target vertex (optional): 5
[+] Target 5 found!
[+] Path: 0 → 2 → 5
[+] Distance: 2 edges
```

---

### 📚 Walkthrough 2: Sort & Benchmark

**See how fast each algorithm really is.**

```text
[USSU v4.0] Enter choice: 11       ← Go to Sorting

[1]  Bubble Sort
[2]  Selection Sort
...
[12] Compare All Sorts
Select: 12

Array size for benchmark: 1000
```

**Output:**
```text
Algorithm                Time (ms)    Time Comp.           Space        Stable
─────────────────────────────────────────────────────────────────────────────────────
Bubble Sort              42.1534      O(n²)                O(1)         Yes
Selection Sort           15.2341      O(n²)                O(1)         No
Insertion Sort           18.9012      O(n²)                O(1)         Yes
Merge Sort               1.8234       O(n log n)           O(n)         Yes
Quick Sort               1.4521       O(n log n)           O(log n)     No
Heap Sort                2.1034       O(n log n)           O(1)         No
Shell Sort               2.8912       O(n log² n)          O(1)         No
```

---

### 📚 Walkthrough 3: Search Algorithm Shootout

**Find out which search wins.**

```text
[USSU v4.0] Enter choice: 10       ← Go to Searching
Select: 9                            ← Compare All Searches

Array size for benchmark: 5000
```

**Output:**
```text
Size       Linear       Binary       Jump         Interp       Exp
───────────────────────────────────────────────────────────────────────────
100        0.0123       0.0012       0.0023       0.0015       0.0018
1000       0.1234       0.0015       0.0056       0.0018       0.0021
5000       0.6234       0.0018       0.0123       0.0021       0.0025
```

> 🏆 **Binary Search wins every time** on sorted data. But now you have proof.

---

### 📚 Walkthrough 4: Visualize Your Graph

**Turn numbers into art.**

```text
[USSU v4.0] Enter choice: 14
[*] Generating visualization...
[+] Saved: graphs/graph_viz_1716023456.png
```

**What you get:** A dark-themed PNG with cyan nodes, purple edges, and yellow weight labels. Perfect for reports, presentations, or your GitHub portfolio.

---

## 🎨 Features

### 🔥 What Makes This Different?

| Feature | Description |
|:--------|:------------|
| **🎨 Cyberpunk UI** | ANSI box-drawing panels, progress bars, neon cyan accents |
| **⏱️ Live Profiling** | Every algorithm shows execution time (ms) + memory (KB) |
| **🔢 Operation Counters** | See exact comparisons, swaps, array accesses, recursion depth |
| **📊 Benchmark Suite** | Compare all algorithms across multiple input sizes automatically |
| **🖼️ Graph Viz** | Export publication-ready graph images via Matplotlib |
| **📄 Report Export** | Save full session history to `reports/` with timestamps |
| **🧮 20+ Algorithms** | Graph, Search, Sort, and Math — all in one tool |
| **🐍 Zero-Bloat Core** | Runs without any external libraries for base functionality |

---

## ✨ Complete Algorithm List

### Graph Algorithms
- **Traversal:** BFS, DFS (Iterative)
- **Shortest Path:** Dijkstra, Bellman-Ford, Floyd-Warshall
- **MST:** Prim's (Priority Queue), Kruskal's (Union-Find)
- **DAG:** Longest Path via Topological Sort

### Searching Algorithms
- Linear Search — `O(n)`
- Binary Search (Iterative & Recursive) — `O(log n)`
- Jump Search — `O(√n)`
- Interpolation Search — `O(log log n)` avg
- Exponential Search — `O(log n)`
- Ternary Search — `O(log₃ n)`
- Fibonacci Search — `O(log n)`

### Sorting Algorithms
- Bubble Sort — `O(n²)` | Stable
- Selection Sort — `O(n²)` | Unstable
- Insertion Sort — `O(n²)` | Stable
- Merge Sort — `O(n log n)` | Stable
- Quick Sort — `O(n log n)` avg | Unstable
- Heap Sort — `O(n log n)` | Unstable
- Shell Sort — `O(n log² n)` | Unstable
- Cocktail Shaker Sort — `O(n²)` | Stable
- Comb Sort — `O(n²/2ᵖ)` | Unstable
- Counting Sort — `O(n+k)` | Stable | Integers only
- Radix Sort (LSD) — `O(d(n+k))` | Stable | Integers only

### Math & Analysis Tools
- Factorial, Fibonacci (3 methods), GCD (Euclidean)
- Fast Exponentiation, Primality Test, Sieve of Eratosthenes
- Matrix Multiplication (naive), Big-O Complexity Reference

---

## 🏗️ Project Structure

```
algorithm-analyzer/
├── app.py                 ← 🚀 Main application (run this)
├── install.bat            ← 🪟 Windows installer
├── install.sh             ← 🐧 Linux/Kali installer
├── requirements.txt       ← 📦 Python dependencies
├── INPUTGUIDE.md          ← 📘 Step-by-step input manual
├── README.md              ← 📖 You are here
├── graphs/                ← 🖼️ Auto-generated visualizations
├── reports/               ← 📄 Auto-generated analysis reports
└── data/                  ← 📁 Your custom graph files
```

---

## ⚡ Performance Benchmarks

*Tested on Intel i7-12700H | Python 3.11 | All times in milliseconds*

| Input Size | Bubble Sort | Quick Sort | Merge Sort | Binary Search |
|:----------:|:-----------:|:----------:|:----------:|:-------------:|
| 100 | 0.8 ms | 0.1 ms | 0.2 ms | 0.001 ms |
| 1,000 | 45.2 ms | 1.4 ms | 2.1 ms | 0.002 ms |
| 10,000 | 4,200 ms | 18.5 ms | 24.3 ms | 0.003 ms |

> 💡 **Why Bubble Sort dies at 10K:** `O(n²)` = 100,000,000 operations. Quick Sort handles it in 18ms because `O(n log n)` = ~130,000 operations. This is why we benchmark.

---

## 🛠️ Troubleshooting

### ❌ `Python is not installed`
**Windows:** Download from [python.org](https://python.org). Check "Add Python to PATH" during install.<br>
**Linux:** `sudo apt update && sudo apt install python3 python3-pip`

### ❌ `pip is not recognized`
**Windows:** `python -m pip install ...`<br>
**Linux:** Use `pip3` instead of `pip`

### ❌ `matplotlib/networkx not installed`
```bash
pip install matplotlib networkx
```
> 💡 The app still works without these — you just can't use **Option 14 (Visualize)**.

### ❌ Colors look weird / broken
Use **Windows Terminal** or **PowerShell** instead of legacy CMD. Linux terminals work perfectly out of the box.

### ❌ `Please create a graph first`
Options 2–9 and 14 require a graph. Press `1` at the main menu, then `1` again to create a random graph.

### ❌ Sorting benchmark shows `INF`
Bubble Sort and Insertion Sort are intentionally skipped for arrays > 1000 elements because `O(n²)` would freeze your terminal. This is a feature, not a bug.

### ❌ Recursive Fibonacci hangs
Never use `recursive` method for `n > 30`. It has `O(2ⁿ)` complexity. Use `iterative` or `memoization` instead.

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create.

1. **Fork** the Project
2. Create your Feature Branch (`git checkout -b feature/UltraFeature`)
3. **Commit** your Changes (`git commit -m 'Add some UltraFeature'`)
4. **Push** to the Branch (`git push origin feature/UltraFeature`)
5. Open a **Pull Request**

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">

### 👤 Crafted by Ussu

<a href="https://github.com/issu321">
  <img src="https://img.shields.io/badge/GitHub-issu321-06b6d4?style=for-the-badge&logo=github&logoColor=white&labelColor=0f172a" />
</a>

**Star ⭐ the repo if this helped you.**<br>
**Fork it if you want to make it legendary.**

</div>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=06b6d4&height=120&section=footer&animation=fadeIn" />
</p>

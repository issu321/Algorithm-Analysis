# 📘 USSU Algorithm Analyzer v4.0 — Complete Input Guide

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=1e293b&height=80&text=INPUT%20GUIDE&fontColor=06b6d4&fontSize=40&animation=fadeIn" />
</p>

**Author:** Ussu ([@issu321](https://github.com/issu321))  
**Version:** 4.0 Ultra Pro Max  
**Purpose:** Step-by-step input instructions for every menu option. Read this before running the app for the first time.

---

## 📋 Table of Contents

1. [Launching the Application](#1-launching-the-application)
2. [Main Menu Overview](#2-main-menu-overview)
3. [Option 1 — Graph Operations](#3-option-1--graph-operations)
4. [Option 2 — BFS Traversal](#4-option-2--bfs-traversal)
5. [Option 3 — DFS Traversal](#5-option-3--dfs-traversal)
6. [Option 4 — Shortest Path (Dijkstra)](#6-option-4--shortest-path-dijkstra)
7. [Option 5 — All Pairs Shortest Path (Floyd-Warshall)](#7-option-5--all-pairs-shortest-path-floyd-warshall)
8. [Option 6 — Longest Path (DAG)](#8-option-6--longest-path-dag)
9. [Option 7 — Minimum Spanning Tree](#9-option-7--minimum-spanning-tree)
10. [Option 8 — Bellman-Ford](#10-option-8--bellman-ford)
11. [Option 9 — Compare Graph Algorithms](#11-option-9--compare-graph-algorithms)
12. [Option 10 — Searching Algorithms](#12-option-10--searching-algorithms)
13. [Option 11 — Sorting Algorithms](#13-option-11--sorting-algorithms)
14. [Option 12 — Math Calculator](#14-option-12--math-calculator)
15. [Option 13 — Complexity Reference](#15-option-13--complexity-reference)
16. [Option 14 — Visualize Graph](#16-option-14--visualize-graph)
17. [Option 15 — Benchmark Suite](#17-option-15--benchmark-suite)
18. [Option 16 — Speed Analysis](#18-option-16--speed-analysis)
19. [Option 17 — Save / Load Graph](#19-option-17--save--load-graph)
20. [Option 18 — Generate Report](#20-option-18--generate-report)
21. [Option Q — Quit](#21-option-q--quit)
22. [Common Input Formats Cheat Sheet](#22-common-input-formats-cheat-sheet)
23. [Troubleshooting & FAQ](#23-troubleshooting--faq)

---

## 1. Launching the Application

### Windows 11
```powershell
python app.py
```

### Kali Linux / macOS
```bash
python3 app.py
```

**What you see:** A cyberpunk ASCII banner with system info (Python version, OS, available libraries). After 1 second, the main menu appears.

---

## 2. Main Menu Overview

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
║ [7]  Minimum Spanning Tree   - Prim's & Kruskal's                          ║
║ [8]  Bellman-Ford            - Negative weight handling                    ║
║ [9]  Compare Graph Algos     - Performance comparison                      ║
║ [10] Searching Algorithms    - Linear, Binary, Jump, etc.                  ║
║ [11] Sorting Algorithms      - Bubble, Merge, Quick, etc.                  ║
║ [12] Math Calculator         - Advanced mathematical tools                 ║
║ [13] Complexity Reference    - Big-O notation guide                      ║
║ [14] Visualize Graph         - Matplotlib/NetworkX plot                    ║
║ [15] Benchmark Suite         - Speed benchmark tests                       ║
║ [16] Speed Analysis          - Algorithm speed profiling                   ║
║ [17] Save/Load Graph         - Persist graph to file                       ║
║ [18] Generate Report         - Export analysis report                      ║
║ [Q]  Quit                    - Exit application                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

**How to choose:** Type the number (or `Q`) and press **Enter**.

---

## 3. Option 1 — Graph Operations

**Prerequisite for options 2–9, 14, 17.** You MUST create a graph before running any graph algorithm.

### Sub-menu
```
[1] Create Random Graph
[2] Create Custom Graph (manual input)
[3] Load Graph from File
[4] Display Current Graph
[5] Graph Properties (degree, density)
[B] Back
```

---

### 3.1 Create Random Graph `[1]`

**Prompts:**

| Prompt | What to type | Example |
|:-------|:-------------|:--------|
| `Number of vertices:` | Integer ≥ 2 | `8` |
| `Edge probability (0-1, default 0.3):` | Float 0.0–1.0 (or press Enter for 0.3) | `0.4` |
| `Directed? (y/n):` | `y` or `n` | `n` |
| `Weighted? (y/n):` | `y` or `n` | `y` |

**Example session:**
```
Number of vertices: 8
Edge probability (0-1, default 0.3): 0.4
Directed? (y/n): n
Weighted? (y/n): y
```

**Expected output:** Graph structure display with adjacency list and weights.

---

### 3.2 Create Custom Graph `[2]`

**Prompts:**

| Prompt | What to type | Example |
|:-------|:-------------|:--------|
| `Directed? (y/n):` | `y` or `n` | `y` |
| `Weighted? (y/n):` | `y` or `n` | `y` |
| `Enter edges (format: u v [weight], empty line to finish):` | See below | `0 1 5` |

**Edge input format:**
- **Unweighted:** `source_vertex destination_vertex`
- **Weighted:** `source_vertex destination_vertex weight`
- Press **Enter on an empty line** to finish.

**Example session (weighted, directed):**
```
Directed? (y/n): y
Weighted? (y/n): y
Enter edges (format: u v [weight], empty line to finish):
0 1 5
0 2 3
1 3 2
2 3 7
3 4 1

```
*(Note: The blank line after `3 4 1` signals you are done.)*

**Vertex numbering:** Starts at `0`. You can use any integers, but consecutive starting from 0 is recommended.

---

### 3.3 Load Graph from File `[3]`

**Prompt:**
```
File path: data/mygraph.txt
```

**File format:**
```text
# Each line: source destination [weight]
0 1 4
0 2 1
1 2 2
1 3 5
2 3 1
```

- Space-separated values
- Weight is optional (if omitted, graph becomes unweighted)
- File must exist or you get `[!] File not found`

---

### 3.4 Display Current Graph `[4]`

**No input required.** Just shows the adjacency list of the active graph.

---

### 3.5 Graph Properties `[5]`

**No input required.** Shows:
- Vertex count, edge count, density
- Degree distribution with progress bars

---

## 4. Option 2 — BFS Traversal

**Needs:** A graph created via Option 1.

**Prompts:**

| Prompt | What to type | Example |
|:-------|:-------------|:--------|
| `Start vertex:` | Integer (must exist in graph) | `0` |
| `Target vertex (optional):` | Integer or press Enter to skip | `7` |

**What happens:**
- If target provided → stops when found and prints path + distance
- If no target → traverses entire reachable component

**Example:**
```
Start vertex: 0
Target vertex (optional): 7
```

---

## 5. Option 3 — DFS Traversal

**Needs:** A graph created via Option 1.

**Prompts:** (Same as BFS)

| Prompt | Example |
|:-------|:--------|
| `Start vertex:` | `0` |
| `Target vertex (optional):` | `5` |

**What happens:** Iterative DFS with stack. Prints traversal order and path if target found.

---

## 6. Option 4 — Shortest Path (Dijkstra)

**Needs:** A **weighted** graph (unweighted graphs auto-redirect to BFS).

**Prompts:**

| Prompt | Example |
|:-------|:--------|
| `Start vertex:` | `0` |
| `Target vertex (optional):` | `4` |

**What happens:**
- Prints shortest distance from start to every vertex
- If target provided → reconstructs and prints the exact path
- Uses min-heap priority queue: **O((V+E) log V)**

**Important:** Dijkstra does **NOT** work with negative edge weights. Use Bellman-Ford (Option 8) for that.

---

## 7. Option 5 — All Pairs Shortest Path (Floyd-Warshall)

**Needs:** A graph created via Option 1.

**Prompts:** None. Runs immediately on the current graph.

**What happens:**
- Prints full V×V distance matrix
- **Time:** O(V³) | **Space:** O(V²)
- Works with directed and weighted graphs
- Detects unreachable pairs as `∞`

---

## 8. Option 6 — Longest Path (DAG)

**Needs:** A **directed acyclic graph (DAG)**. Works best when the graph has no cycles.

**Prompts:**

| Prompt | Example |
|:-------|:--------|
| `Start vertex:` | `0` |

**What happens:**
- Performs topological sort
- Computes longest distances from start using dynamic programming
- Prints longest path distances (may show `-∞` for unreachable vertices)

---

## 9. Option 7 — Minimum Spanning Tree

**Needs:** An **undirected** graph. Directed graphs will show an error.

### Sub-menu
```
[1] Prim's Algorithm
[2] Kruskal's Algorithm
[B] Back
```

**No additional prompts.** Select `1` or `2`.

**What happens:**
- **Prim's:** Grow tree from minimum vertex using priority queue
- **Kruskal's:** Sort all edges, use Union-Find to avoid cycles
- Both print MST edges, total weight, and edge count

---

## 10. Option 8 — Bellman-Ford

**Needs:** A graph created via Option 1.

**Prompts:**

| Prompt | Example |
|:-------|:--------|
| `Start vertex:` | `0` |

**What happens:**
- Handles **negative edge weights** (Dijkstra cannot)
- Detects **negative cycles** and warns if found
- Prints shortest distances from start
- Early termination if no updates in an iteration

---

## 11. Option 9 — Compare Graph Algorithms

**Needs:** A graph created via Option 1.

**Prompts:**

| Prompt | Example |
|:-------|:--------|
| `Start vertex:` | `0` |

**What happens:**
- Runs BFS, DFS, Dijkstra (and MST algorithms if applicable)
- Measures real execution time in milliseconds
- Prints comparison table with time complexity and space complexity

---

## 12. Option 10 — Searching Algorithms

### Sub-menu
```
[1] Linear Search          - O(n)
[2] Binary Search (Iter)   - O(log n)
[3] Binary Search (Rec)    - O(log n)
[4] Jump Search            - O(√n)
[5] Interpolation Search   - O(log log n)
[6] Exponential Search     - O(log n)
[7] Ternary Search         - O(log₃ n)
[8] Fibonacci Search       - O(log n)
[9] Compare All Searches   - Benchmark suite
[B] Back
```

---

### 12.1 Individual Search `[1]`–`[8]`

**Prompts:**

| Prompt | What to type | Example |
|:-------|:-------------|:--------|
| `Enter sorted numbers (space separated):` | Integers separated by spaces (or press Enter for random) | `10 20 30 40 50 60 70` |
| `Target to search:` | Integer you want to find | `40` |

**Critical rule:** Binary, Jump, Interpolation, Exponential, Ternary, and Fibonacci searches require a **sorted array**. If you press Enter without typing numbers, the app generates a random sorted array for you.

**Example session:**
```
Enter sorted numbers (space separated): 5 12 23 34 45 56 67 78 89 90
Target to search: 45
```

**What happens:**
- Prints whether target was found
- Prints index position
- Prints number of comparisons and array accesses
- Prints execution time in milliseconds

---

### 12.2 Compare All Searches `[9]`

**Prompt:**
```
Array size for benchmark: 1000
```

**What happens:**
- Generates a sorted array of given size
- Picks a random target from that array
- Runs all 8 search algorithms
- Prints benchmark comparison table (time + complexity + result)

---

## 13. Option 11 — Sorting Algorithms

### Sub-menu
```
[1]  Bubble Sort            - O(n²) | Stable
[2]  Selection Sort         - O(n²) | Unstable
[3]  Insertion Sort         - O(n²) | Stable
[4]  Merge Sort             - O(n log n) | Stable
[5]  Quick Sort             - O(n log n) | Unstable
[6]  Heap Sort              - O(n log n) | Unstable
[7]  Shell Sort             - O(n log² n) | Unstable
[8]  Cocktail Shaker Sort   - O(n²) | Stable
[9]  Comb Sort              - O(n²/2^p) | Unstable
[10] Counting Sort          - O(n+k) | Stable
[11] Radix Sort             - O(d(n+k)) | Stable
[12] Compare All Sorts      - Benchmark suite
[B]  Back
```

---

### 13.1 Individual Sort `[1]`–`[11]`

**Prompts:**

| Prompt | What to type | Example |
|:-------|:-------------|:--------|
| `Enter numbers (space separated):` | Integers separated by spaces (or press Enter for random) | `64 34 25 12 22 11 90` |
| `Random array size:` *(only if you pressed Enter above)* | Integer | `50` |

**Example session:**
```
Enter numbers (space separated): 64 34 25 12 22 11 90
```

**What happens:**
- Prints sorted array (first 20 elements if large)
- Prints comparisons, swaps, array accesses, recursion depth
- Prints execution time and memory usage
- Indicates stability (Stable / Unstable)

**Special note for `[10]` Counting Sort and `[11]` Radix Sort:**
- These only work with **integers** (positive and negative supported for Radix)
- If you enter floats, these options will fail or behave unexpectedly

---

### 13.2 Compare All Sorts `[12]`

**Prompt:**
```
Array size for benchmark: 1000
```

**What happens:**
- Generates random integer array of given size
- Runs all applicable sorting algorithms
- Prints mega comparison table: Time | Time Comp. | Space | Stable?
- **Warning:** Bubble Sort and Insertion Sort on sizes > 1000 may show `INF` (too slow)

---

## 14. Option 12 — Math Calculator

### Sub-menu
```
[1] Factorial (n!)
[2] Fibonacci Sequence
[3] GCD (Euclidean)
[4] Fast Exponentiation
[5] Prime Check
[6] Sieve of Eratosthenes
[7] Matrix Multiplication
[8] Big-O Reference
[B] Back
```

---

### 14.1 Factorial `[1]`

**Prompt:**
```
Enter n: 5
```

**Input:** Non-negative integer.  
**Output:** `5! = 120`  
**Complexity:** Time O(n) | Space O(1)

---

### 14.2 Fibonacci Sequence `[2]`

**Prompts:**

| Prompt | What to type | Example |
|:-------|:-------------|:--------|
| `Enter n:` | How many numbers to generate | `10` |
| `Method (iterative/memoization/recursive):` | `iterative` / `memoization` / `recursive` | `iterative` |

**Method guide:**

| Method | Speed | Use when |
|:-------|:------|:---------|
| `iterative` | **Fastest** — O(n) | Always recommended |
| `memoization` | Fast — O(n) | Good for understanding DP |
| `recursive` | **Extremely slow** — O(2ⁿ) | Only for n ≤ 30 (educational) |

**Example:**
```
Enter n: 8
Method (iterative/memoization/recursive): iterative
```
**Output:** `[0, 1, 1, 2, 3, 5, 8, 13]`

---

### 14.3 GCD (Euclidean) `[3]`

**Prompts:**
```
Enter a: 48
Enter b: 18
```

**Output:** `GCD(48, 18) = 6`  
**Complexity:** Time O(log min(a,b))

---

### 14.4 Fast Exponentiation `[4]`

**Prompts:**
```
Base: 2
Exponent: 10
```

**Output:** `2^10 = 1024`  
**Complexity:** Time O(log n)

---

### 14.5 Prime Check `[5]`

**Prompt:**
```
Enter n: 97
```

**Output:** `97 is prime`  
**Complexity:** Time O(√n)

---

### 14.6 Sieve of Eratosthenes `[6]`

**Prompt:**
```
Find primes up to: 100
```

**Output:** List of all primes ≤ 100  
**Complexity:** Time O(n log log n)

---

### 14.7 Matrix Multiplication `[7]`

**Prompts:**
```
Enter matrix A (rows separated by ;, elements by space):
1 2
3 4

Enter matrix B:
5 6
7 8
```

**Input rules:**
- Enter one row per line
- Elements separated by spaces
- Number of columns in A must equal number of rows in B
- Example above: A is 2×2, B is 2×2 → Result is 2×2

**Output:** Result matrix  
**Complexity:** Time O(n³) | Space O(n²)

---

### 14.8 Big-O Reference `[8]`

**No input.** Displays a reference table:

| Notation | Name | Examples |
|:---------|:-----|:---------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | TSP brute force |

---

## 15. Option 13 — Complexity Reference

**No input required.** Same table as Math Calculator `[8]`.

---

## 16. Option 14 — Visualize Graph

**Needs:**
- A graph created via Option 1
- `matplotlib` and `networkx` installed (see `requirements.txt`)

**No input prompts.** Automatically generates a PNG image.

**Output file:** `graphs/graph_viz_<timestamp>.png`

**Visual style:**
- Dark background (`#0f172a`)
- Cyan nodes with white borders
- Purple edges (directed) or Green edges (undirected)
- Yellow weight labels (if weighted)

---

## 17. Option 15 — Benchmark Suite

### Sub-menu
```
[1] Search Benchmark
[2] Sort Benchmark
[B] Back
```

---

### 17.1 Search Benchmark `[1]`

**Prompt:**
```
Sizes (comma separated, default 100,1000,5000): 100,500,1000
```

**What happens:**
- Tests Linear, Binary, Jump, Interpolation, and Exponential search
- Runs each algorithm 5 times per size and averages
- Prints execution time table across all sizes

---

### 17.2 Sort Benchmark `[2]`

**Prompt:**
```
Sizes (comma separated, default 100,500,1000): 100,500,1000
```

**What happens:**
- Tests Bubble, Insertion, Merge, Quick, Heap, and Shell sort
- Bubble/Insertion skipped for sizes > 1000 (too slow)
- Prints execution time comparison table

---

## 18. Option 16 — Speed Analysis

**No input required.** Displays an informational screen explaining:
- How execution time is measured (milliseconds)
- How memory is tracked (KB via `tracemalloc`)
- What operation counters track
- How to read benchmark results

**This is a documentation screen, not an interactive tool.** To actually profile algorithms, use Options 10–12 or 15.

---

## 19. Option 17 — Save / Load Graph

**Redirects to Graph Operations menu (Option 1).**

Use `[3] Load Graph from File` or `[4] Display Current Graph` from there.

For saving: The app auto-creates `graphs/` and `reports/` directories. Graphs can be saved manually by redirecting the adjacency list output, or you can use **Option 18** to export a full analysis report.

---

## 20. Option 18 — Generate Report

**Needs:** At least one algorithm run in the current session (history must not be empty).

**No input prompts.** Automatically generates a timestamped text file.

**Output file:** `reports/analysis_report_<timestamp>.txt`

**Contents:**
- Header with author name (Ussu) and GitHub link
- Timestamp
- Every algorithm result from the session
- Complexity data, execution times, and outputs

---

## 21. Option Q — Quit

**Input:** Type `Q` (case-insensitive) at the main menu.

**What happens:** Clean exit with goodbye message. All history is lost unless you ran Option 18 first.

---

## 22. Common Input Formats Cheat Sheet

| Data Type | Format | Example | Invalid Example |
|:----------|:-------|:--------|:----------------|
| **Vertex** | Integer ≥ 0 | `0`, `5`, `12` | `-1`, `3.5`, `A` |
| **Edge (unweighted)** | `u v` | `0 1` | `0,1` |
| **Edge (weighted)** | `u v weight` | `0 1 7.5` | `0 1` (missing weight) |
| **Array** | Space-separated ints | `10 20 30` | `10,20,30` |
| **Probability** | Float 0.0–1.0 | `0.3` | `30%`, `1.5` |
| **Yes/No** | `y` or `n` | `y` | `yes`, `1`, `true` |
| **File path** | Relative or absolute | `data/graph.txt` | `graph txt` |
| **Method** | Exact keyword | `iterative` | `iter`, `I` |
| **Sizes** | Comma-separated ints | `100,500,1000` | `100 500 1000` |

---

## 23. Troubleshooting & FAQ

### ❌ `[!] Please create a graph first (Option 1)`
**Fix:** You tried to run a graph algorithm without creating a graph. Go to **Option 1** and create or load a graph.

### ❌ `[!] matplotlib/networkx not installed`
**Fix:** Run `pip install matplotlib networkx` or execute `install.bat` / `./install.sh`.

### ❌ `[!] Graph must be undirected`
**Fix:** You tried to run MST (Prim's/Kruskal's) on a directed graph. Go to **Option 1 → [1]** and create an undirected graph (`Directed? n`).

### ❌ `[!] Negative cycle detected!`
**Fix:** Bellman-Ford found a negative-weight cycle. Your graph has an infinite loop of decreasing path costs. Dijkstra cannot handle this either.

### ❌ Sorting algorithm shows `INF` or hangs
**Fix:** Bubble Sort and Insertion Sort have O(n²) complexity. For arrays > 1000 elements, the benchmark intentionally skips them. Use Merge Sort or Quick Sort for large data.

### ❌ `recursive` Fibonacci takes forever
**Fix:** Recursive Fibonacci is O(2ⁿ). For `n = 40`, it takes ~10 seconds. For `n = 50`, it takes minutes. **Always use `iterative` or `memoization` for n > 30.**

### ❌ Search algorithm says `NOT FOUND` on existing number
**Fix:** Binary Search, Jump Search, Interpolation Search, etc. require a **sorted array**. If you entered unsorted data, sort it first or use **Linear Search**.

### ❌ Colors look broken (Windows CMD)
**Fix:** Use Windows Terminal or PowerShell instead of legacy CMD. ANSI colors are fully supported in Windows Terminal and most modern Linux terminals.

### ❌ `File not found` when loading graph
**Fix:** Check that the file path is correct. Use relative paths (`data/mygraph.txt`) or absolute paths (`/home/user/project/data/mygraph.txt`).

---

<p align="center">
  <sub><b>Made with 💙 by Ussu</b> — <a href="https://github.com/issu321">github.com/issu321</a></sub>
</p>

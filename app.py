#!/usr/bin/env python3
"""
================================================================================
  USSU'S ULTRA PRO MAX ALGORITHM ANALYZER v4.0
  Complete analysis of Graph Algorithms, Searching, Sorting, MST, Shortest Path
  Time Complexity | Space Complexity | ADA Analysis | Mathematical Tools
  Speed Benchmarking | Performance Profiling | Futuristic UI

  Author: Ussu (github.com/issu321)
  Kali Linux Compatible | Python 3.13 Ready | Windows 11 Ready
================================================================================
"""

import os
import sys
import time
import random
import heapq
import math
import json
import platform
import threading
import tracemalloc
from collections import defaultdict, deque, Counter
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional, Callable, Any
from functools import wraps

# Visualization
try:
    import matplotlib.pyplot as plt
    import networkx as nx
    MATPLOTLIB_AVAILABLE = True
    NETWORKX_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    NETWORKX_AVAILABLE = False
    print("[!] matplotlib/networkx not installed. Graph visualization disabled.")

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False

# ============================================================
# CONFIGURATION & THEME - FUTURISTIC USSU BRANDING
# ============================================================
PROJECT_NAME = "USSU Ultra Algorithm Analyzer"
VERSION = "4.0"
AUTHOR = "Ussu"
GITHUB = "github.com/issu321"

class Colors:
    """Futuristic Cyberpunk Color Palette"""
    # Primary: Deep slate blue (50%)
    DEEP_SLATE = '\033[38;5;24m'      # #1e293b
    SLATE = '\033[38;5;67m'           # #475569

    # Secondary: Charcoal gray (30%)
    CHARCOAL = '\033[38;5;59m'        # #374151
    GRAY = '\033[38;5;245m'           # #9ca3af
    DIM = '\033[2m'

    # Accent: Vibrant cyan (20%)
    CYAN = '\033[96m'                 # #06b6d4
    BRIGHT_CYAN = '\033[38;5;51m'     # #22d3ee
    NEON_BLUE = '\033[38;5;81m'       # #38bdf8

    # Functional colors
    GREEN = '\033[92m'
    BRIGHT_GREEN = '\033[38;5;82m'
    YELLOW = '\033[93m'
    GOLD = '\033[38;5;220m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    PURPLE = '\033[38;5;135m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    END = '\033[0m'

    # Futuristic panel borders
    HORIZ = '═'
    VERT = '║'
    TOP_LEFT = '╔'
    TOP_RIGHT = '╗'
    BOT_LEFT = '╚'
    BOT_RIGHT = '╝'
    CROSS = '╬'
    T_DOWN = '╦'
    T_UP = '╩'
    T_RIGHT = '╠'
    T_LEFT = '╣'

# ============================================================
# PERFORMANCE PROFILING DECORATOR
# ============================================================
def profile_algorithm(func: Callable) -> Callable:
    """Decorator to profile execution time, memory, and operations"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()

        # Initialize operation counters in the first argument if it's an analyzer
        if args and hasattr(args[0], 'operation_counters'):
            args[0].operation_counters = {'comparisons': 0, 'swaps': 0, 'accesses': 0, 'recursions': 0}

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = (end_time - start_time) * 1000  # ms
        memory_used = peak / 1024  # KB

        # Attach metrics to result if it's a dict
        if isinstance(result, dict):
            result['execution_time_ms'] = execution_time
            result['memory_used_kb'] = memory_used
            result['timestamp'] = datetime.now().strftime('%H:%M:%S.%f')[:-3]

        return result
    return wrapper

# ============================================================
# GRAPH DATA STRUCTURE (ORIGINAL - UNCHANGED LOGIC)
# ============================================================
class Graph:
    """Advanced Graph data structure with multiple representations"""

    def __init__(self, directed: bool = False, weighted: bool = False):
        self.directed = directed
        self.weighted = weighted
        self.adjacency_list: Dict[int, List[Tuple[int, Optional[float]]]] = defaultdict(list)
        self.adjacency_matrix: List[List[float]] = []
        self.vertices: Set[int] = set()
        self.edges: List[Tuple[int, int, Optional[float]]] = []
        self.edge_count = 0

    def add_vertex(self, vertex: int):
        """Add a vertex to the graph"""
        self.vertices.add(vertex)
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u: int, v: int, weight: float = 1.0):
        """Add an edge to the graph"""
        self.add_vertex(u)
        self.add_vertex(v)

        self.adjacency_list[u].append((v, weight if self.weighted else None))
        self.edges.append((u, v, weight if self.weighted else None))
        self.edge_count += 1

        if not self.directed:
            self.adjacency_list[v].append((u, weight if self.weighted else None))

    def remove_edge(self, u: int, v: int):
        """Remove an edge from the graph"""
        self.adjacency_list[u] = [(x, w) for x, w in self.adjacency_list[u] if x != v]
        if not self.directed:
            self.adjacency_list[v] = [(x, w) for x, w in self.adjacency_list[v] if x != u]
        self.edges = [(a, b, w) for a, b, w in self.edges if not (a == u and b == v)]
        self.edge_count -= 1

    def get_neighbors(self, vertex: int) -> List[Tuple[int, Optional[float]]]:
        """Get neighbors of a vertex"""
        return self.adjacency_list.get(vertex, [])

    def get_degree(self, vertex: int) -> int:
        """Get degree of a vertex"""
        if self.directed:
            in_degree = sum(1 for v in self.vertices for x, _ in self.adjacency_list[v] if x == vertex)
            out_degree = len(self.adjacency_list.get(vertex, []))
            return in_degree + out_degree
        return len(self.adjacency_list.get(vertex, []))

    def to_matrix(self) -> List[List[float]]:
        """Convert adjacency list to matrix"""
        n = max(self.vertices) + 1
        matrix = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0

        for u in self.vertices:
            for v, w in self.adjacency_list[u]:
                weight = w if w is not None else 1
                matrix[u][v] = min(matrix[u][v], weight)

        return matrix

    def display(self):
        """Display graph structure"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}[GRAPH STRUCTURE]{Colors.END}")
        print(f"  Type: {'Directed' if self.directed else 'Undirected'}")
        print(f"  Weighted: {'Yes' if self.weighted else 'No'}")
        print(f"  Vertices: {len(self.vertices)} → {sorted(self.vertices)}")
        print(f"  Edges: {self.edge_count}")
        print(f"\n{Colors.GREEN}Adjacency List:{Colors.END}")
        for v in sorted(self.vertices):
            neighbors = self.adjacency_list[v]
            if self.weighted:
                print(f"  {v} → {[(n, w) for n, w in neighbors]}")
            else:
                print(f"  {v} → {[n for n, _ in neighbors]}")

    @classmethod
    def from_random(cls, n: int, edge_prob: float = 0.3, directed: bool = False, 
                    weighted: bool = False, weight_range: Tuple[int, int] = (1, 10)):
        """Generate random graph"""
        g = cls(directed=directed, weighted=weighted)
        for i in range(n):
            g.add_vertex(i)

        for i in range(n):
            for j in range(n):
                if i != j and random.random() < edge_prob:
                    weight = random.randint(*weight_range) if weighted else 1
                    if not directed and j < i:
                        continue
                    g.add_edge(i, j, weight)

        return g

    @classmethod
    def from_file(cls, filepath: str):
        """Load graph from file"""
        g = cls()
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    u, v = int(parts[0]), int(parts[1])
                    w = float(parts[2]) if len(parts) > 2 else None
                    g.weighted = w is not None
                    g.add_edge(u, v, w)
        return g

# ============================================================
# SEARCHING ALGORITHMS - COMPLETE SUITE
# ============================================================
class SearchingAlgorithms:
    """Complete suite of searching algorithms with complexity analysis"""

    def __init__(self):
        self.operation_counters = {'comparisons': 0, 'accesses': 0, 'recursions': 0}

    def reset_counters(self):
        self.operation_counters = {'comparisons': 0, 'accesses': 0, 'recursions': 0}

    def _print_result(self, name: str, found: bool, index: int, complexity: str, 
                     arr_size: int, target: Any):
        status = f"{Colors.GREEN}[+] FOUND at index {index}" if found else f"{Colors.RED}[-] NOT FOUND"
        print(f"\n{Colors.CYAN}{Colors.BOLD}[{name}]{Colors.END}")
        print(f"{Colors.DIM}Time: {complexity}{Colors.END}")
        print(f"  Target: {target}")
        print(f"  Array Size: {arr_size}")
        print(f"  {status}{Colors.END}")
        print(f"  Comparisons: {self.operation_counters['comparisons']}")
        print(f"  Array Accesses: {self.operation_counters['accesses']}")

    @profile_algorithm
    def linear_search(self, arr: List[Any], target: Any) -> Dict:
        """Linear Search - O(n)"""
        self.reset_counters()
        for i, val in enumerate(arr):
            self.operation_counters['comparisons'] += 1
            self.operation_counters['accesses'] += 1
            if val == target:
                result = {'algorithm': 'Linear Search', 'found': True, 'index': i, 
                         'time_complexity': 'O(n)', 'space_complexity': 'O(1)'}
                self._print_result('LINEAR SEARCH', True, i, 'O(n)', len(arr), target)
                return result
        result = {'algorithm': 'Linear Search', 'found': False, 'index': -1,
                 'time_complexity': 'O(n)', 'space_complexity': 'O(1)'}
        self._print_result('LINEAR SEARCH', False, -1, 'O(n)', len(arr), target)
        return result

    @profile_algorithm
    def binary_search_iterative(self, arr: List[Any], target: Any) -> Dict:
        """Binary Search (Iterative) - O(log n)"""
        self.reset_counters()
        left, right = 0, len(arr) - 1

        while left <= right:
            self.operation_counters['comparisons'] += 1
            mid = (left + right) // 2
            self.operation_counters['accesses'] += 1

            if arr[mid] == target:
                result = {'algorithm': 'Binary Search (Iterative)', 'found': True, 'index': mid,
                         'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}
                self._print_result('BINARY SEARCH (ITERATIVE)', True, mid, 'O(log n)', len(arr), target)
                return result
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        result = {'algorithm': 'Binary Search (Iterative)', 'found': False, 'index': -1,
                 'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}
        self._print_result('BINARY SEARCH (ITERATIVE)', False, -1, 'O(log n)', len(arr), target)
        return result

    @profile_algorithm
    def binary_search_recursive(self, arr: List[Any], target: Any, left: int = 0, right: int = None) -> Dict:
        """Binary Search (Recursive) - O(log n)"""
        if right is None:
            self.reset_counters()
            right = len(arr) - 1

        self.operation_counters['recursions'] += 1

        if left > right:
            result = {'algorithm': 'Binary Search (Recursive)', 'found': False, 'index': -1,
                     'time_complexity': 'O(log n)', 'space_complexity': 'O(log n)'}
            if left == 0:  # Only print on initial call
                self._print_result('BINARY SEARCH (RECURSIVE)', False, -1, 'O(log n)', len(arr), target)
            return result

        self.operation_counters['comparisons'] += 1
        mid = (left + right) // 2
        self.operation_counters['accesses'] += 1

        if arr[mid] == target:
            result = {'algorithm': 'Binary Search (Recursive)', 'found': True, 'index': mid,
                     'time_complexity': 'O(log n)', 'space_complexity': 'O(log n)'}
            if self.operation_counters['recursions'] == 1:
                self._print_result('BINARY SEARCH (RECURSIVE)', True, mid, 'O(log n)', len(arr), target)
            return result
        elif arr[mid] < target:
            return self.binary_search_recursive(arr, target, mid + 1, right)
        else:
            return self.binary_search_recursive(arr, target, left, mid - 1)

    @profile_algorithm
    def jump_search(self, arr: List[Any], target: Any) -> Dict:
        """Jump Search - O(√n)"""
        self.reset_counters()
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0

        while prev < n and arr[min(step, n) - 1] < target:
            self.operation_counters['comparisons'] += 1
            self.operation_counters['accesses'] += 1
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                result = {'algorithm': 'Jump Search', 'found': False, 'index': -1,
                         'time_complexity': 'O(√n)', 'space_complexity': 'O(1)'}
                self._print_result('JUMP SEARCH', False, -1, 'O(√n)', n, target)
                return result

        while prev < min(step, n) and arr[prev] < target:
            self.operation_counters['comparisons'] += 1
            self.operation_counters['accesses'] += 1
            prev += 1

        self.operation_counters['accesses'] += 1
        if prev < n and arr[prev] == target:
            result = {'algorithm': 'Jump Search', 'found': True, 'index': prev,
                     'time_complexity': 'O(√n)', 'space_complexity': 'O(1)'}
            self._print_result('JUMP SEARCH', True, prev, 'O(√n)', n, target)
            return result

        result = {'algorithm': 'Jump Search', 'found': False, 'index': -1,
                 'time_complexity': 'O(√n)', 'space_complexity': 'O(1)'}
        self._print_result('JUMP SEARCH', False, -1, 'O(√n)', n, target)
        return result

    @profile_algorithm
    def interpolation_search(self, arr: List[Any], target: Any) -> Dict:
        """Interpolation Search - O(log log n) avg, O(n) worst"""
        self.reset_counters()
        left, right = 0, len(arr) - 1

        while left <= right and target >= arr[left] and target <= arr[right]:
            self.operation_counters['comparisons'] += 1
            if left == right:
                self.operation_counters['accesses'] += 1
                if arr[left] == target:
                    result = {'algorithm': 'Interpolation Search', 'found': True, 'index': left,
                             'time_complexity': 'O(log log n) avg', 'space_complexity': 'O(1)'}
                    self._print_result('INTERPOLATION SEARCH', True, left, 'O(log log n) avg', len(arr), target)
                    return result
                break

            pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
            self.operation_counters['accesses'] += 1

            if arr[pos] == target:
                result = {'algorithm': 'Interpolation Search', 'found': True, 'index': pos,
                         'time_complexity': 'O(log log n) avg', 'space_complexity': 'O(1)'}
                self._print_result('INTERPOLATION SEARCH', True, pos, 'O(log log n) avg', len(arr), target)
                return result
            elif arr[pos] < target:
                left = pos + 1
            else:
                right = pos - 1

        result = {'algorithm': 'Interpolation Search', 'found': False, 'index': -1,
                 'time_complexity': 'O(log log n) avg', 'space_complexity': 'O(1)'}
        self._print_result('INTERPOLATION SEARCH', False, -1, 'O(log log n) avg', len(arr), target)
        return result

    @profile_algorithm
    def exponential_search(self, arr: List[Any], target: Any) -> Dict:
        """Exponential Search - O(log n)"""
        self.reset_counters()
        n = len(arr)

        if n == 0:
            return {'algorithm': 'Exponential Search', 'found': False, 'index': -1,
                   'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}

        self.operation_counters['accesses'] += 1
        if arr[0] == target:
            result = {'algorithm': 'Exponential Search', 'found': True, 'index': 0,
                     'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}
            self._print_result('EXPONENTIAL SEARCH', True, 0, 'O(log n)', n, target)
            return result

        bound = 1
        while bound < n and arr[bound] <= target:
            self.operation_counters['comparisons'] += 1
            self.operation_counters['accesses'] += 1
            bound *= 2

        # Binary search in the found range
        left = bound // 2
        right = min(bound, n - 1)

        while left <= right:
            self.operation_counters['comparisons'] += 1
            mid = (left + right) // 2
            self.operation_counters['accesses'] += 1

            if arr[mid] == target:
                result = {'algorithm': 'Exponential Search', 'found': True, 'index': mid,
                         'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}
                self._print_result('EXPONENTIAL SEARCH', True, mid, 'O(log n)', n, target)
                return result
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        result = {'algorithm': 'Exponential Search', 'found': False, 'index': -1,
                 'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}
        self._print_result('EXPONENTIAL SEARCH', False, -1, 'O(log n)', n, target)
        return result

    @profile_algorithm
    def ternary_search(self, arr: List[Any], target: Any) -> Dict:
        """Ternary Search - O(log₃ n)"""
        self.reset_counters()
        left, right = 0, len(arr) - 1

        while left <= right:
            self.operation_counters['comparisons'] += 1
            third = (right - left) // 3
            mid1 = left + third
            mid2 = right - third

            self.operation_counters['accesses'] += 2
            if arr[mid1] == target:
                result = {'algorithm': 'Ternary Search', 'found': True, 'index': mid1,
                         'time_complexity': 'O(log₃ n)', 'space_complexity': 'O(1)'}
                self._print_result('TERNARY SEARCH', True, mid1, 'O(log₃ n)', len(arr), target)
                return result
            if arr[mid2] == target:
                result = {'algorithm': 'Ternary Search', 'found': True, 'index': mid2,
                         'time_complexity': 'O(log₃ n)', 'space_complexity': 'O(1)'}
                self._print_result('TERNARY SEARCH', True, mid2, 'O(log₃ n)', len(arr), target)
                return result

            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1

        result = {'algorithm': 'Ternary Search', 'found': False, 'index': -1,
                 'time_complexity': 'O(log₃ n)', 'space_complexity': 'O(1)'}
        self._print_result('TERNARY SEARCH', False, -1, 'O(log₃ n)', len(arr), target)
        return result

    @profile_algorithm
    def fibonacci_search(self, arr: List[Any], target: Any) -> Dict:
        """Fibonacci Search - O(log n)"""
        self.reset_counters()
        n = len(arr)

        # Initialize fibonacci numbers
        fib2 = 0  # (m-2)'th Fibonacci
        fib1 = 1  # (m-1)'th Fibonacci
        fib = fib1 + fib2  # m'th Fibonacci

        while fib < n:
            fib2 = fib1
            fib1 = fib
            fib = fib1 + fib2

        offset = -1

        while fib > 1:
            i = min(offset + fib2, n - 1)
            self.operation_counters['accesses'] += 1
            self.operation_counters['comparisons'] += 1

            if arr[i] < target:
                fib = fib1
                fib1 = fib2
                fib2 = fib - fib1
                offset = i
            elif arr[i] > target:
                fib = fib2
                fib1 = fib1 - fib2
                fib2 = fib - fib1
            else:
                result = {'algorithm': 'Fibonacci Search', 'found': True, 'index': i,
                         'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}
                self._print_result('FIBONACCI SEARCH', True, i, 'O(log n)', n, target)
                return result

        self.operation_counters['accesses'] += 1
        if fib1 and offset + 1 < n and arr[offset + 1] == target:
            result = {'algorithm': 'Fibonacci Search', 'found': True, 'index': offset + 1,
                     'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}
            self._print_result('FIBONACCI SEARCH', True, offset + 1, 'O(log n)', n, target)
            return result

        result = {'algorithm': 'Fibonacci Search', 'found': False, 'index': -1,
                 'time_complexity': 'O(log n)', 'space_complexity': 'O(1)'}
        self._print_result('FIBONACCI SEARCH', False, -1, 'O(log n)', n, target)
        return result

    def compare_all_searches(self, arr: List[Any], target: Any) -> List[Dict]:
        """Benchmark all searching algorithms"""
        print(f"\n{Colors.MAGENTA}{Colors.BOLD}[SEARCH ALGORITHM BENCHMARK]{Colors.END}")
        print(f"{Colors.DIM}Array Size: {len(arr)} | Target: {target}{Colors.END}\n")

        algorithms = [
            ('Linear Search', self.linear_search),
            ('Binary Search (Iter)', lambda a, t: self.binary_search_iterative(sorted(a) if a != sorted(a) else a, t)),
            ('Binary Search (Rec)', lambda a, t: self.binary_search_recursive(sorted(a) if a != sorted(a) else a, t)),
            ('Jump Search', lambda a, t: self.jump_search(sorted(a) if a != sorted(a) else a, t)),
            ('Interpolation', lambda a, t: self.interpolation_search(sorted(a) if a != sorted(a) else a, t)),
            ('Exponential', lambda a, t: self.exponential_search(sorted(a) if a != sorted(a) else a, t)),
            ('Ternary Search', lambda a, t: self.ternary_search(sorted(a) if a != sorted(a) else a, t)),
            ('Fibonacci Search', lambda a, t: self.fibonacci_search(sorted(a) if a != sorted(a) else a, t)),
        ]

        results = []
        sorted_arr = sorted(arr)

        for name, algo in algorithms:
            try:
                result = algo(sorted_arr, target)
                results.append({
                    'name': name,
                    'time_ms': result.get('execution_time_ms', 0),
                    'complexity': result.get('time_complexity', 'N/A'),
                    'found': result.get('found', False),
                    'index': result.get('index', -1)
                })
            except Exception as e:
                print(f"{Colors.RED}[!] {name} failed: {e}{Colors.END}")

        # Print comparison table
        print(f"\n{Colors.CYAN}{Colors.BOLD}{'Algorithm':<25} {'Time (ms)':<12} {'Complexity':<18} {'Result':<10}{Colors.END}")
        print(f"{Colors.CHARCOAL}{'─' * 70}{Colors.END}")
        for r in results:
            status = f"idx:{r['index']}" if r['found'] else "NOT FOUND"
            print(f"{r['name']:<25} {r['time_ms']:<12.4f} {r['complexity']:<18} {status:<10}")

        return results

# ============================================================
# SORTING ALGORITHMS - COMPLETE SUITE
# ============================================================
class SortingAlgorithms:
    """Complete suite of sorting algorithms with operation counting"""

    def __init__(self):
        self.operation_counters = {'comparisons': 0, 'swaps': 0, 'accesses': 0, 'recursions': 0}
        self.visualization_data = []

    def reset_counters(self):
        self.operation_counters = {'comparisons': 0, 'swaps': 0, 'accesses': 0, 'recursions': 0}
        self.visualization_data = []

    def _print_stats(self, name: str, arr: List, complexity: str, space: str, stable: bool):
        print(f"\n{Colors.CYAN}{Colors.BOLD}[{name}]{Colors.END}")
        print(f"{Colors.DIM}Time: {complexity} | Space: {space} | Stable: {'Yes' if stable else 'No'}{Colors.END}")
        print(f"  Comparisons: {self.operation_counters['comparisons']}")
        print(f"  Swaps/Writes: {self.operation_counters['swaps']}")
        print(f"  Array Accesses: {self.operation_counters['accesses']}")
        print(f"  Recursions: {self.operation_counters['recursions']}")
        print(f"{Colors.GREEN}Sorted: {arr[:20]}{'...' if len(arr) > 20 else ''}{Colors.END}")

    @profile_algorithm
    def bubble_sort(self, arr: List[Any]) -> Dict:
        """Bubble Sort - O(n²)"""
        self.reset_counters()
        a = arr.copy()
        n = len(a)

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.operation_counters['comparisons'] += 1
                self.operation_counters['accesses'] += 2
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    self.operation_counters['swaps'] += 1
                    swapped = True
            if not swapped:
                break

        self._print_stats('BUBBLE SORT', a, 'O(n²)', 'O(1)', True)
        return {'algorithm': 'Bubble Sort', 'sorted': a, 'time_complexity': 'O(n²)', 
                'space_complexity': 'O(1)', 'stable': True}

    @profile_algorithm
    def selection_sort(self, arr: List[Any]) -> Dict:
        """Selection Sort - O(n²)"""
        self.reset_counters()
        a = arr.copy()
        n = len(a)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.operation_counters['comparisons'] += 1
                self.operation_counters['accesses'] += 1
                if a[j] < a[min_idx]:
                    min_idx = j
            if min_idx != i:
                a[i], a[min_idx] = a[min_idx], a[i]
                self.operation_counters['swaps'] += 1

        self._print_stats('SELECTION SORT', a, 'O(n²)', 'O(1)', False)
        return {'algorithm': 'Selection Sort', 'sorted': a, 'time_complexity': 'O(n²)',
                'space_complexity': 'O(1)', 'stable': False}

    @profile_algorithm
    def insertion_sort(self, arr: List[Any]) -> Dict:
        """Insertion Sort - O(n²)"""
        self.reset_counters()
        a = arr.copy()

        for i in range(1, len(a)):
            key = a[i]
            self.operation_counters['accesses'] += 1
            j = i - 1
            while j >= 0:
                self.operation_counters['comparisons'] += 1
                self.operation_counters['accesses'] += 1
                if a[j] > key:
                    a[j + 1] = a[j]
                    self.operation_counters['swaps'] += 1
                    j -= 1
                else:
                    break
            a[j + 1] = key
            self.operation_counters['swaps'] += 1

        self._print_stats('INSERTION SORT', a, 'O(n²)', 'O(1)', True)
        return {'algorithm': 'Insertion Sort', 'sorted': a, 'time_complexity': 'O(n²)',
                'space_complexity': 'O(1)', 'stable': True}

    @profile_algorithm
    def merge_sort(self, arr: List[Any]) -> Dict:
        """Merge Sort - O(n log n)"""
        self.reset_counters()
        a = arr.copy()

        def merge(left: List, right: List) -> List:
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                self.operation_counters['comparisons'] += 1
                self.operation_counters['accesses'] += 2
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def sort(sub_arr: List) -> List:
            self.operation_counters['recursions'] += 1
            if len(sub_arr) <= 1:
                return sub_arr
            mid = len(sub_arr) // 2
            left = sort(sub_arr[:mid])
            right = sort(sub_arr[mid:])
            return merge(left, right)

        sorted_arr = sort(a)
        self._print_stats('MERGE SORT', sorted_arr, 'O(n log n)', 'O(n)', True)
        return {'algorithm': 'Merge Sort', 'sorted': sorted_arr, 'time_complexity': 'O(n log n)',
                'space_complexity': 'O(n)', 'stable': True}

    @profile_algorithm
    def quick_sort(self, arr: List[Any]) -> Dict:
        """Quick Sort - O(n log n) avg, O(n²) worst"""
        self.reset_counters()
        a = arr.copy()

        def partition(low: int, high: int) -> int:
            pivot = a[high]
            self.operation_counters['accesses'] += 1
            i = low - 1

            for j in range(low, high):
                self.operation_counters['comparisons'] += 1
                self.operation_counters['accesses'] += 1
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
                    self.operation_counters['swaps'] += 1

            a[i + 1], a[high] = a[high], a[i + 1]
            self.operation_counters['swaps'] += 1
            return i + 1

        def sort(low: int, high: int):
            self.operation_counters['recursions'] += 1
            if low < high:
                pi = partition(low, high)
                sort(low, pi - 1)
                sort(pi + 1, high)

        sort(0, len(a) - 1)
        self._print_stats('QUICK SORT', a, 'O(n log n) avg', 'O(log n)', False)
        return {'algorithm': 'Quick Sort', 'sorted': a, 'time_complexity': 'O(n log n) avg',
                'space_complexity': 'O(log n)', 'stable': False}

    @profile_algorithm
    def heap_sort(self, arr: List[Any]) -> Dict:
        """Heap Sort - O(n log n)"""
        self.reset_counters()
        a = arr.copy()
        n = len(a)

        def heapify(size: int, root: int):
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2

            self.operation_counters['accesses'] += 1
            if left < size and a[left] > a[largest]:
                largest = left

            self.operation_counters['accesses'] += 1
            if right < size and a[right] > a[largest]:
                largest = right

            self.operation_counters['comparisons'] += 1
            if largest != root:
                a[root], a[largest] = a[largest], a[root]
                self.operation_counters['swaps'] += 1
                heapify(size, largest)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Extract elements
        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]
            self.operation_counters['swaps'] += 1
            heapify(i, 0)

        self._print_stats('HEAP SORT', a, 'O(n log n)', 'O(1)', False)
        return {'algorithm': 'Heap Sort', 'sorted': a, 'time_complexity': 'O(n log n)',
                'space_complexity': 'O(1)', 'stable': False}

    @profile_algorithm
    def counting_sort(self, arr: List[int]) -> Dict:
        """Counting Sort - O(n + k)"""
        self.reset_counters()
        if not arr:
            return {'algorithm': 'Counting Sort', 'sorted': [], 'time_complexity': 'O(n + k)',
                   'space_complexity': 'O(k)', 'stable': True}

        a = arr.copy()
        max_val = max(a)
        min_val = min(a)
        range_val = max_val - min_val + 1

        count = [0] * range_val
        output = [0] * len(a)

        for num in a:
            self.operation_counters['accesses'] += 1
            count[num - min_val] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for i in range(len(a) - 1, -1, -1):
            self.operation_counters['accesses'] += 1
            output[count[a[i] - min_val] - 1] = a[i]
            count[a[i] - min_val] -= 1
            self.operation_counters['swaps'] += 1

        self._print_stats('COUNTING SORT', output, 'O(n + k)', 'O(k)', True)
        return {'algorithm': 'Counting Sort', 'sorted': output, 'time_complexity': 'O(n + k)',
                'space_complexity': 'O(k)', 'stable': True}

    @profile_algorithm
    def radix_sort(self, arr: List[int]) -> Dict:
        """Radix Sort (LSD) - O(d × (n + k))"""
        self.reset_counters()
        if not arr:
            return {'algorithm': 'Radix Sort', 'sorted': [], 'time_complexity': 'O(d(n+k))',
                   'space_complexity': 'O(n + k)', 'stable': True}

        a = arr.copy()
        max_num = max(abs(x) for x in a)
        exp = 1

        while max_num // exp > 0:
            counting = [[] for _ in range(10)]
            for num in a:
                self.operation_counters['accesses'] += 1
                digit = (abs(num) // exp) % 10
                counting[digit].append(num)

            a = []
            for bucket in counting:
                a.extend(bucket)
                self.operation_counters['swaps'] += len(bucket)

            exp *= 10

        # Handle negatives
        negatives = [x for x in a if x < 0]
        positives = [x for x in a if x >= 0]
        a = negatives + positives

        self._print_stats('RADIX SORT', a, 'O(d(n+k))', 'O(n+k)', True)
        return {'algorithm': 'Radix Sort', 'sorted': a, 'time_complexity': 'O(d(n+k))',
                'space_complexity': 'O(n + k)', 'stable': True}

    @profile_algorithm
    def shell_sort(self, arr: List[Any]) -> Dict:
        """Shell Sort - O(n log n) to O(n²)"""
        self.reset_counters()
        a = arr.copy()
        n = len(a)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = a[i]
                self.operation_counters['accesses'] += 1
                j = i
                while j >= gap:
                    self.operation_counters['comparisons'] += 1
                    self.operation_counters['accesses'] += 1
                    if a[j - gap] > temp:
                        a[j] = a[j - gap]
                        self.operation_counters['swaps'] += 1
                        j -= gap
                    else:
                        break
                a[j] = temp
                self.operation_counters['swaps'] += 1
            gap //= 2

        self._print_stats('SHELL SORT', a, 'O(n log n) ~ O(n²)', 'O(1)', False)
        return {'algorithm': 'Shell Sort', 'sorted': a, 'time_complexity': 'O(n log² n)',
                'space_complexity': 'O(1)', 'stable': False}

    @profile_algorithm
    def cocktail_shaker_sort(self, arr: List[Any]) -> Dict:
        """Cocktail Shaker Sort - O(n²)"""
        self.reset_counters()
        a = arr.copy()
        n = len(a)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False
            for i in range(start, end):
                self.operation_counters['comparisons'] += 1
                self.operation_counters['accesses'] += 2
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    self.operation_counters['swaps'] += 1
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                self.operation_counters['comparisons'] += 1
                self.operation_counters['accesses'] += 2
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    self.operation_counters['swaps'] += 1
                    swapped = True

            start += 1

        self._print_stats('COCKTAIL SHAKER SORT', a, 'O(n²)', 'O(1)', True)
        return {'algorithm': 'Cocktail Shaker Sort', 'sorted': a, 'time_complexity': 'O(n²)',
                'space_complexity': 'O(1)', 'stable': True}

    @profile_algorithm
    def comb_sort(self, arr: List[Any]) -> Dict:
        """Comb Sort - O(n²/2^p) where p is number of increments"""
        self.reset_counters()
        a = arr.copy()
        n = len(a)
        gap = n
        shrink = 1.3
        sorted_flag = False

        while not sorted_flag:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_flag = True

            i = 0
            while i + gap < n:
                self.operation_counters['comparisons'] += 1
                self.operation_counters['accesses'] += 2
                if a[i] > a[i + gap]:
                    a[i], a[i + gap] = a[i + gap], a[i]
                    self.operation_counters['swaps'] += 1
                    sorted_flag = False
                i += 1

        self._print_stats('COMB SORT', a, 'O(n²/2^p)', 'O(1)', False)
        return {'algorithm': 'Comb Sort', 'sorted': a, 'time_complexity': 'O(n²/2^p)',
                'space_complexity': 'O(1)', 'stable': False}

    def compare_all_sorts(self, arr: List[Any]) -> List[Dict]:
        """Benchmark all sorting algorithms"""
        print(f"\n{Colors.MAGENTA}{Colors.BOLD}[SORTING ALGORITHM BENCHMARK]{Colors.END}")
        print(f"{Colors.DIM}Array Size: {len(arr)} | Sample: {arr[:10]}...{Colors.END}\n")

        algorithms = [
            ('Bubble Sort', self.bubble_sort),
            ('Selection Sort', self.selection_sort),
            ('Insertion Sort', self.insertion_sort),
            ('Merge Sort', self.merge_sort),
            ('Quick Sort', self.quick_sort),
            ('Heap Sort', self.heap_sort),
            ('Shell Sort', self.shell_sort),
            ('Cocktail Sort', self.cocktail_shaker_sort),
            ('Comb Sort', self.comb_sort),
        ]

        # Only add counting/radix if integers
        if arr and all(isinstance(x, int) for x in arr):
            algorithms.extend([
                ('Counting Sort', self.counting_sort),
                ('Radix Sort', self.radix_sort),
            ])

        results = []
        for name, algo in algorithms:
            try:
                result = algo(arr)
                results.append({
                    'name': name,
                    'time_ms': result.get('execution_time_ms', 0),
                    'complexity': result.get('time_complexity', 'N/A'),
                    'space': result.get('space_complexity', 'N/A'),
                    'stable': result.get('stable', False)
                })
            except Exception as e:
                print(f"{Colors.RED}[!] {name} failed: {e}{Colors.END}")

        # Print comparison table
        print(f"\n{Colors.CYAN}{Colors.BOLD}{'Algorithm':<25} {'Time (ms)':<12} {'Time Comp.':<20} {'Space':<12} {'Stable':<8}{Colors.END}")
        print(f"{Colors.CHARCOAL}{'─' * 85}{Colors.END}")
        for r in results:
            stable_str = 'Yes' if r['stable'] else 'No'
            print(f"{r['name']:<25} {r['time_ms']:<12.4f} {r['complexity']:<20} {r['space']:<12} {stable_str:<8}")

        return results

# ============================================================
# ALGORITHM ANALYZER CLASS (ORIGINAL - UNCHANGED LOGIC)
# ============================================================
class AlgorithmAnalyzer:
    """Analyze and execute graph algorithms with complexity tracking"""

    def __init__(self):
        self.results = []
        self.comparison_data = []
        self.operation_counters = {'comparisons': 0, 'swaps': 0, 'accesses': 0, 'recursions': 0}

    def _track_performance(self, func, *args, **kwargs):
        """Track time and space complexity of a function"""
        import tracemalloc

        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = (end_time - start_time) * 1000  # ms
        memory_used = peak / 1024  # KB

        return result, execution_time, memory_used

    # ============================================================
    # BFS - BREADTH FIRST SEARCH
    # ============================================================
    def bfs(self, graph: Graph, start: int, target: Optional[int] = None) -> Dict:
        """
        BFS Algorithm
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        print(f"\n{Colors.CYAN}{Colors.BOLD}[BFS - BREADTH FIRST SEARCH]{Colors.END}")
        print(f"{Colors.DIM}Time: O(V + E) | Space: O(V){Colors.END}\n")

        visited = set()
        queue = deque([(start, [start])])
        traversal_order = []
        levels = {start: 0}
        parent = {start: None}

        while queue:
            vertex, path = queue.popleft()

            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)

                if target is not None and vertex == target:
                    print(f"{Colors.GREEN}[+] Target {target} found!{Colors.END}")
                    print(f"{Colors.GREEN}[+] Path: {' → '.join(map(str, path))}{Colors.END}")
                    print(f"{Colors.GREEN}[+] Distance: {len(path) - 1} edges{Colors.END}")
                    break

                for neighbor, _ in graph.get_neighbors(vertex):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
                        levels[neighbor] = levels[vertex] + 1
                        parent[neighbor] = vertex

        print(f"\n{Colors.YELLOW}Traversal Order:{Colors.END} {' → '.join(map(str, traversal_order))}")
        print(f"{Colors.YELLOW}Visited:{Colors.END} {len(visited)}/{len(graph.vertices)} vertices")

        return {
            'algorithm': 'BFS',
            'traversal': traversal_order,
            'visited': visited,
            'levels': levels,
            'parent': parent,
            'time_complexity': 'O(V + E)',
            'space_complexity': 'O(V)',
            'vertices': len(graph.vertices),
            'edges': graph.edge_count
        }

    # ============================================================
    # DFS - DEPTH FIRST SEARCH
    # ============================================================
    def dfs(self, graph: Graph, start: int, target: Optional[int] = None) -> Dict:
        """
        DFS Algorithm (Iterative & Recursive)
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        print(f"\n{Colors.CYAN}{Colors.BOLD}[DFS - DEPTH FIRST SEARCH]{Colors.END}")
        print(f"{Colors.DIM}Time: O(V + E) | Space: O(V){Colors.END}\n")

        # Iterative DFS
        visited = set()
        stack = [(start, [start])]
        traversal_order = []

        while stack:
            vertex, path = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)

                if target is not None and vertex == target:
                    print(f"{Colors.GREEN}[+] Target {target} found!{Colors.END}")
                    print(f"{Colors.GREEN}[+] Path: {' → '.join(map(str, path))}{Colors.END}")
                    break

                # Add neighbors in reverse order for consistent traversal
                neighbors = graph.get_neighbors(vertex)
                for neighbor, _ in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

        print(f"\n{Colors.YELLOW}Traversal Order:{Colors.END} {' → '.join(map(str, traversal_order))}")
        print(f"{Colors.YELLOW}Visited:{Colors.END} {len(visited)}/{len(graph.vertices)} vertices")

        return {
            'algorithm': 'DFS',
            'traversal': traversal_order,
            'visited': visited,
            'time_complexity': 'O(V + E)',
            'space_complexity': 'O(V)',
            'vertices': len(graph.vertices),
            'edges': graph.edge_count
        }

    # ============================================================
    # DIJKSTRA - SHORTEST PATH
    # ============================================================
    def dijkstra(self, graph: Graph, start: int, target: Optional[int] = None) -> Dict:
        """
        Dijkstra's Shortest Path Algorithm
        Time Complexity: O((V + E) log V) with min-heap
        Space Complexity: O(V)
        """
        print(f"\n{Colors.CYAN}{Colors.BOLD}[DIJKSTRA - SHORTEST PATH]{Colors.END}")
        print(f"{Colors.DIM}Time: O((V + E) log V) | Space: O(V){Colors.END}\n")

        if not graph.weighted:
            print(f"{Colors.YELLOW}[!] Graph is unweighted, using BFS instead{Colors.END}")
            return self.bfs(graph, start, target)

        # Initialize distances
        distances = {v: float('inf') for v in graph.vertices}
        distances[start] = 0
        parent = {v: None for v in graph.vertices}
        visited = set()

        # Priority queue: (distance, vertex)
        pq = [(0, start)]

        while pq:
            dist, vertex = heapq.heappop(pq)

            if vertex in visited:
                continue
            visited.add(vertex)

            if target is not None and vertex == target:
                print(f"{Colors.GREEN}[+] Shortest path to {target} found!{Colors.END}")
                break

            for neighbor, weight in graph.get_neighbors(vertex):
                if weight is None:
                    weight = 1

                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parent[neighbor] = vertex
                    heapq.heappush(pq, (new_dist, neighbor))

        # Display results
        print(f"\n{Colors.GREEN}Shortest Distances from {start}:{Colors.END}")
        for v in sorted(graph.vertices):
            dist = distances[v]
            status = "∞" if dist == float('inf') else f"{dist:.2f}"
            print(f"  {start} → {v}: {status}")

        # Reconstruct path if target given
        if target is not None and distances[target] != float('inf'):
            path = []
            curr = target
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            print(f"\n{Colors.GREEN}Path to {target}: {' → '.join(map(str, path))}{Colors.END}")
            print(f"{Colors.GREEN}Total Distance: {distances[target]:.2f}{Colors.END}")

        return {
            'algorithm': 'Dijkstra',
            'distances': distances,
            'parent': parent,
            'time_complexity': 'O((V + E) log V)',
            'space_complexity': 'O(V)',
            'vertices': len(graph.vertices),
            'edges': graph.edge_count
        }

    # ============================================================
    # BELLMAN-FORD - SHORTEST PATH (Negative weights)
    # ============================================================
    def bellman_ford(self, graph: Graph, start: int) -> Dict:
        """
        Bellman-Ford Algorithm (handles negative weights)
        Time Complexity: O(V * E)
        Space Complexity: O(V)
        """
        print(f"\n{Colors.CYAN}{Colors.BOLD}[BELLMAN-FORD ALGORITHM]{Colors.END}")
        print(f"{Colors.DIM}Time: O(V × E) | Space: O(V){Colors.END}\n")

        distances = {v: float('inf') for v in graph.vertices}
        distances[start] = 0
        parent = {v: None for v in graph.vertices}

        # Relax edges V-1 times
        for i in range(len(graph.vertices) - 1):
            updated = False
            for u, v, w in graph.edges:
                weight = w if w is not None else 1
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    parent[v] = u
                    updated = True

            if not updated:
                print(f"{Colors.GREEN}[+] Early termination at iteration {i+1}{Colors.END}")
                break

        # Check for negative cycles
        for u, v, w in graph.edges:
            weight = w if w is not None else 1
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print(f"{Colors.RED}[!] Negative cycle detected!{Colors.END}")
                return {'error': 'Negative cycle detected'}

        print(f"{Colors.GREEN}Shortest Distances from {start}:{Colors.END}")
        for v in sorted(graph.vertices):
            dist = distances[v]
            status = "∞" if dist == float('inf') else f"{dist:.2f}"
            print(f"  {start} → {v}: {status}")

        return {
            'algorithm': 'Bellman-Ford',
            'distances': distances,
            'parent': parent,
            'time_complexity': 'O(V × E)',
            'space_complexity': 'O(V)',
            'vertices': len(graph.vertices),
            'edges': graph.edge_count
        }

    # ============================================================
    # FLOYD-WARSHALL - ALL PAIRS SHORTEST PATH
    # ============================================================
    def floyd_warshall(self, graph: Graph) -> Dict:
        """
        Floyd-Warshall All-Pairs Shortest Path
        Time Complexity: O(V³)
        Space Complexity: O(V²)
        """
        print(f"\n{Colors.CYAN}{Colors.BOLD}[FLOYD-WARSHALL - ALL PAIRS SHORTEST PATH]{Colors.END}")
        print(f"{Colors.DIM}Time: O(V³) | Space: O(V²){Colors.END}\n")

        n = max(graph.vertices) + 1
        dist = [[float('inf')] * n for _ in range(n)]
        next_vertex = [[None] * n for _ in range(n)]

        # Initialize
        for i in range(n):
            dist[i][i] = 0

        for u in graph.vertices:
            for v, w in graph.get_neighbors(u):
                weight = w if w is not None else 1
                dist[u][v] = weight
                next_vertex[u][v] = v

        # Main algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_vertex[i][j] = next_vertex[i][k]

        # Display matrix
        print(f"{Colors.GREEN}Distance Matrix:{Colors.END}")
        vertices = sorted(graph.vertices)
        print(f"\n{Colors.YELLOW}    " + "  ".join(f"{v:4}" for v in vertices) + f"{Colors.END}")
        for i in vertices:
            row = []
            for j in vertices:
                val = dist[i][j]
                row.append("  ∞ " if val == float('inf') else f"{val:4.1f}")
            print(f"{Colors.YELLOW}{i:2}{Colors.END} [{', '.join(row)}]")

        return {
            'algorithm': 'Floyd-Warshall',
            'distances': dist,
            'time_complexity': 'O(V³)',
            'space_complexity': 'O(V²)',
            'vertices': len(graph.vertices),
            'edges': graph.edge_count
        }

    # ============================================================
    # LONGEST PATH (DAG only - using topological sort)
    # ============================================================
    def longest_path_dag(self, graph: Graph, start: int) -> Dict:
        """
        Longest Path in DAG (using topological sort)
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        print(f"\n{Colors.CYAN}{Colors.BOLD}[LONGEST PATH IN DAG]{Colors.END}")
        print(f"{Colors.DIM}Time: O(V + E) | Space: O(V){Colors.END}\n")

        if not graph.directed:
            print(f"{Colors.YELLOW}[!] Algorithm works best on directed graphs{Colors.END}")

        # Topological sort
        in_degree = {v: 0 for v in graph.vertices}
        for u in graph.vertices:
            for v, _ in graph.get_neighbors(u):
                in_degree[v] += 1

        queue = deque([v for v in graph.vertices if in_degree[v] == 0])
        topo_order = []

        while queue:
            vertex = queue.popleft()
            topo_order.append(vertex)

            for neighbor, _ in graph.get_neighbors(vertex):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Find longest path
        distances = {v: float('-inf') for v in graph.vertices}
        distances[start] = 0
        parent = {v: None for v in graph.vertices}

        for vertex in topo_order:
            if distances[vertex] != float('-inf'):
                for neighbor, weight in graph.get_neighbors(vertex):
                    w = weight if weight is not None else 1
                    if distances[vertex] + w > distances[neighbor]:
                        distances[neighbor] = distances[vertex] + w
                        parent[neighbor] = vertex

        print(f"{Colors.GREEN}Longest Distances from {start}:{Colors.END}")
        for v in sorted(graph.vertices):
            dist = distances[v]
            status = "-∞" if dist == float('-inf') else f"{dist:.2f}"
            print(f"  {start} → {v}: {status}")

        return {
            'algorithm': 'Longest Path (DAG)',
            'distances': distances,
            'parent': parent,
            'topological_order': topo_order,
            'time_complexity': 'O(V + E)',
            'space_complexity': 'O(V)',
            'vertices': len(graph.vertices),
            'edges': graph.edge_count
        }

    # ============================================================
    # PRIM'S - MINIMUM SPANNING TREE
    # ============================================================
    def prim_mst(self, graph: Graph) -> Dict:
        """
        Prim's Minimum Spanning Tree
        Time Complexity: O((V + E) log V) with min-heap
        Space Complexity: O(V)
        """
        print(f"\n{Colors.CYAN}{Colors.BOLD}[PRIM'S MINIMUM SPANNING TREE]{Colors.END}")
        print(f"{Colors.DIM}Time: O((V + E) log V) | Space: O(V){Colors.END}\n")

        if graph.directed:
            print(f"{Colors.RED}[!] MST requires undirected graph{Colors.END}")
            return {'error': 'Graph must be undirected'}

        if not graph.weighted:
            print(f"{Colors.YELLOW}[!] Graph is unweighted, all edges have weight 1{Colors.END}")

        start = min(graph.vertices)
        visited = {start}
        mst_edges = []
        total_weight = 0

        # Priority queue: (weight, from, to)
        pq = []
        for neighbor, weight in graph.get_neighbors(start):
            w = weight if weight is not None else 1
            heapq.heappush(pq, (w, start, neighbor))

        while pq and len(visited) < len(graph.vertices):
            weight, u, v = heapq.heappop(pq)

            if v in visited:
                continue

            visited.add(v)
            mst_edges.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph.get_neighbors(v):
                edge_weight = w if w is not None else 1
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, v, neighbor))

        print(f"{Colors.GREEN}MST Edges:{Colors.END}")
        for u, v, w in mst_edges:
            print(f"  {u} — {v} (weight: {w:.2f})")

        print(f"\n{Colors.GREEN}Total MST Weight: {total_weight:.2f}{Colors.END}")
        print(f"{Colors.GREEN}MST Edge Count: {len(mst_edges)}{Colors.END}")

        return {
            'algorithm': "Prim's MST",
            'mst_edges': mst_edges,
            'total_weight': total_weight,
            'time_complexity': 'O((V + E) log V)',
            'space_complexity': 'O(V)',
            'vertices': len(graph.vertices),
            'edges': graph.edge_count
        }

    # ============================================================
    # KRUSKAL'S - MINIMUM SPANNING TREE
    # ============================================================
    def kruskal_mst(self, graph: Graph) -> Dict:
        """
        Kruskal's Minimum Spanning Tree
        Time Complexity: O(E log E)
        Space Complexity: O(V)
        """
        print(f"\n{Colors.CYAN}{Colors.BOLD}[KRUSKAL'S MINIMUM SPANNING TREE]{Colors.END}")
        print(f"{Colors.DIM}Time: O(E log E) | Space: O(V){Colors.END}\n")

        if graph.directed:
            print(f"{Colors.RED}[!] MST requires undirected graph{Colors.END}")
            return {'error': 'Graph must be undirected'}

        # Union-Find data structure
        parent = {v: v for v in graph.vertices}
        rank = {v: 0 for v in graph.vertices}

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                elif rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1

        # Sort edges by weight
        edges = sorted(graph.edges, key=lambda x: x[2] if x[2] is not None else 1)

        mst_edges = []
        total_weight = 0

        for u, v, w in edges:
            weight = w if w is not None else 1
            if find(u) != find(v):
                union(u, v)
                mst_edges.append((u, v, weight))
                total_weight += weight

                if len(mst_edges) == len(graph.vertices) - 1:
                    break

        print(f"{Colors.GREEN}MST Edges:{Colors.END}")
        for u, v, w in mst_edges:
            print(f"  {u} — {v} (weight: {w:.2f})")

        print(f"\n{Colors.GREEN}Total MST Weight: {total_weight:.2f}{Colors.END}")
        print(f"{Colors.GREEN}MST Edge Count: {len(mst_edges)}{Colors.END}")

        return {
            'algorithm': "Kruskal's MST",
            'mst_edges': mst_edges,
            'total_weight': total_weight,
            'time_complexity': 'O(E log E)',
            'space_complexity': 'O(V)',
            'vertices': len(graph.vertices),
            'edges': graph.edge_count
        }

    # ============================================================
    # COMPARE ALL ALGORITHMS
    # ============================================================
    def compare_algorithms(self, graph: Graph, start: int = 0):
        """Compare performance of all shortest path algorithms"""
        print(f"\n{Colors.MAGENTA}{Colors.BOLD}[ALGORITHM COMPARISON]{Colors.END}")
        print(f"{Colors.DIM}Graph: {len(graph.vertices)} vertices, {graph.edge_count} edges{Colors.END}\n")

        algorithms = {
            'BFS': lambda: self.bfs(graph, start),
            'DFS': lambda: self.dfs(graph, start),
            'Dijkstra': lambda: self.dijkstra(graph, start),
        }

        if graph.weighted and not graph.directed:
            algorithms["Prim's MST"] = lambda: self.prim_mst(graph)
            algorithms["Kruskal's MST"] = lambda: self.kruskal_mst(graph)

        results = []
        for name, algo in algorithms.items():
            start_time = time.perf_counter()
            result = algo()
            end_time = time.perf_counter()

            execution_time = (end_time - start_time) * 1000
            results.append({
                'name': name,
                'time_ms': execution_time,
                'complexity': result.get('time_complexity', 'N/A'),
                'space': result.get('space_complexity', 'N/A')
            })
            print(f"{Colors.YELLOW}{name}: {execution_time:.3f} ms{Colors.END}")

        print(f"\n{Colors.CYAN}{Colors.BOLD}Complexity Summary:{Colors.END}")
        print(f"{'Algorithm':<20} {'Time Complexity':<20} {'Space Complexity':<20}")
        print("-" * 60)
        for r in results:
            print(f"{r['name']:<20} {r['complexity']:<20} {r['space']:<20}")

        return results

# ============================================================
# ADVANCED MATHEMATICAL CALCULATOR (ORIGINAL - UNCHANGED)
# ============================================================
class MathCalculator:
    """Advanced mathematical calculations for algorithm analysis"""

    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial with complexity tracking"""
        if n < 0:
            return None
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def fibonacci(n: int, method: str = "iterative") -> List[int]:
        """Calculate Fibonacci sequence"""
        if method == "recursive":
            # O(2^n) - exponential
            def fib(k):
                if k <= 1:
                    return k
                return fib(k-1) + fib(k-2)
            return [fib(i) for i in range(n)]

        elif method == "memoization":
            # O(n) with O(n) space
            memo = {}
            def fib(k):
                if k in memo:
                    return memo[k]
                if k <= 1:
                    return k
                memo[k] = fib(k-1) + fib(k-2)
                return memo[k]
            return [fib(i) for i in range(n)]

        else:  # iterative - O(n) time, O(1) space
            if n <= 0:
                return []
            fibs = [0, 1]
            for i in range(2, n):
                fibs.append(fibs[-1] + fibs[-2])
            return fibs[:n]

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Euclidean GCD algorithm - O(log min(a,b))"""
        steps = 0
        while b:
            a, b = b, a % b
            steps += 1
        return a, steps

    @staticmethod
    def power(base: float, exp: int) -> float:
        """Fast exponentiation - O(log n)"""
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        return result

    @staticmethod
    def is_prime(n: int) -> Tuple[bool, int]:
        """Primality test - O(√n)"""
        if n < 2:
            return False, 0
        if n == 2:
            return True, 1
        if n % 2 == 0:
            return False, 1

        checks = 0
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            checks += 1
            if n % i == 0:
                return False, checks
        return True, checks

    @staticmethod
    def sieve_of_eratosthenes(n: int) -> List[int]:
        """Find all primes up to n - O(n log log n)"""
        if n < 2:
            return []

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False

        return [i for i in range(2, n + 1) if is_prime[i]]

    @staticmethod
    def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
        """Matrix multiplication - O(n³) for naive"""
        n = len(A)
        m = len(B[0])
        p = len(B)

        result = [[0.0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for k in range(p):
                    result[i][j] += A[i][k] * B[k][j]

        return result

    @staticmethod
    def big_o_notation():
        """Display Big-O complexity reference"""
        complexities = [
            ("O(1)", "Constant", "Array access, hash table lookup"),
            ("O(log n)", "Logarithmic", "Binary search, balanced BST"),
            ("O(√n)", "Square root", "Prime checking, some optimizations"),
            ("O(n)", "Linear", "Linear search, array traversal"),
            ("O(n log n)", "Linearithmic", "Merge sort, heap sort, Dijkstra"),
            ("O(n²)", "Quadratic", "Bubble sort, matrix multiplication"),
            ("O(n³)", "Cubic", "Floyd-Warshall, naive matrix mult"),
            ("O(2^n)", "Exponential", "Recursive Fibonacci, subsets"),
            ("O(n!)", "Factorial", "Traveling salesman, permutations"),
        ]

        print(f"\n{Colors.CYAN}{Colors.BOLD}[BIG-O COMPLEXITY REFERENCE]{Colors.END}")
        print(f"{'Notation':<12} {'Name':<18} {'Examples'}{Colors.END}")
        print("-" * 60)
        for notation, name, examples in complexities:
            print(f"{Colors.GREEN}{notation:<12}{Colors.END} {name:<18} {examples}")

# ============================================================
# SPEED BENCHMARK SUITE
# ============================================================
class BenchmarkSuite:
    """Advanced benchmarking and speed analysis suite"""

    def __init__(self):
        self.results = []

    def benchmark_search(self, sizes: List[int] = [100, 1000, 5000, 10000]) -> List[Dict]:
        """Benchmark searching algorithms across different input sizes"""
        print(f"\n{Colors.PURPLE}{Colors.BOLD}[SEARCH SPEED BENCHMARK]{Colors.END}")
        print(f"{Colors.DIM}Testing across multiple input sizes...{Colors.END}\n")

        searcher = SearchingAlgorithms()
        all_results = []

        for size in sizes:
            arr = sorted(random.sample(range(size * 2), size))
            target = random.choice(arr)

            algorithms = [
                ('Linear', searcher.linear_search),
                ('Binary', searcher.binary_search_iterative),
                ('Jump', searcher.jump_search),
                ('Interpolation', searcher.interpolation_search),
                ('Exponential', searcher.exponential_search),
            ]

            size_results = {'size': size, 'times': {}}
            for name, algo in algorithms:
                # Warmup
                algo(arr.copy(), target)
                # Benchmark
                times = []
                for _ in range(5):
                    start = time.perf_counter()
                    algo(arr.copy(), target)
                    times.append((time.perf_counter() - start) * 1000)
                size_results['times'][name] = sum(times) / len(times)

            all_results.append(size_results)

        # Print table
        print(f"{Colors.CYAN}{Colors.BOLD}{'Size':<10} {'Linear':<12} {'Binary':<12} {'Jump':<12} {'Interp':<12} {'Exp':<12}{Colors.END}")
        print(f"{Colors.CHARCOAL}{'─' * 75}{Colors.END}")
        for r in all_results:
            print(f"{r['size']:<10} " + " ".join(f"{r['times'][k]:<12.4f}" for k in ['Linear', 'Binary', 'Jump', 'Interpolation', 'Exponential']))

        return all_results

    def benchmark_sort(self, sizes: List[int] = [100, 500, 1000, 2000]) -> List[Dict]:
        """Benchmark sorting algorithms across different input sizes"""
        print(f"\n{Colors.PURPLE}{Colors.BOLD}[SORT SPEED BENCHMARK]{Colors.END}")
        print(f"{Colors.DIM}Testing across multiple input sizes...{Colors.END}\n")

        sorter = SortingAlgorithms()
        all_results = []

        for size in sizes:
            arr = [random.randint(0, size) for _ in range(size)]

            algorithms = [
                ('Bubble', sorter.bubble_sort),
                ('Insertion', sorter.insertion_sort),
                ('Merge', sorter.merge_sort),
                ('Quick', sorter.quick_sort),
                ('Heap', sorter.heap_sort),
                ('Shell', sorter.shell_sort),
            ]

            size_results = {'size': size, 'times': {}}
            for name, algo in algorithms:
                if size > 1000 and name in ['Bubble', 'Insertion']:
                    size_results['times'][name] = float('inf')
                    continue
                test_arr = arr.copy()
                start = time.perf_counter()
                algo(test_arr)
                size_results['times'][name] = (time.perf_counter() - start) * 1000

            all_results.append(size_results)

        # Print table
        print(f"{Colors.CYAN}{Colors.BOLD}{'Size':<10} {'Bubble':<12} {'Insertion':<12} {'Merge':<12} {'Quick':<12} {'Heap':<12} {'Shell':<12}{Colors.END}")
        print(f"{Colors.CHARCOAL}{'─' * 85}{Colors.END}")
        for r in all_results:
            row = f"{r['size']:<10} "
            for k in ['Bubble', 'Insertion', 'Merge', 'Quick', 'Heap', 'Shell']:
                val = r['times'][k]
                row += f"{'INF' if val == float('inf') else f'{val:<12.4f}'}"
            print(row)

        return all_results

# ============================================================
# FUTURISTIC UI RENDERER
# ============================================================
class FuturisticUI:
    """Advanced futuristic UI rendering with cyberpunk aesthetics"""

    @staticmethod
    def draw_box(title: str, content: List[str], width: int = 70):
        """Draw a futuristic box panel"""
        c = Colors
        print(f"\n{c.CYAN}{c.BOLD}{c.TOP_LEFT}{c.HORIZ * (width - 2)}{c.TOP_RIGHT}{c.END}")
        print(f"{c.CYAN}{c.BOLD}{c.VERT}{c.END} {c.BRIGHT_CYAN}{title:<{width - 4}}{c.END} {c.CYAN}{c.BOLD}{c.VERT}{c.END}")
        print(f"{c.CYAN}{c.BOLD}{c.T_RIGHT}{c.HORIZ * (width - 2)}{c.T_LEFT}{c.END}")
        for line in content:
            print(f"{c.CYAN}{c.BOLD}{c.VERT}{c.END} {line:<{width - 4}}{c.END} {c.CYAN}{c.BOLD}{c.VERT}{c.END}")
        print(f"{c.CYAN}{c.BOLD}{c.BOT_LEFT}{c.HORIZ * (width - 2)}{c.BOT_RIGHT}{c.END}")

    @staticmethod
    def draw_progress_bar(label: str, percent: float, width: int = 40):
        """Draw a futuristic progress bar"""
        c = Colors
        filled = int(width * percent / 100)
        bar = f"{c.CYAN}{'█' * filled}{c.CHARCOAL}{'░' * (width - filled)}{c.END}"
        print(f"  {c.GRAY}{label:<15}{c.END} {bar} {c.CYAN}{percent:>5.1f}%{c.END}")

    @staticmethod
    def print_header(text: str):
        c = Colors
        print(f"\n{c.CYAN}{c.BOLD}{'═' * 72}{c.END}")
        print(f"{c.CYAN}{c.BOLD}  ▶ {text.upper()}{c.END}")
        print(f"{c.CYAN}{c.BOLD}{'═' * 72}{c.END}")

    @staticmethod
    def print_subheader(text: str):
        c = Colors
        print(f"\n{c.BRIGHT_CYAN}{c.BOLD}  ▸ {text}{c.END}")
        print(f"{c.CHARCOAL}{'─' * 50}{c.END}")

    @staticmethod
    def print_success(text: str):
        print(f"  {Colors.BRIGHT_GREEN}✓ {text}{Colors.END}")

    @staticmethod
    def print_warning(text: str):
        print(f"  {Colors.GOLD}⚠ {text}{Colors.END}")

    @staticmethod
    def print_error(text: str):
        print(f"  {Colors.RED}✗ {text}{Colors.END}")

    @staticmethod
    def print_info(text: str):
        print(f"  {Colors.GRAY}ℹ {text}{Colors.END}")

# ============================================================
# MAIN APPLICATION CLASS - ULTRA ADVANCED
# ============================================================
class AlgorithmAnalyzerApp:
    def __init__(self):
        self.analyzer = AlgorithmAnalyzer()
        self.calculator = MathCalculator()
        self.searcher = SearchingAlgorithms()
        self.sorter = SortingAlgorithms()
        self.benchmark = BenchmarkSuite()
        self.ui = FuturisticUI()
        self.current_graph = None
        self.history = []
        self.switch_menus = {}
        self._build_switch_menus()

    def _build_switch_menus(self):
        """Build switch-case style menu dispatchers"""
        # Main menu switch
        self.switch_menus['main'] = {
            '1': self.create_graph_menu,
            '2': lambda: self._run_graph_algo('bfs'),
            '3': lambda: self._run_graph_algo('dfs'),
            '4': lambda: self._run_graph_algo('dijkstra'),
            '5': lambda: self._run_graph_algo('floyd'),
            '6': lambda: self._run_graph_algo('longest'),
            '7': lambda: self._run_graph_algo('mst'),
            '8': lambda: self._run_graph_algo('bellman'),
            '9': self.run_comparison,
            '10': self.searching_menu,
            '11': self.sorting_menu,
            '12': self.math_calculator_menu,
            '13': self.complexity_reference,
            '14': self.visualize_graph,
            '15': self.benchmark_menu,
            '16': self.speed_analysis,
            '17': self.save_load_menu,
            '18': self.generate_report,
            'Q': self.quit_app,
            'q': self.quit_app,
        }

        # Graph submenu switch
        self.switch_menus['graph'] = {
            '1': self._create_random_graph,
            '2': self._create_custom_graph,
            '3': self._load_graph_file,
            '4': self._display_graph,
            '5': self._graph_properties,
            'B': lambda: None,
            'b': lambda: None,
        }

        # MST submenu switch
        self.switch_menus['mst'] = {
            '1': lambda: self._run_mst('prim'),
            '2': lambda: self._run_mst('kruskal'),
            'B': lambda: None,
            'b': lambda: None,
        }

    def print_banner(self):
        os.system('clear' if os.name != 'nt' else 'cls')
        c = Colors
        banner = f"""
{c.CYAN}{c.BOLD}
    ██╗   ██╗███████╗███████╗██╗   ██╗    █████╗ ██╗      ██████╗  ██████╗ 
    ██║   ██║██╔════╝██╔════╝██║   ██║   ██╔══██╗██║     ██╔═══██╗██╔════╝ 
    ██║   ██║███████╗███████╗██║   ██║   ███████║██║     ██║   ██║██║  ███╗
    ██║   ██║╚════██║╚════██║██║   ██║   ██╔══██║██║     ██║   ██║██║   ██║
    ╚██████╔╝███████║███████║╚██████╔╝   ██║  ██║███████╗╚██████╔╝╚██████╔╝
     ╚═════╝ ╚══════╝╚══════╝ ╚═════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ 
{c.END}
{c.BRIGHT_CYAN}{c.BOLD}         ╔═══════════════════════════════════════════════════════════════╗
         ║     USSU'S ULTRA PRO MAX ALGORITHM ANALYZER v4.0              ║
         ║     Graph Theory | Search | Sort | ADA | Speed Benchmark      ║
         ║     github.com/issu321 | Kali Linux | Python 3.13             ║
         ╚═══════════════════════════════════════════════════════════════╝{c.END}
{c.GRAY}
         [ SYSTEM: {platform.system()} {platform.release()} ]
         [ PYTHON: {platform.python_version()} ]
         [ MATPLOTLIB: {'YES' if MATPLOTLIB_AVAILABLE else 'NO'} ]
         [ NETWORKX: {'YES' if NETWORKX_AVAILABLE else 'NO'} ]
         [ NUMPY: {'YES' if NUMPY_AVAILABLE else 'NO'} ]
{c.END}
        """
        print(banner)
        time.sleep(0.8)

    def print_main_menu(self):
        c = Colors
        menu_lines = [
            f"{c.GREEN}[1]{c.END}  {c.WHITE}Graph Operations        {c.GRAY}- Create, load, display graphs{c.END}",
            f"{c.GREEN}[2]{c.END}  {c.WHITE}BFS Traversal           {c.GRAY}- Breadth First Search{c.END}",
            f"{c.GREEN}[3]{c.END}  {c.WHITE}DFS Traversal           {c.GRAY}- Depth First Search{c.END}",
            f"{c.GREEN}[4]{c.END}  {c.WHITE}Shortest Path (Dijkstra){c.GRAY}- Single source shortest path{c.END}",
            f"{c.GREEN}[5]{c.END}  {c.WHITE}All Pairs Shortest Path {c.GRAY}- Floyd-Warshall algorithm{c.END}",
            f"{c.GREEN}[6]{c.END}  {c.WHITE}Longest Path (DAG)      {c.GRAY}- Critical path analysis{c.END}",
            f"{c.GREEN}[7]{c.END}  {c.WHITE}Minimum Spanning Tree   {c.GRAY}- Prim's & Kruskal's{c.END}",
            f"{c.GREEN}[8]{c.END}  {c.WHITE}Bellman-Ford            {c.GRAY}- Negative weight handling{c.END}",
            f"{c.GREEN}[9]{c.END}  {c.WHITE}Compare Graph Algos     {c.GRAY}- Performance comparison{c.END}",
            f"{c.GREEN}[10]{c.END} {c.WHITE}Searching Algorithms    {c.GRAY}- Linear, Binary, Jump, etc.{c.END}",
            f"{c.GREEN}[11]{c.END} {c.WHITE}Sorting Algorithms      {c.GRAY}- Bubble, Merge, Quick, etc.{c.END}",
            f"{c.GREEN}[12]{c.END} {c.WHITE}Math Calculator         {c.GRAY}- Advanced mathematical tools{c.END}",
            f"{c.GREEN}[13]{c.END} {c.WHITE}Complexity Reference    {c.GRAY}- Big-O notation guide{c.END}",
            f"{c.GREEN}[14]{c.END} {c.WHITE}Visualize Graph         {c.GRAY}- Matplotlib/NetworkX plot{c.END}",
            f"{c.GREEN}[15]{c.END} {c.WHITE}Benchmark Suite         {c.GRAY}- Speed benchmark tests{c.END}",
            f"{c.GREEN}[16]{c.END} {c.WHITE}Speed Analysis          {c.GRAY}- Algorithm speed profiling{c.END}",
            f"{c.GREEN}[17]{c.END} {c.WHITE}Save/Load Graph         {c.GRAY}- Persist graph to file{c.END}",
            f"{c.GREEN}[18]{c.END} {c.WHITE}Generate Report         {c.GRAY}- Export analysis report{c.END}",
            f"{c.RED}[Q]{c.END}  {c.WHITE}Quit                    {c.GRAY}- Exit application{c.END}",
        ]
        self.ui.draw_box("ALGORITHM ANALYZER COMMAND CENTER v4.0", menu_lines, 78)

    # ==================== SWITCH CASE GRAPH OPERATIONS ====================
    def create_graph_menu(self):
        """Graph creation submenu with switch case"""
        self.ui.print_header("Graph Operations")
        print(f"\n{Colors.GREEN}[1]{Colors.END} Create Random Graph")
        print(f"{Colors.GREEN}[2]{Colors.END} Create Custom Graph (manual input)")
        print(f"{Colors.GREEN}[3]{Colors.END} Load Graph from File")
        print(f"{Colors.GREEN}[4]{Colors.END} Display Current Graph")
        print(f"{Colors.GREEN}[5]{Colors.END} Graph Properties (degree, density)")
        print(f"{Colors.GREEN}[B]{Colors.END} Back")

        choice = input(f"\n{Colors.YELLOW}Select: {Colors.END}").strip().upper()
        action = self.switch_menus['graph'].get(choice)
        if action:
            action()
        else:
            self.ui.print_error("Invalid choice")

    def _create_random_graph(self):
        n = int(input(f"{Colors.YELLOW}Number of vertices: {Colors.END}") or "5")
        edge_prob = float(input(f"{Colors.YELLOW}Edge probability (0-1, default 0.3): {Colors.END}") or "0.3")
        directed = input(f"{Colors.YELLOW}Directed? (y/n): {Colors.END}").strip().lower() == 'y'
        weighted = input(f"{Colors.YELLOW}Weighted? (y/n): {Colors.END}").strip().lower() == 'y'

        self.current_graph = Graph.from_random(n, edge_prob, directed, weighted)
        self.ui.print_success("Random graph created!")
        self.current_graph.display()

    def _create_custom_graph(self):
        self.current_graph = Graph()
        directed = input(f"{Colors.YELLOW}Directed? (y/n): {Colors.END}").strip().lower() == 'y'
        weighted = input(f"{Colors.YELLOW}Weighted? (y/n): {Colors.END}").strip().lower() == 'y'
        self.current_graph.directed = directed
        self.current_graph.weighted = weighted

        print(f"{Colors.YELLOW}Enter edges (format: u v [weight], empty line to finish):{Colors.END}")
        while True:
            line = input().strip()
            if not line:
                break
            parts = line.split()
            if len(parts) >= 2:
                u, v = int(parts[0]), int(parts[1])
                w = float(parts[2]) if len(parts) > 2 and weighted else None
                self.current_graph.add_edge(u, v, w)

        self.ui.print_success("Custom graph created!")
        self.current_graph.display()

    def _load_graph_file(self):
        filepath = input(f"{Colors.YELLOW}File path: {Colors.END}").strip()
        if os.path.exists(filepath):
            self.current_graph = Graph.from_file(filepath)
            self.ui.print_success("Graph loaded!")
            self.current_graph.display()
        else:
            self.ui.print_error("File not found")

    def _display_graph(self):
        if self.current_graph:
            self.current_graph.display()
        else:
            self.ui.print_error("No graph created yet")

    def _graph_properties(self):
        if not self.current_graph:
            self.ui.print_error("No graph created yet")
            return

        g = self.current_graph
        n = len(g.vertices)
        m = g.edge_count

        self.ui.print_subheader("Graph Properties")
        print(f"  {Colors.WHITE}Vertices (V):{Colors.END} {Colors.CYAN}{n}{Colors.END}")
        print(f"  {Colors.White}Edges (E):{Colors.END} {Colors.CYAN}{m}{Colors.END}")
        print(f"  {Colors.WHITE}Density:{Colors.END} {Colors.CYAN}{2*m/(n*(n-1)) if n > 1 else 0:.4f}{Colors.END}")
        print(f"  {Colors.WHITE}Type:{Colors.END} {Colors.CYAN}{'Directed' if g.directed else 'Undirected'}{Colors.END}")
        print(f"  {Colors.WHITE}Weighted:{Colors.END} {Colors.CYAN}{'Yes' if g.weighted else 'No'}{Colors.END}")

        self.ui.print_subheader("Degree Distribution")
        for v in sorted(g.vertices):
            deg = g.get_degree(v)
            self.ui.draw_progress_bar(f"Vertex {v}", min(deg * 100 / max(n-1, 1), 100))

    # ==================== SWITCH CASE GRAPH ALGORITHMS ====================
    def _run_graph_algo(self, algo_type: str):
        if not self.current_graph:
            self.ui.print_error("Please create a graph first (Option 1)")
            return

        start = int(input(f"{Colors.YELLOW}Start vertex: {Colors.END}") or "0")
        target = input(f"{Colors.YELLOW}Target vertex (optional): {Colors.END}").strip()
        target = int(target) if target else None

        algo_map = {
            'bfs': self.analyzer.bfs,
            'dfs': self.analyzer.dfs,
            'dijkstra': self.analyzer.dijkstra,
            'floyd': self.analyzer.floyd_warshall,
            'longest': self.analyzer.longest_path_dag,
            'bellman': self.analyzer.bellman_ford,
        }

        if algo_type == 'mst':
            self.ui.print_header("Minimum Spanning Tree")
            print(f"\n{Colors.GREEN}[1]{Colors.END} Prim's Algorithm")
            print(f"{Colors.GREEN}[2]{Colors.END} Kruskal's Algorithm")
            print(f"{Colors.GREEN}[B]{Colors.END} Back")
            mst_choice = input(f"\n{Colors.YELLOW}Select: {Colors.END}").strip().upper()
            action = self.switch_menus['mst'].get(mst_choice)
            if action:
                action()
            return

        algo_func = algo_map.get(algo_type)
        if algo_func:
            if algo_type == 'floyd':
                result = algo_func(self.current_graph)
            elif algo_type == 'longest':
                result = algo_func(self.current_graph, start)
            elif algo_type == 'bellman':
                result = algo_func(self.current_graph, start)
            else:
                result = algo_func(self.current_graph, start, target)
            self.history.append(result)

    def _run_mst(self, mst_type: str):
        if mst_type == 'prim':
            result = self.analyzer.prim_mst(self.current_graph)
        else:
            result = self.analyzer.kruskal_mst(self.current_graph)
        self.history.append(result)

    def run_comparison(self):
        if not self.current_graph:
            self.ui.print_error("Please create a graph first")
            return
        start = int(input(f"{Colors.YELLOW}Start vertex: {Colors.END}") or "0")
        self.analyzer.compare_algorithms(self.current_graph, start)

    # ==================== SEARCHING MENU (SWITCH CASE) ====================
    def searching_menu(self):
        self.ui.print_header("Searching Algorithms")

        search_switch = {
            '1': self.searcher.linear_search,
            '2': self.searcher.binary_search_iterative,
            '3': self.searcher.binary_search_recursive,
            '4': self.searcher.jump_search,
            '5': self.searcher.interpolation_search,
            '6': self.searcher.exponential_search,
            '7': self.searcher.ternary_search,
            '8': self.searcher.fibonacci_search,
            '9': self.searcher.compare_all_searches,
            'B': lambda: None,
            'b': lambda: None,
        }

        print(f"\n{Colors.GREEN}[1]{Colors.END} Linear Search          {Colors.GRAY}- O(n){Colors.END}")
        print(f"{Colors.GREEN}[2]{Colors.END} Binary Search (Iter)   {Colors.GRAY}- O(log n){Colors.END}")
        print(f"{Colors.GREEN}[3]{Colors.END} Binary Search (Rec)    {Colors.GRAY}- O(log n){Colors.END}")
        print(f"{Colors.GREEN}[4]{Colors.END} Jump Search            {Colors.GRAY}- O(√n){Colors.END}")
        print(f"{Colors.GREEN}[5]{Colors.END} Interpolation Search   {Colors.GRAY}- O(log log n){Colors.END}")
        print(f"{Colors.GREEN}[6]{Colors.END} Exponential Search     {Colors.GRAY}- O(log n){Colors.END}")
        print(f"{Colors.GREEN}[7]{Colors.END} Ternary Search         {Colors.GRAY}- O(log₃ n){Colors.END}")
        print(f"{Colors.GREEN}[8]{Colors.END} Fibonacci Search       {Colors.GRAY}- O(log n){Colors.END}")
        print(f"{Colors.GREEN}[9]{Colors.END} Compare All Searches   {Colors.GRAY}- Benchmark suite{Colors.END}")
        print(f"{Colors.GREEN}[B]{Colors.END} Back")

        choice = input(f"\n{Colors.YELLOW}Select: {Colors.END}").strip().upper()
        action = search_switch.get(choice)

        if not action:
            self.ui.print_error("Invalid choice")
            return
        if choice in ['B', 'b']:
            return

        if choice == '9':
            size = int(input(f"{Colors.YELLOW}Array size for benchmark: {Colors.END}") or "1000")
            arr = sorted(random.sample(range(size * 2), size))
            target = random.choice(arr)
            action(arr, target)
        else:
            input_str = input(f"{Colors.YELLOW}Enter sorted numbers (space separated): {Colors.END}").strip()
            arr = list(map(int, input_str.split())) if input_str else sorted(random.sample(range(100), 20))
            target = int(input(f"{Colors.YELLOW}Target to search: {Colors.END}"))
            result = action(arr, target)
            if result:
                self.history.append(result)

    # ==================== SORTING MENU (SWITCH CASE) ====================
    def sorting_menu(self):
        self.ui.print_header("Sorting Algorithms")

        sort_switch = {
            '1': self.sorter.bubble_sort,
            '2': self.sorter.selection_sort,
            '3': self.sorter.insertion_sort,
            '4': self.sorter.merge_sort,
            '5': self.sorter.quick_sort,
            '6': self.sorter.heap_sort,
            '7': self.sorter.shell_sort,
            '8': self.sorter.cocktail_shaker_sort,
            '9': self.sorter.comb_sort,
            '10': self.sorter.counting_sort,
            '11': self.sorter.radix_sort,
            '12': self.sorter.compare_all_sorts,
            'B': lambda: None,
            'b': lambda: None,
        }

        print(f"\n{Colors.GREEN}[1]{Colors.END}  Bubble Sort            {Colors.GRAY}- O(n²) | Stable{c.END}")
        print(f"{Colors.GREEN}[2]{Colors.END}  Selection Sort         {Colors.GRAY}- O(n²) | Unstable{c.END}")
        print(f"{Colors.GREEN}[3]{Colors.END}  Insertion Sort         {Colors.GRAY}- O(n²) | Stable{c.END}")
        print(f"{Colors.GREEN}[4]{Colors.END}  Merge Sort             {Colors.GRAY}- O(n log n) | Stable{c.END}")
        print(f"{Colors.GREEN}[5]{Colors.END}  Quick Sort             {Colors.GRAY}- O(n log n) | Unstable{c.END}")
        print(f"{Colors.GREEN}[6]{Colors.END}  Heap Sort              {Colors.GRAY}- O(n log n) | Unstable{c.END}")
        print(f"{Colors.GREEN}[7]{Colors.END}  Shell Sort             {Colors.GRAY}- O(n log² n) | Unstable{c.END}")
        print(f"{Colors.GREEN}[8]{Colors.END}  Cocktail Shaker Sort   {Colors.GRAY}- O(n²) | Stable{c.END}")
        print(f"{Colors.GREEN}[9]{Colors.END}  Comb Sort              {Colors.GRAY}- O(n²/2^p) | Unstable{c.END}")
        print(f"{Colors.GREEN}[10]{Colors.END} Counting Sort          {Colors.GRAY}- O(n+k) | Stable{c.END}")
        print(f"{Colors.GREEN}[11]{Colors.END} Radix Sort             {Colors.GRAY}- O(d(n+k)) | Stable{c.END}")
        print(f"{Colors.GREEN}[12]{Colors.END} Compare All Sorts      {Colors.GRAY}- Benchmark suite{c.END}")
        print(f"{Colors.GREEN}[B]{Colors.END}  Back")

        choice = input(f"\n{Colors.YELLOW}Select: {Colors.END}").strip().upper()
        action = sort_switch.get(choice)

        if not action:
            self.ui.print_error("Invalid choice")
            return
        if choice in ['B', 'b']:
            return

        if choice == '12':
            size = int(input(f"{Colors.YELLOW}Array size for benchmark: {Colors.END}") or "1000")
            arr = [random.randint(0, size) for _ in range(size)]
            action(arr)
        else:
            input_str = input(f"{Colors.YELLOW}Enter numbers (space separated): {Colors.END}").strip()
            if input_str:
                arr = list(map(int, input_str.split()))
            else:
                size = int(input(f"{Colors.YELLOW}Random array size: {Colors.END}") or "20")
                arr = [random.randint(0, 100) for _ in range(size)]

            result = action(arr)
            if result:
                self.history.append(result)

    # ==================== BENCHMARK & SPEED ====================
    def benchmark_menu(self):
        self.ui.print_header("Benchmark Suite")
        print(f"\n{Colors.GREEN}[1]{Colors.END} Search Benchmark")
        print(f"{Colors.GREEN}[2]{Colors.END} Sort Benchmark")
        print(f"{Colors.GREEN}[B]{Colors.END} Back")

        choice = input(f"\n{Colors.YELLOW}Select: {Colors.END}").strip().upper()
        if choice == '1':
            sizes = input(f"{Colors.YELLOW}Sizes (comma separated, default 100,1000,5000): {Colors.END}").strip()
            sizes = [int(x) for x in sizes.split(',')] if sizes else [100, 1000, 5000]
            self.benchmark.benchmark_search(sizes)
        elif choice == '2':
            sizes = input(f"{Colors.YELLOW}Sizes (comma separated, default 100,500,1000): {Colors.END}").strip()
            sizes = [int(x) for x in sizes.split(',')] if sizes else [100, 500, 1000]
            self.benchmark.benchmark_sort(sizes)

    def speed_analysis(self):
        self.ui.print_header("Algorithm Speed Analysis")
        print(f"\n{Colors.GRAY}Speed profiling analyzes algorithm performance characteristics:{Colors.END}")
        print(f"  • Execution time in milliseconds")
        print(f"  • Memory usage in KB")
        print(f"  • Operation counters (comparisons, swaps, accesses)")
        print(f"  • Time complexity verification")
        print(f"\n{Colors.YELLOW}Use options 10-12 to run algorithms with speed profiling enabled.{Colors.END}")

    # ==================== EXISTING FEATURES ====================
    def math_calculator_menu(self):
        self.ui.print_header("Advanced Mathematical Calculator")
        print(f"\n{Colors.GREEN}[1]{Colors.END} Factorial (n!)")
        print(f"{Colors.GREEN}[2]{Colors.END} Fibonacci Sequence")
        print(f"{Colors.GREEN}[3]{Colors.END} GCD (Euclidean)")
        print(f"{Colors.GREEN}[4]{Colors.END} Fast Exponentiation")
        print(f"{Colors.GREEN}[5]{Colors.END} Prime Check")
        print(f"{Colors.GREEN}[6]{Colors.END} Sieve of Eratosthenes")
        print(f"{Colors.GREEN}[7]{Colors.END} Matrix Multiplication")
        print(f"{Colors.GREEN}[8]{Colors.END} Big-O Reference")
        print(f"{Colors.GREEN}[B]{Colors.END} Back")

        choice = input(f"\n{Colors.YELLOW}Select: {Colors.END}").strip().upper()

        if choice == 'B':
            return
        elif choice == '1':
            n = int(input(f"{Colors.YELLOW}Enter n: {Colors.END}"))
            result = self.calculator.factorial(n)
            print(f"{Colors.GREEN}{n}! = {result}{Colors.END}")
            print(f"{Colors.DIM}Time: O(n) | Space: O(1){Colors.END}")

        elif choice == '2':
            n = int(input(f"{Colors.YELLOW}Enter n: {Colors.END}"))
            method = input(f"{Colors.YELLOW}Method (iterative/memoization/recursive): {Colors.END}").strip()
            result = self.calculator.fibonacci(n, method)
            print(f"{Colors.GREEN}Fibonacci: {result}{Colors.END}")
            if method == "recursive":
                print(f"{Colors.RED}Time: O(2^n) - Very slow for large n!{Colors.END}")
            else:
                print(f"{Colors.DIM}Time: O(n) | Space: O(n){Colors.END}")

        elif choice == '3':
            a = int(input(f"{Colors.YELLOW}Enter a: {Colors.END}"))
            b = int(input(f"{Colors.YELLOW}Enter b: {Colors.END}"))
            result, steps = self.calculator.gcd(a, b)
            print(f"{Colors.GREEN}GCD({a}, {b}) = {result}{Colors.END}")
            print(f"{Colors.DIM}Steps: {steps} | Time: O(log min(a,b)){Colors.END}")

        elif choice == '4':
            base = float(input(f"{Colors.YELLOW}Base: {Colors.END}"))
            exp = int(input(f"{Colors.YELLOW}Exponent: {Colors.END}"))
            result = self.calculator.power(base, exp)
            print(f"{Colors.GREEN}{base}^{exp} = {result}{Colors.END}")
            print(f"{Colors.DIM}Time: O(log n){Colors.END}")

        elif choice == '5':
            n = int(input(f"{Colors.YELLOW}Enter n: {Colors.END}"))
            is_prime, checks = self.calculator.is_prime(n)
            print(f"{Colors.GREEN}{n} is {'prime' if is_prime else 'not prime'}{Colors.END}")
            print(f"{Colors.DIM}Checks: {checks} | Time: O(√n){Colors.END}")

        elif choice == '6':
            n = int(input(f"{Colors.YELLOW}Find primes up to: {Colors.END}"))
            primes = self.calculator.sieve_of_eratosthenes(n)
            print(f"{Colors.GREEN}Primes up to {n}: {primes}{Colors.END}")
            print(f"{Colors.DIM}Count: {len(primes)} | Time: O(n log log n){Colors.END}")

        elif choice == '7':
            print(f"{Colors.YELLOW}Enter matrix A (rows separated by ;, elements by space):{Colors.END}")
            A = []
            for _ in range(2):
                row = list(map(float, input().split()))
                A.append(row)

            print(f"{Colors.YELLOW}Enter matrix B:{Colors.END}")
            B = []
            for _ in range(2):
                row = list(map(float, input().split()))
                B.append(row)

            result = self.calculator.matrix_multiply(A, B)
            print(f"{Colors.GREEN}Result:{Colors.END}")
            for row in result:
                print(f"  {row}")
            print(f"{Colors.DIM}Time: O(n³) | Space: O(n²){Colors.END}")

        elif choice == '8':
            self.calculator.big_o_notation()

    def complexity_reference(self):
        self.calculator.big_o_notation()

    def visualize_graph(self):
        if not MATPLOTLIB_AVAILABLE or not NETWORKX_AVAILABLE:
            self.ui.print_error("matplotlib and networkx required")
            print(f"{Colors.YELLOW}[!] Install: pip install matplotlib networkx{Colors.END}")
            return

        if not self.current_graph:
            self.ui.print_error("No graph to visualize")
            return

        print(f"{Colors.CYAN}[*] Generating visualization...{Colors.END}")

        G = nx.DiGraph() if self.current_graph.directed else nx.Graph()

        for v in self.current_graph.vertices:
            G.add_node(v)

        for u, v, w in self.current_graph.edges:
            weight = w if w is not None else 1
            G.add_edge(u, v, weight=weight)

        plt.figure(figsize=(12, 9), facecolor='#0f172a')
        pos = nx.spring_layout(G, k=2, iterations=50)

        nx.draw_networkx_nodes(G, pos, node_color='#06b6d4', node_size=1000, 
                              edgecolors='white', linewidths=2)
        nx.draw_networkx_labels(G, pos, font_color='white', font_size=12, font_weight='bold')

        edge_color = '#8b5cf6' if self.current_graph.directed else '#10b981'
        nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=2.5, 
                              arrows=self.current_graph.directed, 
                              arrowsize=25, alpha=0.8, connectionstyle='arc3,rad=0.1' if self.current_graph.directed else None)

        if self.current_graph.weighted:
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, 
                                        font_color='#fbbf24', font_size=10, font_weight='bold')

        plt.title(f"USSU Graph Visualizer | {'Directed' if self.current_graph.directed else 'Undirected'} | "
                 f"{len(self.current_graph.vertices)}V {self.current_graph.edge_count}E",
                 color='white', fontsize=16, fontweight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout()

        os.makedirs('graphs', exist_ok=True)
        filename = f"graphs/graph_viz_{int(time.time())}.png"
        plt.savefig(filename, dpi=150, facecolor='#0f172a', edgecolor='none', bbox_inches='tight')
        self.ui.print_success(f"Saved: {filename}")
        plt.show()

    def save_load_menu(self):
        self.create_graph_menu()

    def generate_report(self):
        if not self.history:
            self.ui.print_error("No analysis history to report")
            return

        os.makedirs('reports', exist_ok=True)
        filename = f"reports/analysis_report_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write("=" * 70 + "\n")
            f.write("  USSU'S ULTRA ALGORITHM ANALYZER - ANALYSIS REPORT\n")
            f.write(f"  Author: Ussu | github.com/issu321\n")
            f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 70 + "\n\n")

            for i, entry in enumerate(self.history, 1):
                f.write(f"Analysis #{i}\n")
                f.write("-" * 40 + "\n")
                for key, value in entry.items():
                    f.write(f"  {key}: {value}\n")
                f.write("\n")

        self.ui.print_success(f"Report saved: {filename}")

    def quit_app(self):
        print(f"\n{Colors.CYAN}{Colors.BOLD}[+] USSU Algorithm Analyzer v4.0 offline. Goodbye!{Colors.END}\n")
        sys.exit(0)

    def run(self):
        """Main application loop with switch case dispatch"""
        self.print_banner()

        while True:
            self.print_main_menu()
            choice = input(f"\n{Colors.CYAN}{Colors.BOLD}[USSU v4.0]{Colors.END} {Colors.YELLOW}Enter choice: {Colors.END}").strip().upper()

            action = self.switch_menus['main'].get(choice)
            if action:
                try:
                    action()
                except Exception as e:
                    self.ui.print_error(f"Error: {e}")
            else:
                self.ui.print_error("Invalid choice. Please try again.")


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    try:
        app = AlgorithmAnalyzerApp()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.CYAN}{Colors.BOLD}[+] Interrupted by user.{Colors.END}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[!] Fatal error: {e}{Colors.END}\n")
        sys.exit(1)

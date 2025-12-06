"""
Python implementation: Matrix determinant calculation
Generates a 4x4 matrix with random values (1-9) and calculates its determinant.
Measures execution time and memory usage.
"""

import numpy as np
import time
import tracemalloc
import sys

def generate_matrix(rows=4, cols=4, min_val=1, max_val=9):
    """Generate a random matrix with specified dimensions and value range."""
    return np.random.randint(min_val, max_val + 1, size=(rows, cols))

def calculate_determinant(matrix):
    """Calculate determinant using NumPy's linear algebra module."""
    return np.linalg.det(matrix)

def main():
    print("=" * 60)
    print("Python Implementation: Matrix Determinant Calculation")
    print("=" * 60)
    
    # Start memory tracking
    tracemalloc.start()
    
    # Start time measurement
    start_time = time.perf_counter()
    
    # Generate matrix
    matrix = generate_matrix(rows=4, cols=4, min_val=1, max_val=9)
    
    # Calculate determinant
    determinant = calculate_determinant(matrix)
    
    # End time measurement
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    # Get memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Display results
    print("\nGenerated Matrix (4x4, values 1-9):")
    print(matrix)
    print(f"\nDeterminant: {determinant:.6f}")
    print(f"\nExecution Time: {execution_time:.6f} ms")
    print(f"Memory Usage - Current: {current / 1024:.2f} KB, Peak: {peak / 1024:.2f} KB")
    print(f"Python Version: {sys.version}")
    print(f"NumPy Version: {np.__version__}")
    
    return {
        'matrix': matrix,
        'determinant': determinant,
        'execution_time_ms': execution_time,
        'memory_current_kb': current / 1024,
        'memory_peak_kb': peak / 1024
    }

if __name__ == "__main__":
    result = main()


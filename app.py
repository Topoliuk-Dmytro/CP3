"""
Flask web application for matrix determinant calculation with visual interface
"""

from flask import Flask, render_template, jsonify
import numpy as np
import time
import tracemalloc
import sys

app = Flask(__name__)

def generate_matrix(rows=4, cols=4, min_val=1, max_val=9):
    """Generate a random matrix with specified dimensions and value range."""
    return np.random.randint(min_val, max_val + 1, size=(rows, cols))

def calculate_determinant(matrix):
    """Calculate determinant using NumPy's linear algebra module."""
    return np.linalg.det(matrix)

@app.route('/')
def index():
    """Main page with interface."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate determinant and return results."""
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
    
    # Convert matrix to list for JSON
    matrix_list = matrix.tolist()
    
    return jsonify({
        'success': True,
        'matrix': matrix_list,
        'determinant': float(determinant),
        'execution_time_ms': round(execution_time, 6),
        'memory_current_kb': round(current / 1024, 2),
        'memory_peak_kb': round(peak / 1024, 2),
        'python_version': sys.version.split()[0],
        'numpy_version': np.__version__
    })

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)


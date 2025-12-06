"""
Julia implementation: Matrix determinant calculation
Generates a 4x4 matrix with random values (1-9) and calculates its determinant.
Measures execution time and memory usage.
"""

using Random
using LinearAlgebra

function generate_matrix(rows::Int=4, cols::Int=4, min_val::Int=1, max_val::Int=9)
    """Generate a random matrix with specified dimensions and value range."""
    return rand(min_val:max_val, rows, cols)
end

function calculate_determinant(matrix)
    """Calculate determinant using Julia's LinearAlgebra module."""
    return det(matrix)
end

function main()
    println("=" ^ 60)
    println("Julia Implementation: Matrix Determinant Calculation")
    println("=" ^ 60)
    
    # Start memory tracking using @allocated macro for more accurate measurement
    # This measures allocations during execution
    function run_operations()
        # Generate matrix
        matrix = generate_matrix(4, 4, 1, 9)
        
        # Calculate determinant
        determinant = calculate_determinant(matrix)
        
        return matrix, determinant
    end
    
    # Measure memory allocations
    allocated_bytes = @allocated begin
        matrix, determinant = run_operations()
    end
    
    # Measure execution time
    start_time = time_ns()
    matrix, determinant = run_operations()
    end_time = time_ns()
    execution_time = (end_time - start_time) / 1_000_000  # Convert to milliseconds
    
    # Display results
    println("\nGenerated Matrix (4x4, values 1-9):")
    display(matrix)
    println("\nDeterminant: ", determinant)
    println("\nExecution Time: ", execution_time, " ms")
    println("Memory Allocated: ", allocated_bytes / 1024, " KB")
    println("Julia Version: ", VERSION)
    
    return Dict(
        "matrix" => matrix,
        "determinant" => determinant,
        "execution_time_ms" => execution_time,
        "memory_kb" => allocated_bytes / 1024
    )
end

# Run the main function
if abspath(PROGRAM_FILE) == @__FILE__
    result = main()
end


import time

# Initialize the array in Python
size = 700  # Same size as in the C module
data_array = list(range(size))

# Measure time to sum the array using plain Python
start_time = time.time()
result = sum(data_array)
end_time = time.time()

print(f"Result using plain Python: {result}")
print(f"Execution time using plain Python: {end_time - start_time:.10f} seconds")

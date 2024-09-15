import ctypes
import time


# Load the shared C library
lib = ctypes.CDLL('./libfast_add.so')
lib.load_data.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
lib.sum_array.argtypes = [ctypes.c_int]
lib.sum_array.restype = ctypes.c_int

# Initialize the array in Python
size = 700  # You can adjust the size as needed
data_array = (ctypes.c_int * size)(*range(size))

# Load data into the C module
lib.load_data(data_array, size)

# Measure time to sum the array using the C module
start_time = time.time()
result = lib.sum_array(size)
end_time = time.time()

print(f"Result using C module: {result}")
print(f"Execution time using C module: {end_time - start_time:.10f} seconds")

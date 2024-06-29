from cffi import FFI
ffi = FFI()

# Define the C function signature
ffi.cdef("double similarity_cfunc(const char*, const char*, const char*);")

# Set the source code for the C extension
ffi.set_source("_similarity", """
    double similarity_cfunc(const char* a, const char* b, const char* metric) {
        extern double similarity_wrapper(const char*, const char*, const char*);
        return similarity_wrapper(a, b, metric);
    }
""", libraries=["similarity"])

if __name__ == "__main__":
    ffi.compile()

from image_similarity_measures.evaluate import evaluation
import ctypes

def similarity(a, b, metric: str):
    return evaluation(org_img_path=a, 
           pred_img_path=b, 
           metrics=[metric])[metric]

# Wrapper function for ctypes
def similarity_wrapper(a: bytes, b: bytes, metric: bytes) -> float:
    a_str = a.decode('utf-8')
    b_str = b.decode('utf-8')
    metric_str = metric.decode('utf-8')
    return similarity(a_str, b_str, metric_str)

# Create a prototype for the ctypes function
SimilarityFuncType = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
similarity_cfunc = SimilarityFuncType(similarity_wrapper)

if __name__ == "__main__":
    import ctypes
    dll = ctypes.CDLL(None)
    similarity_cfunc_address = ctypes.addressof(similarity_cfunc)
    dll._handle = similarity_cfunc_address
    print(f"Function address: {similarity_cfunc_address}")

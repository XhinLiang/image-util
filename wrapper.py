from ctypes import *

# 定义需要导出的函数
def add(a, b):
    return a + b

# 创建并设置函数的返回类型和参数类型
add_function = CFUNCTYPE(c_int, c_int, c_int)(add)

# 创建 DLL
if __name__ == "__main__":
    import ctypes
    dll = CDLL(None)
    add_function.restype = c_int
    add_function.argtypes = [c_int, c_int]
    dll.add = add_function

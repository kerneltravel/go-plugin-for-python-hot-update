import os,sys
import ctypes as C

def fileExtension():
    ext = ""
    plat = sys.platform
    if plat.startwith('linux'):
        ext = "so"
    elif plat.startswith("cygwin") or plat.startswith("win") :
        ext = "dll"
    elif plat.startswith("darwin") :
        ext = "dylib"

dll_ext = fileExtension()
pathnow=os.path.abspath("greet.{}".format(dll_ext))
#dll = C.cdll.LoadLibrary('greet.dll')
pathnow=pathnow.replace('\\','/')


print(pathnow)

#实际调用动态库的接口：
dll= C.cdll.LoadLibrary(pathnow)
#print(dll)

#调用 无参数的 接口
dll.F()

#调用无返回值、但有参数 的接口
dll.Add(1,2)

#调用有返回值的 接口
print(dll.AddResult(2,3))

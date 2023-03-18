适用场景：

1. 核心代码希望通过dll封装，外层调用只通过python简单方式来调用 go封装好的 dll提供的功能。本示例代码演示了python脚本调用go封装的dll/so 的函数的效果，二进制发布全部内容。
2. 由于主要基于dll 调用，相当于插件系统，天然支持软件的热更新。可由python脚本检测服务端是否有更新，有则通过热更获得 dll来替换旧dll的方式，实现软件升级的效果。
3. nuitka 由于编译比较费时，不适合python 脚本import 很多其他复杂python库（如PyQT5）的情况，因为容易出现依赖问题。建议只把主要实现都由go的dll实现，python代码只负责业务逻辑代码调用。
4. 支持win和linux 平台。


注意：
1. windows 下go编译的dll如果是32位，则python也要32位。保持数位一致，否则会报错： 无法识别的dll 格式。
    windows 下的main.py 得到可执行文件的 编译过程：
    Python38/python.exe -m nuitka   --output-filename=main.exe --onefile --verbose main.py

2. linux下的编译过程：
    2.1 工具安装：
    #安装 nuitka 工具
    pip3 install  -i  https://mirrors.aliyun.com/pypi/simple/ nuitka

    #安装 patchelf 工具以支持nuitka 的 onefile模式编译
    apt install patchelf    
        否则报错：FATAL: Error, standalone mode on Linux requires 'patchelf' to be installed. Use 'apt/dnf/yum install patchelf' first.
    2.2  编译：
    2.3 运行： ./main
        输出信息：
                /root/goplugin-python/greet.so
                Hello, number 
                1 +2 = 3 
                5

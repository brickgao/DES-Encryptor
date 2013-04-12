DES-Encryptor
=============

一个基于PyQt4的简单的DES加密程序，支持加密，解密和检查。

TODO
----

待增加功能

*   支持自选密钥
*   支持拖拽式输入文件
    
待修复BUG

*   支持Unicode
*   对是否是加密后文件的判断
*   修改为多线程，单线程在加密过程中无法移动窗口
*   密钥内置会存在泄密风险
    
依赖的库
--------

*   PyQt4

环境
----

程序在win7 SP1 64位, Mingw32 4.6.2，Python 2.7, PyQt 4.10下编译通过

编译
----

对于c++模块的编译，请使用如下指令:

    python setup.py build --compiler=mingw32
    
如果出现`未识别的参数-mno-cygwin`，那么请打`cygwinccompiler.patch`（这个问题出现于高版本的mingw32上）。其中`cygwinccompiler.py`位于`PYTHON_HOME/Lib/distutils/`中。

编译好的文件`DES_IN_CPP`会出现在'build/lib.win32-2.7'中，请将模块复制到`src/app/'下即可使用，或者可以将模块拖入你的项目的目录中使用，`DES_IN_CPP`模块的单独用法请参见下文

DES_IN_CPP的用法
----------

    import DES_IN_CPP
    
    DES.Encrypt(text)
    DES.Unencrypt(text)
    DES.Check(text1, text2)
    
其中text是加密或者解密的数据，text1, text2是比较用的数据，请注意text, text1, text2大小必须是8bytes的倍数

性能
----

以下为加密53.2MB文件`AgthStart_v2.8L_t12.7z`的结果，加密函数为DES_IN_CPP中的函数，其余调用为Python

        174 function calls in 15.460 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        54   15.392    0.285   15.392    0.285 :0(Encrypt)
        2    0.000    0.000    0.000    0.000 :0(open)
        1    0.000    0.000    0.000    0.000 :0(pack)
        1    0.000    0.000    0.000    0.000 :0(range)
       54    0.034    0.001    0.034    0.001 :0(read)
        1    0.000    0.000    0.000    0.000 :0(seek)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(stat)
       55    0.021    0.000    0.021    0.000 :0(write)
        1    0.000    0.000    0.000    0.000 genericpath.py:47(getsize)
        1    0.000    0.000   15.460   15.460 profile:0(<code object <module> at 029F9B18, file "test_encrypt.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
        1    0.003    0.003   15.459   15.459 test_encrypt.py:1(<module>)
        1    0.009    0.009   15.456   15.456 test_encrypt.py:6(input_encode)


以下为解密53.2MB文件`AgthStart_v2.8L_t12.7z_DES`的结果，解密函数为DES_IN_CPP中的函数，其余调用为Python

        174 function calls in 15.460 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       54   15.392    0.285   15.392    0.285 :0(Encrypt)
        2    0.000    0.000    0.000    0.000 :0(open)
        1    0.000    0.000    0.000    0.000 :0(pack)
        1    0.000    0.000    0.000    0.000 :0(range)
       54    0.034    0.001    0.034    0.001 :0(read)
        1    0.000    0.000    0.000    0.000 :0(seek)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(stat)
       55    0.021    0.000    0.021    0.000 :0(write)
        1    0.000    0.000    0.000    0.000 genericpath.py:47(getsize)
        1    0.000    0.000   15.460   15.460 profile:0(<code object <module> at 029F9B18, file "test_encrypt.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
        1    0.003    0.003   15.459   15.459 test_encrypt.py:1(<module>)
        1    0.009    0.009   15.456   15.456 test_encrypt.py:6(input_encode)

运行界面
--------

![运行界面](/sample/img.jpg)
    
Log
---
*   2013/4/2

采用c++编写外挂库，将加密解密速度从4k/s提升至3.5MB/s左右

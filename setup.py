from distutils.core import setup, Extension


setup(name='DES_IN_CPP',
      version='0.1',
      description='c-implemented DES for python',
      ext_modules=[Extension('DES_IN_CPP',
                             sources=['src/setup_pyd/DES_IN_CPP.cpp'],
                             include_dirs=['include'])])


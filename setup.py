from distutils.core import setup, Extension

from Cython.Build import cythonize


extensions = [
    Extension('*', ['ringing-lib/*.pyx'],
        language='c++',
        libraries=['ringing', 'ringingcore'],
    ),
]


setup(
    name='ringing-lib',
    version='0.1.0',
    author='Leigh Simpson',
    author_email='code@simpleigh.com',
    url='http://github.com/simpleigh/ringing-lib-python',
    description='Python wrapper for the Ringing Class Library',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    license='GPL',
    ext_modules=cythonize(extensions),
)
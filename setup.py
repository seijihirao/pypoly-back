"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

try:
   import pypandoc
   description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   description = ''

setup(
    name='pypolyback',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.12.4',

    description='A simple back-end rest framework in python using twisted and cyclone',
    long_description=description,

    # The project's main homepage.
    url='https://github.com/seijihirao/pypolyback',

    # Author details
    author='Rodrigo Seiji Piubeli Hirao',
    author_email='rodrigo.seiji.hirao@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='backend rest web service',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['endpoints', 'config', 'utils']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['Twisted', 'cyclone'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'pypolyback=pypolyback.commandline:main'
        ],
    },
)

#
# Build project
# # python2 setup.py sdist
#
# Create wheel
# # python2 setup.py bdist_wheel
#
# Upload to Pypi
# # twine upload dist/pypolyback-x.y.z-py2-none-any.whl
# # # x.y.z - is the actual version
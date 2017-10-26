from distutils.core import setup

setup(
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='A script to render Jinja2 templates',
    license='MIT License',
    long_description=open('README.rst').read(),
    name='jmaker',
    packages=['jmaker'],
    url='https://github.com/GreggyStills/jmaker',
    version='0.1.0',
)

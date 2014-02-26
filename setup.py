from setuptools import setup

README = open('README.rst', 'r').read()

setup(
    name='Flask-MiniDrop',
    version='0.1',
    description='Trivial wrapper over DropboxAPi for Flask',
    long_description=README,
    author='Nataliia Uvarova',
    author_email='grafinya.uvarova@gmail.com',
    url='https://github.com/AAzza/Flask-MiniDrop',
    install_requires=[
        'Flask>=0.8',
        'dropbox',
    ],
    py_modules=[
        'flask_minidrop',
    ],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
    ],
    keywords='flask dropbox',
    license='BSD License',
)

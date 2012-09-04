from setuptools import setup, find_packages
import os

version = '1.0'

tests_require = [
    ]

setup(name='zeam.component',
      version=version,
      description="Component infrastructure, based on zope.interface",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='component interface',
      author='Sylvain Viollon',
      author_email='thefunny@gmail.com',
      url='http://pypi.python.org/pypi/zeam.component',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['zeam'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',
          'martian',
          ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )

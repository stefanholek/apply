from setuptools import setup, find_packages

version = '1.1'

setup(name='apply',
      version=version,
      description='An apply function for Python 2 and 3',
      long_description=open('README.txt').read() + '\n' +
                       open('CHANGES.txt').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='apply read write property properties',
      author='Stefan H. Holek',
      author_email='stefan@epy.co.at',
      url='http://pypi.python.org/pypi/apply',
      license='BSD',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      use_2to3=True,
      test_suite='apply.tests',
      install_requires=[
          'setuptools',
      ],
)

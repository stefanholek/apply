from setuptools import setup, find_packages

version = '1.6'

setup(name='apply',
      version=version,
      description='An apply function for Python 2 and 3',
      long_description=open('README.rst').read() + '\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='apply read write property properties',
      author='Stefan H. Holek',
      author_email='stefan@epy.co.at',
      url='https://github.com/stefanholek/apply',
      license='BSD-2-Clause',
      packages=find_packages(),
      zip_safe=True,
)

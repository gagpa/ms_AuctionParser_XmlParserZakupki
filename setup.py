from setuptools import setup, find_packages

requirements = [line.strip() for line in open('requirements.txt').readlines()]
packages = find_packages('packages') + find_packages(include=['ms_app']) + \
           ['ms_app/' + dir_pack for dir_pack in find_packages('ms_app')]

setup(name='parsers_packages',
      version='1.0',
      author='oFry-Tester',
      entry_points={'console_scripts': ['ms_parser = activate:main']},
      packages=packages,
      package_dir={'parsers': 'packages/parsers'},
      data_files=['activate.py'],
      install_requires=requirements,
      )

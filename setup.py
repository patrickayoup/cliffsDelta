import os
from setuptools import setup

def read(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path) as f:
        return f.read()


setup(
    name='cliffsDelta',
    version='0.1.0',
    author='Neil Ernst',
    author_email='neil@neilernst.net',
    url='https://github.com/neilernst/cliffsDelta',
    description='Implementation of Cliff\'s Delta Effect Size Metric',
    license='GNU GPLv2',
    keywords='cliff\s delta',
    py_modules=['cliffsDelta'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
    ]
)

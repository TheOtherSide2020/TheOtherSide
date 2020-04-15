from setuptools import setup
import py2exe
setup(
    console=['main.py'],
    name='TheOtherSide',
    version='0.0',
    packages=[''],
    url='',
    license='',
    author='rhendre',
    author_email='rhendre@andrew.cmu.edu',
    description='Backend System Editor for The Other Side Touchable Projection Display', install_requires=['PyQt5',
                                                                                                           'pyqtgraph',
                                                                                                           'matplotlib',
                                                                                                           ]
)





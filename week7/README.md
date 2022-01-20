# *Week 7*


## General Description

Biological Computing in Python II - In continuation to week 2, week 7 covers more advanced topics within Python, such as numerical computing and building workflows. 

Introduction to Jupyter Notebooks - The Jupyter Notebook is an interactive platform that allows users to use mulitple programming languages (including R and Python), which can be viewed and manipulated though a web browser. 

***

## Languages
Python and R 

***
## Dependencies
IDEs such as RStudio and Visual Studio Code 

***
## Installation

Package Installations for use in Python 3.9: 

[Numpy](https://numpy.org/) package allows for data creation, manipulation and undergoing basic arithemtic calculations within Python. 
Can use `pip` to install packages on bash terminal.  

```bash
pip3 install numpy
```
Note: `pip3` download packages directly into Python version 3.9


[SciPy](https://scipy.org/) package is simillar to Numpy however it is recommended for more complex numerical operations (e.g integration). Other sub packages in SciPy used is `scipy.integrate`. 

```bash
pip3 install scipy 
```
```python
import scipy.integrate as integrate
```

[matplotlib](https://matplotlib.org/) library is used to create visualizations in Python. 
```bash
pip3 install matplotlib
```
Importing `matplotlib` to be used within the module `Pylab` (already embedded inside `matplotlib`) in Python:
```python
import matplotlib.pylab as p
```   

To install Jupyter Notebooks read through [this](https://jupyter.readthedocs.io/en/latest/install.html) and [this](https://imperial-fons-computing.github.io/jupyter.html). Jupyter Notebook can be launched via bash terminal in Linux/Unix. 

Instructions to install iPython kernel and R kernel can be found [here](https://imperial-fons-computing.github.io/jupyter.html). Additional language kernels are listed [here](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels). 


## Project Structure and Usage

../code

   - LV1.py : Python script to calculate The Lotka-Volterra model using numerical integration and plot out result figures into *results* directory
   - profileme.py : Script to use for profiling code
   - profileme2.py : Alternative script to a less costly method of profileme.py during profiling
   - timeitme.py : Using `timeit` module to find the best efficent method to run a command within a larger program
   - TestR.py : Creating a workflow by running R script(TestR.R) within ipython  
   - TestR.R : R script used for building workflows 
   - oaks_debugme.py : Practical using doctest to debug code 
   - MyFirstJupyterNb.ipynb : First notebook in Jupyter using both ipython and R languages

../data

   - TestOaksData.csv : Species file that contains oak species
   - JustOaksData.csv : Species file that contains only oak species
   

../results

../sandbox


Author: Cherie Yu

Contact: cyy21@ic.ac.uk

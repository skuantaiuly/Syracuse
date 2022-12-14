# Syracuse
## The Syracuse Sequence

The Syracuse (Collatz or Hailstone) conjecture concerns a sequence of integers defined as follows:

Starts with any positive integer N 

&nbsp;&nbsp;And each term is formed from the previous one as follows:
        
&nbsp;&nbsp;&nbsp;&nbsp;if the previous term is odd:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the next term is 3 times the previous term and plus 1 

$$
                3*N + 1
$$

&nbsp;&nbsp;&nbsp;&nbsp;if the previous term is even:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the next term is half the previous term

$$ 
                N / 2
$$
    
The sequence will always reach 1. 🏁

## Solution

+ Solution in IPython Notebook 8.5.0:
[Syracuse.ipynb](https://github.com/skuantaiuly/Syracuse/blob/main/Syracuse.ipynb)

+ Solution in Python 3.10.6:
[Syracuse.py](https://github.com/skuantaiuly/Syracuse/blob/main/Syracuse.py)

#### Additional libraries used for visualization:

Seaborn

```
pip install seaborn
```

Matplotlib

```
pip install matplotlib
```

Plotext

```
pip install plotext
```

## Clone this repository :

```
$ git clone https://github.com/skuantaiuly/Syracuse.git
```

## Author

Kuantaiuly Salamat

11/2022, developed on IPython and Jupyter Notebook, Visual Studio Code



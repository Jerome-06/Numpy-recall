 NumPy Recall— Numerical Computing with Python
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=flat&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat)
![Role](https://img.shields.io/badge/Goal-Data%20Scientist%20%7C%20Analyst-green?style=flat)
> *"NumPy is the foundation of every data science library — master it, and everything else clicks."*
---
About Me
Hi, I'm Jerome R — an aspiring Data Scientist / Analyst on a hands-on Python learning journey.
This repository documents my practical exploration of NumPy, the core numerical computing library behind pandas, scikit-learn, and TensorFlow. Every script was written and tested by me in VS Code.
---
Why NumPy?
Before diving into machine learning or advanced data analysis, you need to understand how numbers are stored and operated on efficiently. NumPy's arrays are faster than Python lists, support vectorized operations, and are the backbone of the entire data science ecosystem.
---
What I Learned & Built
#	Topic	What I Practiced	File
1	Arrays	Creating arrays, element-wise operations, data types	`main.py`
2	Arithmetic	Scalar ops, vectorized math, element-wise ops, comparison operators	`arithmetic.py`
3	Slicing	Row/column/subarray selection using start:stop:step	`slicing.py`
4	Multidimensional Arrays	3D arrays, ndim, shape, size, indexing	`multidimensional.py`
5	Broadcasting	Operations on arrays with different shapes	`broadcasting.py`
6	Filtering	Boolean masks, AND/OR conditions, np.where()	`filtering.py`
7	Aggregation	sum, mean, median, std, var, argmin, argmax with axes	`aggregation.py`
8	Random Numbers	default_rng, integers, normal, shuffle, choice	`random_numbers.py`
---
Key Concepts I Understand
ndarray — NumPy's core data structure; faster and more memory-efficient than Python lists
Vectorized operations — apply math to entire arrays without loops
Broadcasting — NumPy virtually expands smaller arrays to match larger ones for operations
axis=0 / axis=1 — axis 0 operates column-wise (down), axis 1 operates row-wise (across)
Boolean masking — filter arrays using True/False conditions
np.where(condition, x, y) — returns x where condition is True, else y
seed reproducibility — `np.random.default_rng(seed=n)` ensures same random output every run
3D array indexing — `array[depth, row, col]` to access elements in multidimensional arrays
---
🔍 Code Highlights
Broadcasting — adding arrays of different shapes:
```python
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])   # shape (1, 10)
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])  # shape (10, 1)
print(array1 + array2)  # results in a (10, 10) matrix
```
Aggregation with axes:
```python
array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.sum(array, axis=0))  # sum each column → [7, 9, 11, 13, 15]
print(np.sum(array, axis=1))  # sum each row   → [15, 40]
```
Filtering with np.where:
```python
ages = np.array([[21,25,45,12,55,63,15],[18,22,30,28,40,19,17]])
adults = np.where(ages >= 18, ages, "-")  # replace minors with "-"
```
3D Array indexing:
```python
array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z','!']]])
word = array[0,0,0] + array[1,1,1] + array[2,2,2]  # → "ANZ"
```
Slicing a 2D array:
```python
array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(array[0:4:2])     # every other row
print(array[:,::-1])    # reverse all columns
print(array[2:4, 0:2])  # subarray selection
```
Arithmetic & vectorized math:
```python
array = np.array([1,2,3])
print(np.sqrt(array))  # [1.0, 1.414, 1.732]
print(np.exp(array))   # [2.718, 7.389, 20.085]
print(np.log(array))   # [0.0, 0.693, 1.098]

scores = np.array([85,90,78,92,88])
print(scores > 80)     # [True, True, False, True, True]
```
---
📁 Project Structure
```
numpy-mastery/
│
├── main.py                # Array basics & element-wise operations
├── arithmetic.py          # Scalar, vectorized & element-wise arithmetic
├── slicing.py             # Array slicing techniques
├── multidimensional.py    # 3D arrays, shape, ndim, size
├── broadcasting.py        # Broadcasting rules & examples
├── filtering.py           # Boolean filtering & np.where()
├── aggregation.py         # Aggregate functions with axes
└── random_numbers.py      # Random generation, shuffle & choice
```
---
🛠️ Tech Stack
Language: Python 3.x
Library: NumPy
Editor: Visual Studio Code
Version Control: Git & GitHub
---
🚀 Getting Started
```bash
# 1. Clone the repository
git clone https://github.com/JeromeR/numpy-mastery.git

# 2. Navigate into the folder
cd numpy-mastery

# 3. Install NumPy
pip install numpy

# 4. Run any script
python arithmetic.py
```
---
📈 My Data Science Roadmap
[x] Python basics
[x] Pandas fundamentals
[x] NumPy — numerical computing
[ ] Matplotlib & Seaborn — data visualization
[ ] Exploratory Data Analysis (EDA) on a real dataset
[ ] Machine Learning with Scikit-learn
[ ] End-to-end data science project
---
🤝 Let's Connect
I'm actively looking for Data Scientist / Analyst opportunities.
📧 Email: jeromer2004@gmail.com
💼 LinkedIn: linkedin.com/in/jerome-r
🐙 GitHub: github.com/JeromeR
---
📄 License
This project is open source under the MIT License.
---
<p align="center">
  <i>⭐ If this helped you learn NumPy too, consider giving it a star!</i>
</p>

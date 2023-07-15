# Sudoku-Solvers
Exploring the different algorithms to solve Sudoku

## Instructions

### Installing gym-sudoku From [Forked Repo](https://github.com/jamesdvance/gym-sudoku)
1. git clone https://github.com/jamesdvance/gym-sudoku.git
2. pip install ./gym-sudoku

## Background
[Soduku](https://en.wikipedia.org/wiki/Sudoku) is played on a grid of 9 x 9 spaces. Within the rows and columns are 9 “squares” (made up of 3 x 3 spaces). <br/>
Each row, column and square (9 spaces each) needs to be filled out with the numbers 1-9, <br/>
without repeating any numbers within the row, column or square.

<p>
To my knowledge, no one has yet succeeded in solving Sudoku as a pure reinforcement learning problem. Sakin et all [4] managed to train an accurate supervised classifer that could predict the winning outcome of a game. However, the solution does not come up with new solutions and cannot perform multiple solutions on the same problem. 
</p>

<p>
Of course its trivial to solve Sodoku as a Linear Program. It's such a common formulation that it is the example problem in the PulP library documentation. It is also straightforward to solve as a programming problem, including a simple depth-first search approach.     
</p>

## Solutions
[Depth First Search (Memory Optimized)](algorithms/dfs_backtracking_low_memory.py)
<br/>
[Linear Programming](algorithms/linear_program.py)


## Resources

### Depth First Search
1. [Sudoku Leetcode problem](https://leetcode.com/problems/sudoku-solver/)

### Linear Programming
2. [Sudoku As A Linear Program](https://www.coin-or.org/PuLP/CaseStudies/a_sudoku_problem.html)
3. [Sudoku As Graph Coloring Problem](https://www.linkedin.com/pulse/solve-your-sudoku-graph-coloring-problem-alireza-soroudi/?trk=eml-email_series_follow_newsletter_01-hero-1-title_link&midToken=AQET4HYp_zAXXw&fromEmail=fromEmail&ut=2RbmToAhecnGI1)

### Reinforcement Learning
4. [Sudoku-Gym Original](https://github.com/wcheung-code/sudoku-gym)
5. [Reinforcement Learning For Constraint Satisfaction Game Agents](https://arxiv.org/ftp/arxiv/papers/2102/2102.06019.pdf)
6. [Sudoku with Deep Q Learning](https://github.com/adityapujari98/Solving-Sudoku-using-Deep-Q-learning/blob/master/boardenv.py)
    * Seems implausible

### Supervised Learning
7. [Can Convolutional Neural Networks Crack Sudoku Puzzles?](https://github.com/Kyubyong/sudoku)
    * [Fork Of Above With Pytorch](https://github.com/charlesakin/sudoku)
    * [Paper: Solving Sudoku With Neural Networks](https://cs230.stanford.edu/files_winter_2018/projects/6939771.pdf)
8. [Supervised Learning with CNNs (99% accuracy)](https://github.com/shivaverma/Sudoku-Solver/blob/master/sudoku.ipynb)
9. [OptNet: Differentiable Optimization As A Layer In Neural Networks](http://proceedings.mlr.press/v70/amos17a/amos17a.pdf)
10. [One Million Sudoku Games Dataset](https://www.kaggle.com/datasets/bryanpark/sudoku)


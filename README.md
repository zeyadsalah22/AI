# CS50 AI Projects

This repository contains implementations of various AI projects from the CS50 AI course. Each project tackles different concepts and challenges in the field of Artificial Intelligence.

## Project 1: Degrees
- **File:** `degrees.py`
- **Description:** This program determines how many “degrees of separation” apart two actors are. It uses breadth-first search to find the shortest path between two actors by choosing a sequence of movies that connects them.
- **External Resources:**
  - [Project Description](https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip)
  - [Background](https://cs50.harvard.edu/ai/2023/projects/0/degrees/)

## Project 2: Tic-Tac-Toe
- **File:** `tictactoe.py`
- **Description:** This project implements an AI player for Tic-Tac-Toe using the Minimax algorithm. The AI plays optimally to ensure it never loses the game, and it aims to win if possible or force a tie against an optimal opponent.
- **External Resources:**
  - [Project Description](https://cdn.cs50.net/ai/2023/x/projects/0/tictactoe.zip)
  - [Background](https://cs50.harvard.edu/ai/2023/projects/0/tictactoe/)

## Project 3: Knights and Knaves Puzzle Solver

- **File:** `puzzle.py`
- **Description:** The `puzzle.py` file contains a program that solves logic puzzles known as "Knights and Knaves" puzzles. In these puzzles, characters are either knights (who always tell the truth) or knaves (who always lie), and the objective is to determine the identities of characters based on the statements they make.
- **External Resources:**
  - [Project Description](https://cdn.cs50.net/ai/2023/x/projects/1/knights.zip)
  - [Background](https://cdn.cs50.net/ai/2023/x/projects/1/knights.zip)

## Project 4: Minesweeper

- **File:** `minesweeper.py`
- **Description:** This file contains the implementation of an AI to play the game Minesweeper. The AI uses propositional logic and inference to make educated guesses about where the mines are located.
- **External Resources:**
  - [Project Description](https://cs50.harvard.edu/ai/2024/projects/1/minesweeper/)
  - [Background](https://cs50.harvard.edu/ai/2024/projects/1/minesweeper/#background)

## Project 5: PageRank

- **Files:** `pagerank.py`
- **Description:** This file contains the implementation of an AI to rank web pages by importance using the PageRank algorithm. The program estimates the PageRank of each page by both sampling from a Markov Chain random surfer and iteratively applying the PageRank formula.
- **External Resources:**
  - [Project Description](https://cs50.harvard.edu/ai/2025/projects/2/pagerank/)
  - [Background](https://cs50.harvard.edu/ai/2025/projects/2/pagerank/#background)

## Project 6: Heredity

- **Files:** `heredity.py`
- **Description:** This file contains an AI implementation to assess the likelihood that a person will have a particular genetic trait based on a Bayesian Network model. The program calculates joint probabilities, updates probability distributions, and normalizes them to make inferences about a population's genetic traits.
- **External Resources:**
  - [Project Description](https://cs50.harvard.edu/ai/2023/projects/2/heredity/)
  - [Background](https://cs50.harvard.edu/ai/2023/projects/2/heredity/#background)

## Project 7: Crosswords

- **Files:** `generate.py`
- **Description:** This file contains an AI implementation to generate crossword puzzles. Given the structure of a crossword puzzle and a list of words, the program fills in the puzzle by choosing which words should go in each vertical or horizontal sequence of squares. It models the problem as a constraint satisfaction problem and implements algorithms to enforce node consistency, arc consistency, and backtracking search to find a satisfying assignment of words.
- **External Resources:**
  - [Project Description](https://cdn.cs50.net/ai/2023/x/projects/3/crossword.pdf)
  - [Background](https://cdn.cs50.net/ai/2023/x/projects/3/crossword.html)

## Project 8: Shopping

- **Files:** `shopping.py`
- **Description:** This file contains an implementation to predict whether online shopping customers will complete a purchase using a nearest-neighbor classifier. The program loads data from a CSV file, trains a machine learning model, makes predictions, and evaluates the model's sensitivity and specificity.
- **External Resources:**
  - [Project Description](https://cdn.cs50.net/ai/2023/x/projects/4/shopping.pdf)
  - [CSV Documentation](https://docs.python.org/3/library/csv.html)

## Project 9: Nim

- **Files:** `nim.py`, `play.py`
- **Description:** This project implements an AI that learns to play Nim through reinforcement learning. The AI uses Q-learning to learn the optimal strategy for playing Nim by playing simulated games against itself.
- **External Resources:**
  - [Project Description](https://cdn.cs50.net/ai/2023/x/projects/4/nim.pdf)

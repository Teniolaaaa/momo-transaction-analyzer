# Minimum Operations

## Description
This project solves the problem of calculating the minimum number of operations needed to achieve exactly n 'H' characters in a text file, starting with a single 'H' character, using only two operations: Copy All and Paste.

## Problem
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

## Algorithm
The solution uses prime factorization. The minimum number of operations equals the sum of all prime factors of n.

### Example
- n = 9 = 3 × 3 → operations = 3 + 3 = 6
- n = 12 = 2 × 2 × 3 → operations = 2 + 2 + 3 = 7
- n = 4 = 2 × 2 → operations = 2 + 2 = 4

## Files
- `0-minoperations.py`: Contains the minOperations function
- `0-main.py`: Test file for the function

## Requirements
- Python 3.4.3
- Ubuntu 14.04 LTS
- PEP 8 style (version 1.7.x)
- All files must be executable

## Usage
```bash
./0-main.py
```

## Author
Project for ALU Interview Preparation

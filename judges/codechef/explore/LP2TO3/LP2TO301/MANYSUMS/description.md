---
Contest Name: LP2TO301 - Basic programming concepts
Problem Code: MANYSUMS
Problem Title: Distinct Pair Sums
Problem Difficulty: 
Problem Url: https://www.codechef.com/LP2TO301/problems/MANYSUMS
Problem Tags: ; 
Editorial Url: 
Video Editorial Url: https://video.gumlet.io/62c2db7b1a5e497c7a49783d/62d140e3daaef83eaf696d65/main.mpd
Discussion Url: https://discuss.codechef.com/search?q=MANYSUMS
IsTemplate: No
---


# Problem Statement

Read problems statements in [Hindi](https://www.codechef.com/download/translated/COOK126/hindi/MANYSUMS.pdf), [Mandarin Chinese](https://www.codechef.com/download/translated/COOK126/mandarin/MANYSUMS.pdf), [Russian](https://www.codechef.com/download/translated/COOK126/russian/MANYSUMS.pdf), [Vietnamese](https://www.codechef.com/download/translated/COOK126/vietnamese/MANYSUMS.pdf), and [Bengali](https://www.codechef.com/download/translated/COOK126/bengali/MANYSUMS.pdf) as well.

You are given a range of integers $\{L, L+1, \ldots, R\}$. An integer $X$ is 
said to be *reachable* if it can be represented as a sum of two 
**not necessarily distinct** integers in this range. Find the number of 
distinct reachable integers.

# Constraints

- $1 \leq T \leq 10^5$
- $1 \leq L \leq R \leq 10^6$


# Format

## Input

- The first line of the input contains a single integer $T$ denoting the number 
  of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated 
  integers $L$ and $R$.

## Output

For each test case, print a single line containing one integer — the number of 
reachable integers.

# Sample Testcases

## Sample Test 1

**Input:**
2

2 2

2 3

**Output:**
1

3

**Explanation:**
**Example case 1:** The only reachable integer is $2 + 2 = 4$.

**Example case 2:** $4$, $5$ and $6$ are reachable, since $2+2=4$, $2+3=5$ and $3+3=6$.


# Useful References/Discussions

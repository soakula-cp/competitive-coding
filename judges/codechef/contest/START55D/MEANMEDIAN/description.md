---
Contest Name: START55D - Starters 55 Division 4 (Rated)
Problem Code: MEANMEDIAN
Problem Title: Mean and Median
Problem Difficulty: 
Problem Url: https://www.codechef.com/START55D/problems/MEANMEDIAN
Problem Tags: ; 
Editorial Url: 
Video Editorial Url: 
Discussion Url: https://discuss.codechef.com/search?q=MEANMEDIAN
IsTemplate: No
---


# Problem Statement

Chef has two numbers $X$ and $Y$. Chef wants to find three integers 
$A, B,$ and $C$ such that:
- $-1000 \le A, B, C \le 1000$
- $mean([A, B, C]) = X$
- $median([A, B, C]) = Y$

Can you help Chef find such three integers?

As a reminder, $mean([P, Q, R]) = \frac{P + Q + R}{3}$ and $median([P, Q, R])$ 
is the element at the $2^{nd}$ (middle) position after we sort $[P, Q, R]$ in 
non-decreasing order.

# Constraints

- $1 \leq T \leq 10^5$
- $-100 \le X, Y \le 100$

# Format

## Input

- The first line contains a single integer $T$ — the number of test cases. 
  Then the test cases follow.
- The first and only line of each test case contains two space-separated 
  integers $X$ and $Y$ — the required mean and median of the three integers.


## Output

For each test case, output three integers $A, B, C$ which satisfy the given 
conditions.

It is guaranteed that an answer always exists under the given constraints.
 
If multiple answers exist, output any.


# Sample Testcases

## Sample Test 1

**Input:**
3
5 5
67 100
4 5


**Output:**
5 5 5
0 100 101
0 5 7

**Explanation:**
**Test Case 1:** $mean([5, 5, 5]) = \frac{5 + 5 + 5}{3} = 5$, $median([5, 5, 5]) = 5$.

**Test Case 2:** $mean([0, 100, 101]) = \frac{0 + 100 + 101}{3} = \frac{201}{3} = 67$, 
$median([0, 100, 101]) = 100$.

**Test Case 3:** $mean([0, 5, 7]) = \frac{0 + 5 + 7}{3} = 4$, $median([0, 5, 7]) = 5$.


# Useful References/Discussions

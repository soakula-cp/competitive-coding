---
Contest Name: START55D - Starters 55 Division 4 (Rated)
Problem Code: BROKENPHONE
Problem Title: Broken Phone
Problem Difficulty: 
Problem Url: https://www.codechef.com/START55D/problems/BROKENPHONE
Problem Tags: ; 
Editorial Url: 
Video Editorial Url: 
Discussion Url: https://discuss.codechef.com/search?q=BROKENPHONE
IsTemplate: No
---


# Problem Statement

Uttu broke his phone. He can get it repaired by spending $X$ rupees or he can 
buy a new phone by spending $Y$ rupees. Uttu wants to spend as little money as 
possible. Find out if it is better to get the phone repaired or to buy a new phone.

# Constraints

- $1 \leq T \leq 1000$
- $1 \le X, Y \le 10^4$

# Format

## Input

- The first line contains a single integer $T$ — the number of test cases. 
  Then the test cases follow.
- The first and only line of each test case contains two space-separated 
  integers $X$ and $Y$ — the cost of getting the phone repaired and the cost of 
  buying a new phone.


## Output

For each test case, 
- output `REPAIR` if it is better to get the phone repaired.
- output `NEW PHONE` if it is better to buy a new phone.
- output `ANY` if both the options have the same price.

You may print each character of `REPAIR`, `NEW PHONE` and `ANY` in uppercase 
or lowercase (for example, `any`, `ANy`, `Any` will be considered identical).

# Sample Testcases

## Sample Test 1

**Input:**
3
100 1000
10000 5000
3000 3000


**Output:**
REPAIR
NEW PHONE
ANY


**Explanation:**
**Test Case 1:** It is better to get the phone repaired since $100 \lt 1000$.

**Test Case 2:** It is better to buy a new phone since $10000 \gt 5000$.

**Test Case 3:** Uttu can choose either of the two options since $3000 = 3000$.


# Useful References/Discussions

---
Contest Name: LP2TO301 - Basic programming concepts
Problem Code: ALTER
Problem Title: Alternating Work Days
Problem Difficulty: 
Problem Url: https://www.codechef.com/LP2TO301/problems/ALTER
Problem Tags: ; 
Editorial Url: 
Video Editorial Url: https://video.gumlet.io/62c2db7b1a5e497c7a49783d/62d150b8daaef83eaf697dc2/main.mpd
Discussion Url: https://discuss.codechef.com/search?q=ALTER
IsTemplate: No
---


# Problem Statement

Read problem statements in [Mandarin](https://www.codechef.com/download/translated/LTIME101/mandarin/ALTER.pdf), [Russian](https://www.codechef.com/download/translated/LTIME101/russian/ALTER.pdf), and [Vietnamese](https://www.codechef.com/download/translated/LTIME101/vietnamese/ALTER.pdf) as well.

Alice and Bob are two friends. Initially, the skill levels of them are zero. 
They work on alternative days, i.e one of Alice and Bob works on the 
odd-numbered days $(1, 3, 5, \dots)$ and the other works on the even-numbered 
days $(2, 4, 6, \dots)$. The skill levels of Alice and Bob increase by $A, B$ 
respectively on the days they work.

Determine if it is possible that the skill levels of Alice and Bob become 
exactly $P, Q$ respectively on some day.

# Constraints

- $1 \leq T \leq 10^3$
- $1 \leq A, B, P, Q \leq 10^9$

# Format

## Input

- The first line contains an integer $T$, denoting the number of test cases. 
  The $T$ test cases then follow:
- The first and only line of each test case contains four space-separated 
  integers $A, B, P, Q$.

## Output

For each test case, print `YES` if it is possible that the skill levels of 
Alice and Bob become exactly $P, Q$ on some day, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for 
example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

# Subtasks

- **Subtask 1 (100 points):** Original constraints

# Sample Testcases

## Sample Test 1

**Input:**
4
1 2 1 2
1 2 3 2
4 3 4 6
3 5 9 25

**Output:**
YES
NO 
YES
NO

**Explanation:**
**Test Case $1$:** Alice works on the first day and gains skill level $1$. 
Bob works on the second day and gains skill level $2$.

**Test Case $2$:** There is no possible way that the skill levels of Alice and 
Bob become $3$ and $2$ respectively.

**Test Case $3$:** Bob works on the first and third day and Alice works on the 
second day. Hence after the third day, the skill levels of Alice and Bob become 
$1\cdot4 = 4$ and $2 \cdot 3 = 6$ respectively.

# Useful References/Discussions

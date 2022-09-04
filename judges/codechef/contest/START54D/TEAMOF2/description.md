---
Contest Name: START54D - Starters 54 Division 4 (Rated)
Problem Code: TEAMOF2
Problem Title: Team of Two
Problem Difficulty: 
Problem Url: https://www.codechef.com/START54D/problems/TEAMOF2
Problem Tags: Implementation; Algorithms
Editorial Url: https://discuss.codechef.com/problems/TEAMOF2
Video Editorial Url: https://video.gumlet.io/62c2db7b1a5e497c7a49783d/630f920e4dbb69bbe1135b8a/main.mpd
Discussion Url: https://discuss.codechef.com/search?q=TEAMOF2
IsTemplate: No
---

# Problem Statement

Your class recently got a maths assignment with $5$ questions. There are 
$N (\le 20)$ students in the class and **at most** $2$ people can 
collaborate. For each student, you know which problems they solved.

Find out if there exists a team of two students who can together solve all problems.

# Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 20$
- $0 \leq K_i \leq 5$
- $1 \leq x_i \leq 5$

# Format

## Input

The first line of input will contain a single integer $T$, denoting the number 
of test cases. $T$ test cases follow.
- Each of the following test cases contains $N + 1$ lines, where $N$ is the 
  number of students in the class.
    - The first line contains a single integer $N$.
    - Each of the following $N$ lines contains $K_i + 1$ positive integers 
      by whitespaces.
        - In the $i^{th}$ line, the first positive integer $K_i$ is the number 
          of problems the $i^{th}$ student can solve. The next $K_i$ integers 
          are $x_1, x_2, \ldots, x_{K_i}$, the indices of the problems this 
          student can solve.

## Output

The output must consist of $T$ lines.
- Each line must contain a single string: The solution to the $i^{th}$ test 
  case as a `YES` or `NO` (where `YES` should be returned if some pairing of 
  students is capable of solving all the problems, and `NO` otherwise). 

You may print each character of the string in uppercase or lowercase (for 
example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as 
identical). 

# Sample Testcases

## Sample Test 1

**Input:**
4
3
1 3
1 1
4 1 3 4 5
2
4 2 3 4 5
3 1 2 4
3
1 1
1 2
1 3
2
2 1 5
3 2 3 4


**Output:**
NO
YES
NO
YES

**Explanation:**
**Test case $1:$** There is no student who solved the second question.

**Test case $2:$** The second student can solve the first question and the first 
student can solve all the remaining problems, so they can form a team to solve 
all the problems together.

**Test case $3:$** There is no student who solved fourth and fifth questions.

**Test case $4:$** Given $2$ people can collaborate to solve all the problems.

# Useful References/Discussions

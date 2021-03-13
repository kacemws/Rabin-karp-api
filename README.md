# Introduction

Many of our daily used apps offers an integrated search engine, with each one using a diffrent algorithm, but which one is the most efficient regarding time and ressources usage.

## Algorithms and time/ressources usage

The simplest and the first algorithm that comes to mind maybe the naive search. This algorithm overlays the pattern string p at every position in the text t, and checks whether every
pattern character matches the corresponding text character, if we check the **time consumption** it would take O(n\*m) :

    for i from 0 to m -1 :

        for j from 0 to n -1 :

            +1

In the next few paragraphes, we will introduce another algorithm known as The Rabin-karp algorithm. it is based on **hashing** and the **rolling hash** technique, this technique is a hash function where the input is hashed in a window that moves through it

### The Rabin Karp algorithm

the algorithm matches the hash value of the pattern with the hash value of current substring of text, and if the hash values match then only it starts matching individual characters. So Rabin Karp algorithm needs to calculate hash values for following strings.

1. Pattern itself.

2. All the substrings of the text of length m.

Since the algorithm is based on the rolling hash, its hash function should fulfill :

- Hash at the next shift must be efficiently computable from the current hash value and next character in text

### Time complexity

The **average** and **best**-case running **time** of the Rabin-Karp algorithm is O(n+m), but its **worst-case time** is O(nm). Worst case of Rabin-Karp algorithm occurs when all characters of pattern and text are same as the hash values of all the substrings of t match with hash value of p. For example p = “AAA” and t = “AAAAAAA”.

### Code

This repository represents the code for the algorithm presented in the matching chapter in '**Introduction to algorithms, Third edition**'
<img src='./Rabin-Karp.png'>

### Results

The following screenshot is took from the execution of the '**rabin-karp.py**' file
<img src='./execution.png'>

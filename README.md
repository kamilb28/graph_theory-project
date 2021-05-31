# Algorithm of Edmonds-Karp
[Edmonds–Karp algorithm on Wikipedia](https://en.wikipedia.org/wiki/Edmonds–Karp_algorithm)

*Shortcuts in the project:*
* [Analytical part of project](https://github.com/kamilb28/graph_theory-project/blob/main/Documents%20and%20assignments/Kamil_Bernacik-assignment.pdf)
* [Analysis of algorithm](https://github.com/kamilb28/graph_theory-project/blob/main/Documents%20and%20assignments/analysis%20of%20Edmonds-Karp%20algorithm.pdf)

## Input file

Your input file should be a txt file that contains an [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix).

For example:

Given a network of seven nodes, source A, sink G, and capacities as shown below:
![Graph](https://github.com/kamilb28/graph_theory-project/blob/main/Documents%20and%20assignments/graph.jpeg)

So our matrix will look like this:
```
   A B C D E F G
A: 0 9 0 0 9 0 0
B: 0 0 7 3 0 0 0
C: 0 0 0 4 0 0 6
D: 0 0 0 0 0 2 9
E: 0 0 0 3 0 6 0
F: 0 0 0 0 0 0 8
G: 0 0 0 0 0 0 0
```

*in this algorithm source must be always in first line and sink in the bottom line*

The matrix should be written in the txt file like this:
```
0,9,0,0,9,0,0
0,0,7,3,0,0,0
0,0,0,4,0,0,6
0,0,0,0,0,2,9
0,0,0,3,0,6,0
0,0,0,0,0,0,8
0,0,0,0,0,0,0
```

There are examples files:
* [Example1](example.txt)
* [Example2](example2.txt)


## How to use 

1.  Clone this repository
    ```
    git clone https:
    ```
    or download zip file of the repository

2.  Run
    ```
    python main.py
    ```
    or 
    ```
    python3 main.py
    ```

3.  To run your example write
    ```
    python3 main.py "your_example.txt"
    ```

By default the program will write example and then your file
Firstly there will be shown network and after that will print out the maximum flow

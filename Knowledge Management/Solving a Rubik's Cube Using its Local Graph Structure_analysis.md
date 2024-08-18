# Solving a Rubik's Cube Using its Local Graph Structure

# Title: Solving a Rubik's Cube Using its Local Graph Structure

## Summary:
The paper "Solving a Rubik's Cube Using its Local Graph Structure" by Shunyu Yao and Mitchy Lee explores a novel heuristic approach to solving the Rubik's Cube using a combination of graph theory and neural networks. They model the Rubik's Cube state space as a graph where states are nodes and actions are edges, then propose using a weighted convolutional distance heuristic within the A* search algorithm to find the shortest solution path to the solved state. This method improves the search process by considering local graph structures and leveraging neural networks to estimate move probabilities.

## Key Components Analysis

### Main Research Question
**How can the Rubik's Cube be solved more efficiently using a combination of graph representation and neural network approaches?**

### Methodology
1. **Graph Representation**: The Rubik's Cube is modeled as a graph where states are nodes and actions are edges.
2. **A* Search Algorithm**: Used for pathfinding with a newly proposed heuristic - weighted convolutional distance.
3. **Weighted Convolutional Distance**: A heuristic for A* search that applies graph convolution principles to estimate the shortest path.
4. **Neural Networks**: Used to represent the distance from any state to the solved state and the probability of taking specific actions.

### Key Findings and Results
1. The use of weighted convolutional distance as a heuristic in A* search showed promising results.
2. A 1-layer weighted convolutional distance heuristic resulted in an average solution length of 6.525 moves, time taken of 51.757 seconds, and 1097.345 searched nodes.
3. A 2-layer version further improved the solution length to 6.455 moves, reduced the search nodes to 535.000, but increased the time taken to 326.613 seconds.
4. These results indicate that deeper convolutional layers improve search accuracy but at the cost of increased computational time.

### Conclusions and Implications
The authors conclude that the weighted convolutional distance heuristic improves the precision of the A* search algorithm for solving the Rubik's Cube, leading to shorter solution paths and fewer searched nodes. This method, however, faces computational efficiency issues that could be improved with optimized convolution techniques. They suggest the potential generalization of this approach to other combinatorial puzzles like n-dimensional Rubik's Cubes, Sokoban, and sliding tile puzzles.

## First-Principle Analysis

### Fundamental Concepts

1. **Graph Representation**: The transformation of the Rubik's Cube's state space into a graph is a robust approach because it allows leveraging established graph algorithms and theories.
2. **A* Search Algorithm**: This pathfinding algorithm is well-suited for minimizing the cost functions (moves) efficiently.
3. **Neural Networks**: Utilizing neural networks to represent complex heuristics like distances between states taps into their capacity for approximating complex functions.

### Methodology Evaluation

1. **Graph Representation**: Modeling the state space as a graph effectively captures the possible transitions (actions) and states. It is a sound theoretical approach.
2. **Weighted Convolutional Distance**: This heuristic seems innovative and well-suited for leveraging local graph structure information. The experimental results show it provides more precise directions for the search process.
3. **Implementation**: The neural network approach for distance estimation is logical and fits within the broader scope of machine learning applications in pathfinding problems.

### Validity of Claims

1. **Improved Performance**: The results support the claim that the new heuristic improves pathfinding efficiency by showing reduced solution lengths and fewer searched nodes.
2. **Computational Efficiency**: The increase in computation time for deeper convolutions is a valid concern and was clearly demonstrated in the experiments.
3. **Generalization Potential**: The discussion on applying this approach to other combinatorial puzzles is speculative but reasonable given the generality of graph structures in such puzzles.

## Critical Assessment

### Strengths

1. **Novel Heuristic**: The weighted convolutional distance heuristic is an innovative next step in using graph convolution methods within search algorithms.
2. **Empirical Evaluation**: The paper provides solid empirical evidence for the benefits of the proposed heuristic through well-defined performance metrics.
3. **Theoretical Grounding**: Drawing on established graph theory and neural network principles lends credibility to the methodology.

### Weaknesses

1. **Computational Complexity**: The method's computational inefficiency due to the high time complexity of deeper convolution layers is a significant drawback.
2. **Limited Scope**: The depth of experimental scenarios (5-12 random actions) might not fully reflect the heuristic's performance in more complex or real-world scenarios.
3. **Scalability**: Although discussed, the scalability to larger or more complex puzzles remains unproven experimentally.

## Future Research Directions

1. **Optimizing Computational Efficiency**: Implementing fast convolution techniques in GCNs and converting convolution processes to matrix forms could offer significant improvements.
2. **Expanding Experiment Scope**: Testing on more varied and complex scrambling scenarios could provide a clearer picture of the heuristic’s strengths and limitations.
3. **Generalization and Application**: Applying the heuristic to other combinatorial puzzles and exploring practical applications and limitations in those contexts.

## Conclusion

The paper presents a significant advance in the context of solving Rubik's Cube puzzles by combining graph theory and neural network approaches. By developing a weighted convolutional distance heuristic, the authors show notable improvements in the precision of the A* search algorithm. While the method's computational efficiency needs enhancement, the conceptual robustness and empirical success indicate a valuable direction for future research and application. The potential to generalize this approach to other puzzles could have broader implications in the field of combinatorial optimization and artificial intelligence.

---

### Sources and Research Paper Citation
1. S. McAleer, F. Agostinelli, A. Shmakov, and P. Baldi, "Solving the rubik’s cube without human knowledge," arXiv preprint arXiv:1805.07470, 2018.
2. F. Agostinelli, S. McAleer, A. Shmakov, and P. Baldi, "Solving the rubik’s cube with deep reinforcement learning and search," Nature Machine Intelligence, vol. 1, pp. 356-363, 2019.
3. W. Magnus, A. Karrass, and D. Solitar, "Combinatorial Group Theory: Presentations of Groups in Terms of Generators and Relations," Dover Publications, 2004.
4. T. N. Kipf and M. Welling, "Semi-supervised classification with graph convolutional networks," arXiv preprint arXiv:1609.02907, 2016.
5. K. Stachenfeld et al., "Graph networks with spectral message passing," arXiv preprint arXiv:2101.00079, 2020.
6. C. Vignac, A. Loukas, and P. Frossard, "Building powerful and equivariant graph neural networks with structural message-passing," Advances in Neural Information Processing Systems, vol. 33, pp. 14143-14155, 2020.
7. P. E. Hart et al., "A formal basis for the heuristic determination of minimum cost paths," IEEE Transactions on Systems Science and Cybernetics, vol. 4, no. 2, pp. 100-107, 1968.
8. I. Pohl, "Heuristic search viewed as path finding in a graph," Artificial Intelligence, vol. 1, no. 3, pp. 193-204, 1970.
9. R. Ebendt and R. Drechsler, "Weighted A* search – unifying view and application," Artificial Intelligence, vol. 173, no. 14, pp. 1310-1342, 2009.
10. E. McManus, "Mathematical Understandings Of A Rubik’s Cube," PhD thesis, University of Chicago, 2018.
11. F. Murtagh, "Multilayer perceptrons for classification and regression," Neurocomputing, vol. 2, no. 5, pp. 183-197, 1991.
12. M. C. Popescu et al., "Multilayer perceptron and neural networks," WSEAS Transactions on Circuits and Systems, vol. 8, no. 7, pp. 579-588, 2009.
13. F. Wu et al., "Simplifying graph convolutional networks," Proceedings of the 36th International Conference on Machine Learning, vol. 97, pp. 6861-6871, 2019.
14. M. Chen et al., "Simple and deep graph convolutional networks," Proceedings of the 37th International Conference on Machine Learning, vol. 119, pp. 1725-1735, 2020.
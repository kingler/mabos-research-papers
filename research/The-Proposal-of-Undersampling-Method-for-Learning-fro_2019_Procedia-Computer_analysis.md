# The-Proposal-of-Undersampling-Method-for-Learning-fro_2019_Procedia-Computer

# Title: The Proposal of Undersampling Method for Learning from Imbalanced Datasets

## Summary:
The paper, "The Proposal of Undersampling Method for Learning from Imbalanced Datasets" by Małgorzata Bach, Aleksandra Werner, and Mateusz Palt, presents a new undersampling algorithm named KNN_Order that aims to improve the learning process from highly imbalanced datasets. The method focuses on leveraging the k-Nearest Neighbor (KNN) algorithm to thin clusters of majority class examples by removing observations from high-density areas. The effectiveness of the proposed method is demonstrated through experimental comparisons to various existing undersampling techniques using eighteen public datasets. The results suggest that the KNN_Order method often achieves better performance compared to the other techniques evaluated.

## Key Components Analysis

### Main Research Question
The primary research question addressed in this paper is: How can the performance of machine learning models be improved when learning from highly imbalanced datasets through an effective undersampling method?

### Methodology
The authors propose the KNN_Order algorithm for undersampling:
1. **Input Parameters**:
   - `Smaj`: Set of majority class examples.
   - `k`: Number of nearest neighbors to be considered.
   - `P`: Percentage of undersampling.
   
2. **Process**:
   - For each majority class example, find its `k` nearest neighbors and store their indices and distances in a matrix.
   - Sort the neighbors by distance, remove duplicate indices.
   - Based on the undersampling percentage `P`, determine the number of examples to be removed.
   - Remove the examples closest to the majority class instances.

3. **Performance Evaluation**:
   - Conducted experiments on eighteen datasets with various classifiers (Naive Bayes, Rule Induction, k-Nearest Neighbor, Random Forests, Support Vector Machines, Neural Networks).
   - Used multiple metrics for evaluation (Sensitivity, Specificity, Balanced Accuracy, Geometric Mean, Cohen's Kappa).

### Key Findings and Results
- The KNN_Order method consistently outperformed traditional undersampling techniques like ENN, NCL, and Tomek link on most of the tested datasets.
- KNN_Order achieved the highest average ranking in terms of Sensitivity, Balanced Accuracy, G-Mean, and Kappa metrics.
- The method performed better in preserving important information from the majority class by focusing on high-density removal rather than random elimination or removing isolated points.

### Conclusions and Implications
The authors conclude that the KNN_Order algorithm provides a viable improvement over existing undersampling methods for imbalanced datasets. By focusing on high-density clusters, this method reduces the loss of critical information and achieves more reliable model performance across various classifiers and datasets.

## First-Principle Analysis

### Fundamental Concepts
1. **Class Imbalance:**
   - Class imbalance occurs when the classes in a dataset do not have a roughly equal number of observations. This leads to biased models that perform well on the majority class but poorly on the minority class.
   
2. **Undersampling:**
   - Undersampling addresses class imbalance by reducing the number of majority class instances. Effective undersampling should minimize the loss of important information.

### Methodology Evaluation

1. **Task-Aware Modulation:**
   - KNN_Order uses local instance density to guide the removal of majority class examples, a more informed approach than random undersampling.

2. **Experimental Design:**
   - Thorough comparison across multiple datasets and classifiers strengthens the reliability of the results.
   - Including a variety of performance metrics (Sensitivity, Specificity, Balanced Accuracy, Geometric Mean, Kappa) provides a comprehensive assessment of model performance.

3. **Ablation Studies:**
   - The paper does not explicitly perform ablation studies, which could further validate the efficacy of each component within the method.

### Validity of Claims
1. **Improved Performance:**
   - The results show a robust improvement of KNN_Order over other methods across different scenarios, suggesting legitimate advancements.
   - The statistical significance of improvements is implied through extensive comparison but would be strengthened by explicit statistical testing (e.g., t-tests).

2. **Preservation of Information:**
   - By targeting high-density clusters, the method logically preserves more information compared to random or less-informed undersampling methods, aligning with principles of data retention.

## Critical Assessment

### Strengths
1. **Novel Approach:**
   - The use of local instance density to guide undersampling is innovative and grounded in robust principles.
2. **Comprehensive Evaluation:**
   - Employing a broad array of datasets and metrics provides a holistic view of the method's performance.
3. **Practical Implications:**
   - Effective handling of imbalanced datasets has direct applications in areas like fraud detection, medical diagnosis, and quality assurance.

### Weaknesses
1. **Computational Complexity:**
   - The algorithm's reliance on KNN could be computationally expensive for large datasets.
2. **Lack of Direct Comparisons with Oversampling Methods:**
   - Comprehensive evaluation should also include comparisons with state-of-the-art oversampling methods like SMOTE to contextualize the performance improvements.

### Future Research Directions
1. **Hybrid Methods:**
   - Combining KNN_Order with oversampling techniques could further boost performance.
2. **Parameter Optimization:**
   - Exploring adaptive methods for selecting optimal `k` and `P` values could improve robustness.
3. **Scalability:**
   - Implementations focused on reducing computational overhead would make the method more accessible for large-scale applications.

## Conclusion

The paper "The Proposal of Undersampling Method for Learning from Imbalanced Datasets" presents significant advancements in handling class-imbalanced datasets through the novel KNN_Order method. This approach outperforms traditional undersampling techniques by focusing on high-density areas, thereby preserving essential data characteristics. The research contributes valuable insights that can directly enhance the performance of machine learning models in critical areas such as medical diagnostics and fraud detection.

Overall, the proposed KNN_Order method marks a substantial improvement in class balancing techniques. Future work should focus on integrating this approach with oversampling methods and exploring scalability solutions to broaden its applicability.

## References (from the paper)
1. Fotouhi, S., Asadi, S., and Kattan MW. (2019) "A comprehensive data level analysis for cancer diagnosis on imbalanced data." Journal of Biomedical Informatics 90.
2. Bach, M., and Werner, A. (2018) "Cost-Sensitive Feature Selection for Class Imbalance Problem" Advances in Intelligent Systems and Computing, Proceedings of 38th ISAT Conference: 182-194.
... (and others from the provided text)
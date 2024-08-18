# A-new-Transparent-Ensemble-Method-based-on-Deep-l_2019_Procedia-Computer-Sci

# Title: A new Transparent Ensemble Method based on Deep Learning

## Summary:
The paper titled "A new Transparent Ensemble Method based on Deep Learning" by Naziha Sendi, Nadia Abchiche-Mimouni, and Farida Zehraoui presents a novel deep ensemble method that leverages argumentation to significantly improve classification performance while addressing the common criticism of ensemble methods being inexplicable. By combining machine learning algorithms with a multi-agent system, the method extracts high-quality knowledge from classifiers and provides explanations behind decisions, allowing the integration of prior knowledge.

## Key Components Analysis

### Main Research Question
The primary research question addressed in this paper is: How can the combination of argumentation and deep ensemble methods improve the explicability and performance of machine learning classification systems, especially in critical areas like healthcare, justice, and finance?

### Methodology
The methodology comprises two main phases: argument extraction and multi-agent argumentation.

1. **Argument Extraction Phase:**
   - Individual agents generate their training samples via bootstrap sampling from the training data.
   - A deep multilayer perceptron (DMLP) classifier is employed.
   - Rules are extracted from classifiers using pedagogical and eclectic approaches, resulting in a rule base for each classifier.
   - An expert agent, integrating prior knowledge, is included.

2. **Multi-Agent Argumentation Phase:**
   - Argumentation is modeled using structured argumentation theory where agents argue for their prediction using extracted rules.
   - Agents engage in persuasion dialogues, with roles such as Referee, Master, Challenger, and Spectator defined to facilitate the argumentation process.
   - Seven communication performatives are used to instantiate rules and manage the process through speech acts.

### Key Findings and Results
1. The proposed method effectively provided high-quality knowledge for ensemble classifiers and significantly improved classification performance.
2. The method was validated using real datasets and showed superior performance compared to traditional methods like Bagging and AdaBoost, achieving between 83.2% and 89% accuracy.
3. The approach allowed for reasoning and transparency in decision-making, providing explanations for classifications.
4. The argumentation process demonstrated effectiveness in leveraging internal classification knowledge and integrating prior knowledge.

### Conclusions and Implications
The authors conclude that their approach adds a valuable reasoning aspect to ensemble methods through argumentation, providing a transparent and explainable AI solution. This has significant potential in critical domains requiring reliable and interpretable machine learning models.

## First-Principle Analysis

### Fundamental Concepts
1. **Ensemble Methods:** These improve predictions by combining multiple models. However, they often lack transparency.
2. **Deep Neural Networks (DNNs):** These are powerful but often seen as black boxes, necessitating interpretability.
3. **Argumentation:** This encompasses a method of combining knowledge from multiple sources to provide a more comprehensive and understandable result.

### Methodology Evaluation
1. **Support to Research Question:**
   - The combination of ensemble methods with argumentation directly addresses the challenge of transparency.
   - Argumentation helps in both utilizing classifier outputs and providing human-understandable explanations.
  
2. **Experimental Design:**
   - Diverse datasets and multiple configurations (bootstrap samples and argumentation processes) ensure thorough evaluation.
   - The comparison with multiple baselines strengthens the methodology's validity.

3. **Ablation Studies:**
   - The method was compared against existing approaches (DIMLP, TREPAN, bagging, etc.) to isolate and demonstrate the contribution of the argumentation component.

### Validity of Claims
1. **Improved Performance:**
   - The methodology demonstrates statistically significant improvements over baselines, corroborated by comprehensive cross-validation results.
2. **Reasoning Process:**
   - The detailed case study illustrates the dialogical argumentation process, validating the claimed transparency.
3. **Integration of Prior Knowledge:**
   - The method allows smooth injection of domain knowledge, bolstering the explicability of machine learning models.

## Critical Assessment

### Strengths
1. **Novelty:** Combining argumentation with ensemble methods is a novel approach, addressing a significant real-world problem.
2. **Comprehensive Evaluation:** The method is tested on multiple datasets and scenarios, ensuring robustness.
3. **Explanability:** Significant focus on providing intelligible explanations, crucial for adoption in critical areas.

### Weaknesses
1. **Computational Complexity:** The paper does not extensively discuss the computational overhead arising from the argumentation process.
2. **Generalization:** While showing promise, the method's effectiveness across more diverse and larger datasets needs further validation.
3. **Real-World Application Testing:** Though promising, additional testing with real-world data, especially in medical and judicial systems, would solidify claims.

## Future Research Directions
1. **Extension to Other Algorithms:** Extensive testing with other algorithms like convolutional neural networks and recurrent neural networks.
2. **Real-World Data Experiments:** Expanding testing to real-world electronic health record data and other critical domains.
3. **Scalability Studies:** Investigating how well the approach scales with larger datasets and more complex problem settings.
4. **Advanced Negotiation Protocols:** Exploring more sophisticated negotiation protocols within the argumentation process to improve classifier interactions.

## Conclusion
This paper presents a significant advancement in the integration of argumentation with deep ensemble methods, addressing a crucial need for transparent and interpretable machine learning models, particularly in critical applications. The proposed method leverages argumentation to not only improve performance but also provide understandable and justifiable predictive outcomes. Future work extending and testing this approach will further its impact and applicability across various domains.

## References
[1] The original paper: A new Transparent Ensemble Method based on Deep learning, by Naziha Sendi, Nadia Abchiche-Mimouni, Farida Zehraoui. Published in Procedia Computer Science, 2019.

[2] Original sources referenced in the paper's bibliography, covering various studies on neural networks, rule extraction techniques, and argumentation theory within AI.
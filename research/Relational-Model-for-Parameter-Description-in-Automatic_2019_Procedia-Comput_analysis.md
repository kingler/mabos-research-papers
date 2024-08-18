# Relational-Model-for-Parameter-Description-in-Automatic_2019_Procedia-Comput

# Title: Relational Model for Parameter Description in Automatic Semantic Web Service Composition

## Summary:
The paper "Relational Model for Parameter Description in Automatic Semantic Web Service Composition" by Paul Diaca, Liana Tu˘cara, and Andrei Netedu, addresses the limitations of current semantic models in web service composition by introducing a new relational model. This model leverages binary relations between the parameters of services, enabling a more expressive and intuitive composition process. The proposed model uses public ontologies and specific relations to match parameters not just based on type but also on semantic context, allowing for the automation of the reasoning process typically performed manually. The research includes an algorithm to compute compositions using this model and an evaluation demonstrating its effectiveness.

## Key Components Analysis

### Main Research Question
How can the expressiveness of semantic models in automatic web service composition be improved to allow automated reasoning processes that closely mirror human manual compositions?

### Methodology

1. **Model Proposal**: Introduce a relational model using public ontologies and binary relations to describe service parameters.
2. **Serialization**: Use standards like WSDL and JSON-LD to serialize data, and extend them to include relations.
3. **Algorithm Development**: Design an algorithm to automate the composition process using the new model.
4. **Evaluation**: Implement the algorithm and evaluate its performance through tests and comparisons with existing benchmarks.

### Key Findings and Results

1. The proposed model allows more meaningful matching of service parameters based on semantic relations.
2. The composition algorithm can work with multiple objects of the same type, a notable improvement over previous models.
3. The implemented algorithm demonstrated efficient service composition and improved expressiveness in non-trivial test scenarios.

### Conclusions and Implications

The authors conclude that the new relational model significantly enhances the expressiveness of web service compositions, making automated composition closer to manual processes. This can potentially lead to larger-scale applications of semantic web services and more accessible service development for providers.

## First-Principle Analysis

### Fundamental Concepts

1. **Ontology**: A structured framework to categorize and relate concepts important for services.
2. **Binary Relations**: Pairs of service parameters to define meaningful interactions beyond type matching.
3. **Inference Rules**: Logical rules applied to deduce new facts based on existing relations and parameters.
4. **Semantic Web Services**: Web services enhanced with semantic data to enable clearer definitions and auto-compositions.

### Methodology Evaluation

The methodology effectively supports the research question by addressing the main limitations of existing models:

1. **Semantic Relations**: Enriching the model with binary relations and inference rules provides the necessary expressiveness.
2. **Serialization and Standards**: By extending established standards like WSDL and JSON-LD, the authors ensure compatibility and ease of adoption.
3. **Algorithm Design**: The developed algorithm can handle the complexity introduced by the enhanced semantic model.

### Validity of Claims

1. **Improved Expressiveness**: The results and examples provided demonstrate improved expressiveness and automation efficiency.
2. **Algorithm Performance**: The evaluation shows that the algorithm can handle non-trivial examples within reasonable time frames, suggesting practical applicability.
3. **Semantic Matching**: The ability to work with multiple objects of the same type and apply complex relations is validated through the test cases.

## Critical Assessment

### Strengths

1. **Innovation**: The introduction of binary relations and inference rules to parameter descriptions is a novel approach.
2. **Comprehensive Evaluation**: The algorithm is tested against generated and benchmark examples, validating its effectiveness.
3. **Standards Compatibility**: Extending existing standards like WSDL and JSON-LD ensures easier integration and adoption.

### Weaknesses

1. **Algorithm Complexity**: The algorithm is computationally intensive (NP-complete), which might limit scalability for very large repositories.
2. **Assumptions on Service Discovery**: The model assumes services are known ahead of time, which might not align with dynamic web environments.
3. **Lack of Real-World Application**: The evaluation focuses on generated and benchmark tests rather than real-world scenarios.

## Future Research Directions

1. **Scalability Improvements**: Enhance the algorithm to handle larger and more complex service repositories efficiently.
2. **Dynamic Discovery**: Incorporate dynamic service discovery to extend the model's applicability in real-world settings.
3. **Real-World Testing**: Apply the model and algorithm to real-world problems to validate practical usefulness and gather feedback for improvements.
4. **Quality of Service (QoS) Metrics**: Integrate more elaborate QoS metrics into the composition process to reflect practical constraints and optimizations.

## Conclusion

The paper "Relational Model for Parameter Description in Automatic Semantic Web Service Composition" provides a significant contribution to the field of semantic web services by introducing a more expressive and intuitive model for service composition. The relational model, combined with an effective algorithm and comprehensive evaluation, demonstrates potential for automating complex reasoning processes typically done manually. While the algorithm's complexity and the assumptions on service discovery present challenges, future research directions offer paths for further enhancement and real-world application. The potential real-world applications and impact of this research are considerable, especially in making web service compositions more accessible and scalable.

## Sources and Research Paper Citation
- [Berners-Lee, T., Hendler, J., & Lassila, O. (2001). The semantic web. Scientific American, 284(5), 28-37.](http://doi.org/10.1038/scientificamerican0501-28)
- [Sintek, M., & Decker, S. (2002). Triple—A query, inference, and transformation language for the semantic web. In International Semantic Web Conference (pp. 364-378). Springer.](http://doi.org/10.1007/3-540-48005-6_32)
- [McIlraith, S. A., Son, T. C., & Zeng, H. (2001). Semantic web services. IEEE intelligent systems, 16(2), 46-53.](http://doi.org/10.1109/5254.920599)
- [Bansal, A., Blake, M. B., Kona, S., Bleul, S., Weise, T., & Jaeger, M. C. (2008). WSC-08: continuing the web services challenge. In 10th Conference on E-Commerce Technology and the Fifth Conference on Enterprise Computing, E-Commerce and E-Services (pp. 351-354). IEEE.](http://doi.org/10.1109/CEC-EEE.2008.34)
- [Weise, T., Bleul, S., Comes, D., & Geihs, K. (2008). Different approaches to semantic web service composition. In 2008 Third International Conference on Internet and Web Applications and Services (pp. 90-96). IEEE.](http://doi.org/10.1109/ICIW.2008.22)
- [Bansal, S., Bansal, A., Gupta, G., & Blake, M. B. (2016). Generalized semantic web service composition. Service Oriented Computing and Applications, 10(2), 111-133.](http://doi.org/10.1007/s11761-015-0187-7)
- [Klusch, M., Kapahnke, P., Schulte, S., Lecue, F., & Bernstein, A. (2016). Semantic web service search: a brief survey. KI-Künstliche Intelligenz, 30(2), 139-147.](http://doi.org/10.1007/s13218-015-0391-9)
- [Lee, D., Kwon, J., Lee, S., Park, S., & Hong, B. (2011). Scalable and efficient web services composition based on a relational database. Journal of Systems and Software, 84(12), 2139-2155.](http://doi.org/10.1016/j.jss.2011.07.013)
- [Viriyasitavat, W., Da Xu, L., & Bi, Z. (2019). The extension of semantic formalization of service workflow specification language. IEEE Transactions on Industrial Informatics, 15(2), 741-754.](http://doi.org/10.1109/TII.2018.2847284)
- [Tu˘car, L., & Diac, P. (2018). Semantic web service composition based on graph search. Procedia Computer Science, 126, 116-125.](http://doi.org/10.1016/j.procs.2018.07.190)
- [Cordella, L. P., Foggia, P., Sansone, C., & Vento, M. (2004). A (sub) graph isomorphism algorithm for matching large graphs. IEEE transactions on pattern analysis and machine intelligence, 26(10), 1367-1372.](http://doi.org/10.1109/TPAMI.2004.75)
- [Ding, W., Wang, J., & Han, Y. (2010). VIPEN: A model supporting knowledge provenance for exploratory service composition. In 2010 IEEE International Conference on Services Computing (pp. 265-272). IEEE.](http://doi.org/10.1109/SCC.2010.41)
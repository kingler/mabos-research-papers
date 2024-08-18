# Ontology-Alignment-using-Stable-Matching_2019_Procedia-Computer-Science

___
# Title: Ontology Alignment using Stable Matching

## Summary:
The paper titled "Ontology Alignment using Stable Matching" by Imene Ouali, Faiza Ghozzi, Raouia Taktak, and Mohamed Saifeddine Hadj Sassi discusses an enhanced method for ontology alignment, a crucial task in addressing semantic heterogeneity in data integration. The authors propose two new structural alignment methods, named Method of Similarity of Inheritance (MSI) and Method of Sibling Similarity (MSS), which consider inheritance and sibling relationships, respectively. Moreover, they integrate the stable marriage algorithm to select optimal mappings, aiming to improve the alignment quality and stability.

## Key Components Analysis

### Main Research Question

The primary research question addressed by the paper is: How can ontology alignment be improved by leveraging structural information and stable matching algorithms to handle semantic heterogeneity more effectively?

### Methodology

The proposed methodology includes:
1. **Pre-matching Phase:** Initial similarity between ontology concepts is computed using string-based pre-processing techniques.
2. **Matching Phase:** 
   - **Method of Similarity of Inheritance (MSI):** Considers inheritance (father/son) relations to compute similarity.
   - **Method of Sibling Similarity (MSS):** Considers sibling relationships.
3. **Post-matching Phase:** Application of the stable marriage algorithm to ensure stable and optimal mappings between concepts.

### Key Findings and Results

1. The integration of structural approaches (MSI and MSS) improves the alignment quality by considering relationships between concepts.
2. The stable marriage algorithm enhances the stability and robustness of the mappings compared to traditional approaches.
3. Experiments show that the proposed methods achieve competitive F-measure scores compared to state-of-the-art ontology alignment systems.

### Conclusions and Implications

The authors conclude that using structural information along with stable matching algorithms can significantly improve ontology alignment's accuracy and stability. This approach is beneficial for integrating heterogeneous data across various domains, such as e-commerce and biology, by providing more reliable semantic mappings.

## First-Principle Analysis

### Fundamental Concepts

1. **Ontology:** Represents structured information in a domain, typically using classes and relationships.
2. **Ontology Matching:** The process of finding correspondences between semantically related entities of different ontologies.
3. **Stable Marriage Algorithm:** An algorithm to find a stable matching between two sets, ensuring that no pair would prefer to be matched with each other over their current matches.

### Methodology Evaluation

1. **Pre-matching Phase:** The initial similarity computation uses well-established string-based pre-processing techniques, which are foundational and provide a reasonable starting point.
2. **MSI and MSS Methods:** Both methods extend basic string similarity by incorporating structural relationships, which is crucial for accurate alignment in structured domains like ontologies.
3. **Stable Marriage Algorithm:** Its application ensures that the final mappings are stable and optimal, reducing the chances of incorrect or suboptimal alignments.

### Validity of Claims

1. **Improved Performance:** The proposed methods are shown to outperform baseline techniques in terms of the F-measure in the evaluation.
2. **Stability and Robustness:** The stable marriage algorithm has theoretical guarantees of stability, which is corroborated by the experimental results.

### Strengths

1. **Novel Integration:** Combines structural relationships and stable matching, addressing both local and global alignment issues.
2. **Robust Evaluation:** Comprehensive experiments and comparisons with state-of-the-art methods validate the approach.
3. **Theoretical Soundness:** The stable marriage algorithm's established properties enhance the reliability of the results.

### Weaknesses

1. **Computational Complexity:** The additional steps for structural similarity and stable matching can introduce computational overhead, which is not thoroughly discussed.
2. **Sensitivity to Parameters:** The choice of parameters (like the contribution percentage "p") in similarity calculations may affect performance and needs careful tuning.

## Future Research Directions

1. **Scalability:** Investigate methods to reduce computational complexity for large-scale ontologies.
2. **Parameter Optimization:** Develop automatic methods for parameter selection to reduce sensitivity.
3. **Application to Complex Ontologies:** Test the approach on more diverse and complex real-world ontologies to further validate its effectiveness.
4. **Use of Semantic Resources:** Integrating additional semantic resources, like WordNet, to enhance similarity measures.

## Conclusion

The paper "Ontology Alignment using Stable Matching" makes a significant contribution to the field of ontology matching by presenting a novel approach that combines structural similarity measures with the stable marriage algorithm. The proposed methods enhance the accuracy and robustness of ontology alignment, addressing key challenges in semantic heterogeneity.

The integration of structural information (inheritance and sibling relationships) and the stable marriage algorithm is well-motivated and theoretically sound. The experimental results demonstrate its effectiveness, making it a competitive alternative to existing state-of-the-art systems.

Future research could focus on improving scalability, parameter optimization, and testing on more complex ontologies. The potential impact of this research is substantial, offering advanced tools for data integration in various domains.

## Sources and Research Paper Citation
[1] Thi Thuy Anh Nguyen and Stefan Conrad. A new structure-based similarity measure for automatic ontology matching. In KDIR, pages 443–449, 2012.
[2] Peter Mork and Philip A Bernstein. Adapting a generic match algorithm to align ontologies of human anatomy. In Data Engineering, 2004.
Proceedings. 20th International Conference on, pages 787–790, 2004.
[3] Cheng Xie, Melisachew Wudage Chekol, Blerina Spahiu, and Hongming Cai. Leveraging structural information in ontology matching. In 30th 
International Conference on Advanced Information Networking and Applications (AINA), 2016 IEEE, pages 1108–1115, 2016.
[4] Ying Wang, Weiru Liu, and David A Bell. A structure-based similarity spreading approach for ontology matching. In International Conference 
on Scalable Uncertainty Management, pages 361–374, 2010.
[5] Mohammad Mehdi Keikha, Mohammad Ali Nematbakhsh, and Behrouz Tork Ladani. Structural weights in ontology matching. arXiv preprint 
arXiv, pages 41–58, 2013.
[6] Baththama Bello Alhassan, Sahalu B Junaidu, and A Obiniyi. Extending an ontology alignment system with a lexical database. Scientific 
Research Journal, pages 12–17, 2015.
[7] Kaladevi Ramar and TT Mirnalinee. heterogeneous information management using ontology mapping. pages 2078–2081, 2015.
[8] Thi Thuy Anh Nguyen and Stefan Conrad. Ontology matching using multiple similarity measures. In Knowledge Discovery, Knowledge 
Engineering, and Knowledge Management (IC3K), 2015 7th International Joint Conference on, pages 603–611, 2015.
[9] Floriana Esposito, Nicola Fanizzi, and Claudia d’Amato. Recovering uncertain mappings through structural validation and aggregation with 
the moto system. In Proceedings of the 2010 ACM Symposium on Applied Computing, pages 1428–1432, 2010.
[10] Aroua Essayeh and Mourad Abed. Towards ontology matching based system through terminological, structural and semantic level. Procedia 
Computer Science, pages 403–412, 2015.
[11] Jean-François Djoufak-Kengue, Jérôme Euzenat, and Petko Valtchev. Alignement d’ontologies dirigé par la structure. In Actes 14e journées 
nationales sur langages et modèles à objets (LMO), pages 43–57, 2008.
[12] Gilles Bisson. Learning in fol with a similarity measure. In Proceedings of the National Conference on Artificial Intelligence, pages 82–82, 
1992.
[13] Isabel F Cruz and William Sunna. Structural alignment methods with applications to geospatial ontologies. journal: Transactions in GIS, 
pages 683–711, 2008.
[14] David Gale and Lloyd S Shapley. College admissions and the stability of marriage. The American Mathematical Monthly, pages 9–15, 1962.
[15] Dan Gusfield and Robert W Irving. The stable marriage problem: structure and algorithms. 2013.
[16] Ernesto Jiménez-Ruiz and Bernardo Cuenca Grau. Logmap: Logic-based and scalable ontology matching. In International Semantic Web 
Conference, pages 273–288, 2011.
[17] Warith Eddine Djeddi and Mohammed Tarek Khadir. Xmap: a novel structural approach for alignment of owl-full ontologies. In Machine and 
Web Intelligence (ICMWI), 2010 International Conference on, pages 368–373, 2010.
___
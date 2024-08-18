# LANGUAGE MODELS ARE OPEN KNOWLEDGE GRAPHS

# Title: Language Models Are Open Knowledge Graphs
![[LANGUAGE MODELS ARE OPEN KNOWLEDGE GRAPHS_analysis.pdf]]

## Summary
The paper "Language Models Are Open Knowledge Graphs" by Chenguang Wang, Xiao Liu, and Dawn Song from UC Berkeley and Tsinghua University demonstrates how knowledge graphs can be constructed from pre-trained language models (LMs) such as BERT and GPT-2/3 without human supervision. The authors propose an unsupervised method termed "MAMA" (Match and Map) to generate knowledge graphs by leveraging the factual knowledge embedded in these language models during a single forward pass. The proposed method extracts candidate facts and then maps them to existing schemas, creating a new type of knowledge graph, termed as “open KG”, that mixes fixed schemas with novel unmapped facts.

## Key Components Analysis

### Main Research Question
Can pre-trained language models be used to construct knowledge graphs without human supervision?

### Methodology
The authors implement MAMA, a two-stage unsupervised approach to extract and map facts from a corpus utilizing a pre-trained language model:

1. **Match Stage**: 
   - Generates candidate facts using attention weight matrices from a single forward pass of the pre-trained LM (such as BERT or GPT-2/3).
   - Uses a beam search algorithm to find candidate facts that represent (head, relation, tail) triplets from sentences in the corpus.
   - Applies constraints to filter less relevant or incorrect candidate facts.

2. **Map Stage**:
   - Maps the candidate facts to a fixed schema (e.g., Wikidata or TAC KBP) when possible.
   - Identifies and maintains unmapped facts in an open schema, expanding the knowledge graph with new facts not present in the existing schemas.

### Key Findings and Results
1. **Knowledge Graph Construction**:
   - MAMA successfully constructs knowledge graphs from pre-trained LMs without fine-tuning.
   - Resulting knowledge graphs (open KGs) contain both mapped facts to existing schemas and new unmapped facts.

2. **Performance Evaluation on TAC KBP and Wikidata**:
   - MAMA outperforms traditional open IE systems like OpenIE and Stanford OpenIE on the TAC Knowledge Base Population (KBP) task.
   - The quality of open KGs is verified by comparing mapped facts against oracle KGs annotated by humans on datasets like TAC KBP and Wikidata.
   - Larger and deeper LMs (GPT-2 XL) produce higher-quality knowledge graphs.

3. **Unmapped Facts**:
   - Approximately 35.3% of unmapped facts are true facts that extend beyond the current knowledge present in Wikidata.

### Conclusions
The authors conclude that pre-trained language models can indeed construct knowledge graphs autonomously, enriching existing knowledge databases with new facts. The proposed MAMA approach has broad implications for advancing knowledge graph construction, deep neural network interpretation, and information extraction. The research also suggests that larger language models may contain even more knowledge, and using extensive high-quality text corpora can further enhance the generated knowledge graphs.

## First-Principle Analysis

### Fundamental Concepts
1. **Knowledge Graphs (KGs)**:
   - Structured representations of knowledge involving entities (nodes) and relationships (edges).

2. **Language Models (LMs)**:
   - Deep learning models pre-trained on large text corpora to capture linguistic patterns and factual knowledge implicitly.

3. **MAMA Approach**:
   - A methodology to extract and map factual knowledge from LMs into structured KGs.

### Methodology Evaluation
1. **Support for Research Question**:
   - The methodology effectively captures factual knowledge without human intervention, demonstrating strong potential for automating KG construction.

2. **Experimental Design**:
   - The use of diverse datasets (e.g., TAC KBP and Wikidata) and systematic evaluation ensures comprehensive validation of the proposed approach.

3. **Beam Search and Constraints**:
   - The beam search algorithm optimally navigates through attention matrices to generate accurate candidate facts.
   - Constraints enhance the reliability and relevance of extracted facts.

### Validity of Claims
1. **Performance Metrics**:
   - The reported results on precision, recall, and F1-score demonstrate the effectiveness of MAMA compared to existing IE systems.

2. **Statistical Significance**:
   - While the paper shows consistent improvements and qualitative assessments, further statistical significance tests could fortify the claims.

3. **Unmapped Facts**:
   - Analysis of unmapped facts highlights the method's ability to discover new, accurate knowledge extending beyond the reference KGs.

## Critical Assessment

### Strengths
1. **Innovative Approach**:
   - MAMA leverages the hidden knowledge in pre-trained LMs to automate KG construction, addressing a significant research gap.

2. **Comprehensive Evaluation**:
   - Extensive comparison with established methods and evaluation on large datasets provide robust validation.

3. **Expansion Potential**:
   - The generation of open KGs holds potential for continuous enrichment of existing knowledge bases.

### Weaknesses
1. **Dependency on Pre-trained Models**:
   - The approach relies heavily on the quality and size of pre-trained LMs, which may limit applicability to only those with access to such resources.

2. **Error Sources and Fine-tuning**:
   - Errors in entity detection and relation mapping underline the need for possible fine-tuning or additional filtering techniques.

3. **Computational Resources**:
   - The process, especially with larger models, is computationally intensive, posing potential access issues for smaller research groups.

## Future Research Directions
1. **Scaling with Larger Models**:
   - Applying MAMA to GPT-3 or similar large models could further enhance KG quality and coverage.

2. **Error Mitigation**:
   - Improving entity detection and relation mapping through more advanced NLP techniques or additional training data.
    
3. **Interpretabllity**:
   - Developing methods to better interpret the knowledge encapsulated in LMs and understand the rationale behind the extracted facts.

4. **Cross-Lingual Knowledge Graphs**:
   - Extending the approach to construct cross-lingual KGs by leveraging multilingual LMs.

## Conclusion
The paper establishes a significant breakthrough in automating the construction of knowledge graphs using pre-trained language models. MAMA effectively exploits the implicit knowledge in LMs to generate both mapped and novel unmapped facts into structured KGs. This research could substantially enhance the scalability and comprehensiveness of knowledge bases, benefiting diverse applications in AI and beyond.

While the methodology and results are compelling, continued advances in LM capabilities, improved error handling, and more scalable methodologies will further solidify the approach. The potential for integrating increasingly sophisticated models into the MAMA framework opens exciting possibilities for the next generation of intelligent knowledge systems.
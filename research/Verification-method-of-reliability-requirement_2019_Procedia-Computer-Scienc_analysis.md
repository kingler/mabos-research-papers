# Verification-method-of-reliability-requirement_2019_Procedia-Computer-Scienc

# Verification method of reliability requirement: 2019 Procedia Computer Science

## Summary:

The paper "Verification method of reliability requirements" by Satsuki Yamada, Takayuki Omori, and Atsushi Ohnishi explores a structured method to rigorously verify non-functional reliability requirements in software development. The authors present an extended requirements frame model and verification approach. Their method specifically targets ensuring consistency, non-redundancy, unambiguity, and completeness of reliability requirements. They provide a detailed methodology supported by examples and discuss the designed prototype system for the verification of these requirements.

## Key Components Analysis

### Main Research Question

How can non-functional reliability requirements be verified effectively to ensure they are consistent, non-redundant, unambiguous, and complete?

### Methodology

The authors propose a novel method based on an extended requirements frame model. Key steps are:

1. Derivation of reliability requirements from SRS using specific keywords.
2. Verification of these requirements using a frame model to ensure consistency, non-redundancy, unambiguity, and completeness.
3. Implementation of a prototype system for automated verification.

The methodology involves:
- Exploring nouns and verbs within requirement sentences.
- Using keyword extraction and checking to filter out related requirements.
- Applying a defined noun and case frame to analyze and transform sentences into a Conceptual Requirements Description (CRD) for verification.

### Key Findings and Results

1. The proposed method successfully retrieves reliability requirements with high recall and variable precision.
2. Instances of redundancy, ambiguity, inconsistency, and incompleteness in reliability requirements can be detected using the proposed approach.
3. Experimental results indicate the method's effectiveness in ensuring clear and accurate reliability specifications within software requirement documents.
4. A prototype system is under development, indicating practical feasibility of the method.

### Conclusions and Implications

The authors conclude that their verification method significantly improves the quality of non-functional reliability requirements by ensuring they are well defined and accurately specified. This approach helps find errors and inconsistencies that could lead to significant reliability issues in software.

## First-Principle Analysis

### Fundamental Concepts

1. **Software Requirement Specification (SRS)**: The need for specified, clear, and correct requirements to guide software development.
2. **Non-Functional Requirements (NFR)**: Requirements that outline system attributes such as reliability, performance, and usability.
3. **Requirements Frame Model**: A structure to represent, analyze, and verify requirement statements to ensure they meet desired standards.

### Methodology Evaluation

1. **Keyword Extraction**: The method of deriving keywords related to reliability from existing documents is grounded in textual analysis practices. However, the effectiveness heavily depends on the initial selection of relevant keywords.
2. **Frame Model Application**: The use of a structured model (noun and case frames) to analyze requirements sentences ensures consistent representation and facilitates error detection. This approach builds on established grammatical analysis techniques.
3. **Prototype Development**: The steps outlined for a prototype system show practical application feasibility, bridging theoretical methods with real-world utility.

### Validity of Claims

1. **Recall and Precision**: They report high recall, meaning most relevant reliability requirements are extracted. However, precision varies, indicating some non-relevant requirements are falsely identified, which needs optimization.
2. **Redundancy, Ambiguity, Inconsistency, and Incompleteness**: Practical detection of these errors using the proposed method is demonstrated through examples, supporting the method's validity.
3. **Prototype Feasibility**: While still under development, the outlined system architecture suggests a realistic path to practical implementation.

## Critical Assessment

### Strengths

1. **Systematic Approach**: Introduces a structured methodology to analyze and verify reliability requirements.
2. **Automation Potential**: Development of a prototype system shows practical application, offering a tool for developers to enhance requirement accuracy.
3. **Comprehensive Evaluation**: Covers various aspects of reliability requirement verification, emphasizing completeness and clarity.

### Weaknesses

1. **Keyword Dependence**: The approach relies on the correct identification of keywords. Any omission or poor selection can reduce effectiveness.
2. **Initial Manual Steps**: Initial manual filtering of requirements might be needed, making the process partially labor-intensive.
3. **Scalability**: Application to large and complex SRS documents may present challenges, as some reliability terms are context-sensitive and may be misinterpreted.

### Future Research Directions

1. **Enhanced Keyword Identification**: Using machine learning to dynamically expand and optimize keyword sets for better precision.
2. **Scalability Analysis**: Testing the method on more extensive and varied datasets to ensure robustness and scalability.
3. **Integration of Other NFRs**: Extending the method to cover other non-functional requirements beyond reliability.
4. **User-Friendly Prototype**: Developing a sophisticated, user-friendly prototype that can be used efficiently by software developers without extensive training.

## Conclusion

The paper "Verification method of reliability requirements" marks a significant advancement in the field of software requirement specification verification. By focusing on non-functional reliability requirements, the authors provide a valuable methodology for ensuring that reliability requirements are clear, consistent, and complete. Their approach offers practical insights into automating reliability requirement verification, demonstrating potential real-world applications in improving software development processes.

The primary strength lies in its structured, methodical approach, which aligns well with established principles of software specification analysis. However, challenges such as keyword dependence and the need for initial manual filtering highlight avenues for further refinement.

This research contributes substantially to the field by addressing a critical aspect of software quality assurance, offering practical tools and methodologies that could significantly enhance the reliability of software systems.

## Sources and Research Paper Citation

**Suggested Citation:**
Yamada, S., Omori, T., Ohnishi, A. (2019). Verification method of reliability requirements. Procedia Computer Science, 159, 860–869. http://doi.org/10.1016/j.procs.2019.09.245
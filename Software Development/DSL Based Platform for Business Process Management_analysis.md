# DSL Based Platform for Business Process Management

# Title: DSL Based Platform for Business Process Management

## Summary:
The paper "DSL Based Platform for Business Process Management" by Audris Kalnins, Lelde Lace, Elina Kalnina, and Agris Sostaks discusses the design and implementation of a DSBPMS (Domain-Specific Business Process Management System) using a domain-specific language (DSL). The proposed platform (GraDe3) allows business analysts to create and modify process notations tailored to specific domains, thereby speeding up the development of business process support systems. The platform includes tools for DSL creation, graphical editors, and an execution engine, providing a seamless environment for creating, mapping, and executing business processes.

## Key Components Analysis

### Main Research Question:
The main research question the paper seeks to address is: How can a domain-specific language (DSL) be effectively used to build a Business Process Management System (BPMS) tailored for specific business domains, making it easier and faster for domain experts to define and manage business processes?

### Methodology:
The methodology involves:
1. **Selection and Design of DSL**: Choosing a relevant domain and defining a process specification DSL for it.
2. **Platform Implementation**: Utilizing the GraDe3 platform to create graphical editors for the designed DSL and defining mappings from the DSL to a Base language executable by the platform's engine.
3. **Execution Engine**: Providing a complete runtime environment for the developed DSBPMS.
4. **Example Implementation**: Demonstrating the approach with a case study on internal document processing.

### Key Findings and Results:
1. **Feasibility and Flexibility**: The platform allows the quick and feasible creation of a DSBPMS adapted to specific domains.
2. **Domain-Specific Notations**: Using domain-specific notations speeds up development and makes the process management accessible to business analysts.
3. **Model-driven Development**: Every step from DSL definition to execution is model-driven, enabling automation and precision.
4. **Usability Confirmation**: Initial experiments with GraDe3 and the development of a study process management system confirmed the approach's usability.

### Conclusions and Implications:
The authors conclude that the DSBPMS approach simplifies developing specific business process support systems for different domains. The GraDe3 platform effectively integrates DSL definition, process modeling, and execution, allowing business analysts with minimal technical knowledge to develop and manage business processes.

## First-Principle Analysis

### Fundamental Concepts:
1. **Domain-Specific Language (DSL)**: A specialized language designed to be used within a specific domain.
2. **Business Process Management System (BPMS)**: Software designed to model, execute, and optimize business processes.
3. **Model-Driven Development**: The approach where models play a crucial role in the development process, allowing for automation and precision.

### Methodology Evaluation:
The methodology is quite robust:
- **DSL Design**: Allows customization to specific business domains, ensuring that process notations are relevant and easily understandable by domain experts.
- **Graphical Editors**: Simplifies user interaction and process definitions, especially important for business analysts who may not be familiar with technical specifics.
- **Mapping and Execution Engine**: The mapping from DSL to a Base language ensures that the developed processes can be directly executed, providing a full-cycle BPM solution.

### Validity of Claims:
1. **Feasibility and Flexibility**: The creation of a DSL and the subsequent modeling of processes has been demonstrated through examples, lending validity to the claims.
2. **Usability**: The initial experiments and case studies indicate that the platform can be effectively used by domain experts to manage business processes.
3. **Model-driven Approach**: The entire process, from DSL definition to execution, being model-driven, ensures consistency and reduces errors.

### Alternative Explanations:
- While the proposed platform is powerful, its flexibility could also lead to the misuse or unnecessary complexity if not handled properly.
- The reliance on domain experts for the initial DSL design could mean variability in the quality and effectiveness of the different DSLs created, depending on expertise.

## Critical Assessment

### Strengths:
1. **Customizability**: The approach allows customization to fit specific domain needs, improving relevance and efficiency.
2. **Usability**: Seamless integration of DSL definition, graphical editor creation, and execution environment simplifies the development process for non-technical users.

### Weaknesses:
1. **Initial Setup Complexity**: Although the platform simplifies the process once set up, the initial design and implementation of the DSL might require substantial expertise.
2. **Limited Examples**: More diverse examples across different business domains would strengthen the effectiveness and generalizability of the approach.

## Future Research Directions
1. **Scalability**: Investigating how the platform handles more extensive and more complex business processes across various industries.
2. **User Experience**: Conducting extensive usability studies to refine the graphical editors and mapping tools.
3. **Automation**: Exploring further automation in generating mappings from DSLs to the Base language.
4. **Extension to Real-World Applications**: Implementing and testing the platform in real-world business environments to gather feedback and make necessary improvements.

## Conclusion
The paper "DSL Based Platform for Business Process Management" presents a significant contribution by showing how DSLs can be effectively used to build tailored BPMS. The proposed GraDe3 platform demonstrates the feasibility and benefits of this approach, including faster development times and greater accessibility for business analysts. While the approach has strengths in its customizability and usability, there are areas for further research, particularly around scalability and user experience. The successful implementation and positive initial results indicate that this approach could substantially impact how business processes are managed across various domains.

## Sources and Research Paper Citation
1. BPMN 2.0 specification, http://www.bpmn.org/
2. Genon, N., Heymans, P., Amyot, D.: Analysing the Cognitive Effectiveness of the BPMN 2.0 Visual Notation. In: Malloy, B., Staab, S., van den Brand, M. (eds.) SLE 2010. LNCS, vol. 6563, pp. 377–396. Springer, Heidelberg (2011)
3. Sinur, J., Hill, J.: Magic Quadrant for Business Process Management Suites. In: Gartner RAS Core Research Note G00205212 (2010), http://www.gartner.com/id=1453527
4. IBM Business Process Manager, v 8.5, http://www-03.ibm.com/software/products/us/en/business-process-manager-family
5. Oracle Business Process Management Suite 11g, http://www.oracle.com/us/technologies/bpm/suite/overview/inex.html
6. SAP NetWeaver BPM, http://scn.sap.com/community/bpm
7. Bizagi BPM suite 10.1, http://www.bizagi.com/index.php
8. BonitaSoft - Bonita Open Solution, Open Source BPM, http://www.bonitasoft.com
9. ProcessMaker Workflow management and BPM, http://www.processmaker.com
10. Freudenstein, P.: Web Engineering for Workflow-based Applications: Models, Systems and Methodologies. KIT Scientific Publishing, Karlsruhe (2009)
11. Heitkötter, H.: A Framework for Creating Domain-specific Process Modeling Languages. In: Proceedings of the ICSOFT 2012, pp. 127–136 (2012)
12. Becker, J., Pfeiffer, D., Räckers, M.: Domain specific process modelling in public administrations–the PICTURE-approach. In: Wimmer, M.A., Scholl, J., Grönlund, Å. (eds.) EGOV 2007. LNCS, vol. 4656, pp. 68–79. Springer, Heidelberg (2007)
13. UML specification v.2.4.1, http://www.omg.org/spec/UML
14. Lace, L., Liepiņš, R., Rencis, E.: Architecture and Language for Semantic Reduction of Domain-Specific Models in BPMS. In: Aseeva, N., Babkin, E., Kozyrev, O. (eds.) BIR 2012. LNBIP, vol. 128, pp. 70–84. Springer, Heidelberg (2012)
15. Barzdins, J., Zarins, A., Cerans, K., Rencis, E., et al.: GrTP: Transformation Based Graphical Tool Building Platform. In: Proc. of MDDAUI 2007 Workshop of MODELS 2007, Nashville, Tennessee, USA, CEUR Workshop Proceedings, vol. 297 (2007), http://ceur-ws.org
16. Kozlovics, S., Barzdins, J.: The Transformation-Driven Architecture for interactive systems. In: Automatic Control and Computer Sciences, vol. 47(1/2013), pp. 28–37. Allerton Press, Inc (2013)
17. Sprogis, A.: The Configurator in DSL Tool Building. In: Scientific Papers, vol. 756, pp. 173–192. University of Latvia (2010)
18. Liepiņš, R.: Library for model querying: IQuery. In: Proceedings of the 12th Workshop on OCL and Textual Modelling (OCL 2012), pp. 31–36. ACM, New York (2012)
19. Welcome to e-Expense Travel & Business Expense System. A User Guide, Tufts University, http://finance.tufts.edu/accpay/files/eExpenseGuide.pdf
20. The Ohio State University, eTravel ASSIST, https://assist-erp.osu.edu/assistTravel/index.htm
# business_process_ontology_for_defining_user_story

# Title: Business Process Ontology for Defining User Story

## Summary:
The paper "Business Process Ontology for Defining User Story" by Chaleerat Thamrongchote and Wiwat Vatanawood introduces a method to simplify and enhance the process of writing user stories using a business process ontology. The ontology relies on N-triple data structures and aims to capture the Role-Action-Object relationships within user stories by leveraging historical successful projects. The authors propose an ontology schema design that incorporates classes, hierarchy relations, and properties. They also introduce the concept of synonyms to reduce the complexity of the ontology.

## Key Components Analysis

### Main Research Question
The primary research question addressed in this paper is: How can a business process ontology be designed to assist in writing user stories effectively, by reusing concepts from historical successful projects?

### Methodology
The methodology includes several steps:
1. **Ontology Schema Design**: The ontology is structured using classes and hierarchy relationships.
2. **Role-Action-Object Relations**: Properties are defined to represent these relations within user stories.
3. **Data Collection**: User stories are collected from historical projects.
4. **Hierarchy and Class Definitions**: Words from user stories are categorized into classes and their hierarchical relationships are defined.
5. **Synonym Concept**: Introduce a property to define synonyms, reducing the number of nodes.

### Key Findings and Results
- The proposed ontology captures user stories based on Role-Action-Object relations, facilitating their reuse.
- The ontology schema significantly reduces the number of nodes through synonym properties.
- The business process ontology can effectively guide the writing of user stories for new projects by suggesting likely actions and objects once a role is chosen.

### Conclusions and Implications
The authors conclude that the business process ontology provides a structured and reusable knowledge base for writing user stories. This ontology, designed with synonym properties, simplifies the user story writing process and ensures consistency by leveraging historical project data.

## First-Principle Analysis

### Fundamental Concepts
1. **Ontology**: A formal representation of knowledge as a set of concepts within a domain and the relationships between those concepts.
2. **User Stories**: In Agile development, concise descriptions of a software feature from the perspective of an end-user.
3. **N-Triples**: A format for representing data in RDF (Resource Description Framework), used to express facts as subject-predicate-object triples.

### Methodology Evaluation
The methodology supports the research question by systematically building an ontology to streamline user story creation:
1. **Ontology Schema Design**: Provides a foundational structure by clearly defining classes and hierarchy.
2. **Role-Action-Object Relations**: Ensures user stories are captured with clear and actionable relationships.
3. **Data Collection**: Using historical project data grounds the ontology in practical, proven user stories.
4. **Class Definitions and Hierarchy**: The tree structure for classifies helps in easy navigation and understanding of dependencies.
5. **Synonym Concept**: Reduces redundancy, improving the efficiency and manageability of the ontology.

### Validity of Claims
1. **Structured User Stories**: The ontology's structured approach supports the claim that it facilitates user story writing.
2. **Synonym Property**: Effectively demonstrated to reduce complexity without loss of information.
3. **Reusability of User Stories**: The use of historical project data substantiates the ease of reusing user stories.

## Critical Assessment

### Strengths
1. **Innovative Approach**: Provides a novel way of leveraging ontologies for user story creation in Agile.
2. **Reduces Redundancy**: The use of synonyms reduces the complexity of the ontology graph.
3. **Practical Application**: Grounded in historical successful projects, enhancing its practical relevance.

### Weaknesses
1. **Scalability**: The paper does not discuss the scalability of the ontology with increasingly complex projects.
2. **Computational Overhead**: No mention of the computational resources required to manage and query the ontology.
3. **Generalization Beyond Scope**: Focuses primarily on business processes related to user stories, but may not generalize well to other forms of requirement engineering.

## Future Research Directions

1. **Scalability Analysis**: Investigate how the ontology scales with large and complex projects.
2. **Automated Synonym Detection**: Develop algorithms to automatically identify and assign synonyms.
3. **Integration with Other Tools**: Explore integrating the ontology with other Agile tools and platforms for seamless user story management.

## Conclusion

The paper "Business Process Ontology for Defining User Story" makes a significant contribution to the field of requirements engineering in Agile methodologies. By leveraging ontologies, the authors present an innovative approach to writing and reusing user stories, grounded in historical project data. The structured ontology simplifies the user story creation process and reduces redundancy through the concept of synonyms.

While the methodology is robust and well-supported, there are areas for improvement, particularly around scalability and computational efficiency. Despite these limitations, the research provides a solid foundation for future developments in using ontologies for Agile requirement engineering.

The potential impact of this research is notable, especially in streamlining the process of creating consistent and reusable user stories. Future research directions offer exciting opportunities to refine and expand upon this foundational work, potentially leading to more sophisticated and efficient tools for Agile development.

## Sources and Research Paper Citation
[1] Leffingwell, D., "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise." Addison-Wesley, 2011.
[2] Abrahamson P., Salo O., Ronkainen J., Warsta J., "Agile software development methods: Review and analysis (Technical report)." VTT, 2002.
[3] Gruber, Thomas R., "A Translation Approach to Portable Ontology Specifications." Knowledge Acquisition, 1993.
[4] Noy, Natalya F., and McGuinness, Deborah L., "Ontology development 101: A guide to creating your first ontology." Stanford University, 2001.
[5] Phillip Lord, "Components of an Ontology." Ontogenesis, 2010. http://ontogenesis.knowledgeblog.org/514
[6] Cohn, M., "User stories applied: for Agile software development." Addison-Wesley, 2004.
[7] Zeaaraoui, A., Bougroun, Z., Belkasmi, M.G., and Bouchentouf, T., "User stories template for object-oriented applications," Innovative Computing Technology (INTECH), 2013 Third International Conference on. London, 2013, pp. 407-410.
[8] Zeaaraoui, A., Bougroun, Z., Belkasmi, M.G., and Bouchentouf, T., "Object-oriented analysis and design approach for requirements engineering," Innovative Computing Technology (INTECH), 2012 Second International Conference on. Casablanca, 2012, pp. 133-133-137.

___
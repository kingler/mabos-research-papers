# Code: ontology.py

```python
# knowledge/ontology.py
from typing import Dict, List, Any, Optional

class Concept:
    def __init__(self, name: str):
        self.name = name
        self.properties: Dict[str, Any] = {}
        self.relations: Dict[str, 'Concept'] = {}

    def add_property(self, name: str, value: Any):
        self.properties[name] = value

    def add_relation(self, name: str, target: 'Concept'):
        self.relations[name] = target

    def __str__(self):
        return f"Concept({self.name})"

class Ontology:
    def __init__(self):
        self.concepts: Dict[str, Concept] = {}

    def add_concept(self, name: str) -> Concept:
        if name not in self.concepts:
            self.concepts[name] = Concept(name)
        return self.concepts[name]

    def get_concept(self, name: str) -> Optional[Concept]:
        return self.concepts.get(name)

    def add_property(self, concept_name: str, property_name: str, value: Any):
        concept = self.get_concept(concept_name)
        if concept:
            concept.add_property(property_name, value)

    def add_relation(self, from_concept: str, relation: str, to_concept: str):
        concept1 = self.get_concept(from_concept)
        concept2 = self.get_concept(to_concept)
        if concept1 and concept2:
            concept1.add_relation(relation, concept2)

    def query(self, concept_name: str, property_name: Optional[str] = None) -> Any:
        concept = self.get_concept(concept_name)
        if not concept:
            return None
        if property_name:
            return concept.properties.get(property_name)
        return concept

    def get_related_concepts(self, concept_name: str, relation: str) -> List[Concept]:
        concept = self.get_concept(concept_name)
        if not concept:
            return []
        return [related_concept for rel, related_concept in concept.relations.items() if rel == relation]

# Example usage
if __name__ == "__main__":
    ontology = Ontology()

    # Add concepts
    ontology.add_concept("Person")
    ontology.add_concept("Company")
    ontology.add_concept("Job")

    # Add properties
    ontology.add_property("Person", "age", 30)
    ontology.add_property("Company", "name", "Tech Corp")
    ontology.add_property("Job", "title", "Software Engineer")

    # Add relations
    ontology.add_relation("Person", "works_for", "Company")
    ontology.add_relation("Person", "has_job", "Job")

    # Query the ontology
    person = ontology.query("Person")
    print(f"Person age: {ontology.query('Person', 'age')}")

    company = ontology.query("Company")
    print(f"Company name: {ontology.query('Company', 'name')}")

    # Get related concepts
    person_job = ontology.get_related_concepts("Person", "has_job")
    print(f"Person's job: {person_job[0] if person_job else 'None'}")

```
# Code: knowledge_graph.py

```python
# knowledge/knowledge_graph.py
from typing import Dict, List, Any, Optional
import networkx as nx
import matplotlib.pyplot as plt

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id: str, properties: Dict[str, Any] = None):
        """Add a node to the knowledge graph."""
        self.graph.add_node(node_id, **properties or {})

    def add_edge(self, from_node: str, to_node: str, relation: str, properties: Dict[str, Any] = None):
        """Add an edge (relation) between two nodes in the knowledge graph."""
        self.graph.add_edge(from_node, to_node, relation=relation, **properties or {})

    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a node's properties from the knowledge graph."""
        return self.graph.nodes.get(node_id)

    def get_relations(self, node_id: str) -> List[Dict[str, Any]]:
        """Get all relations (edges) for a given node."""
        relations = []
        for _, to_node, data in self.graph.out_edges(node_id, data=True):
            relations.append({
                "to_node": to_node,
                "relation": data["relation"],
                **data
            })
        return relations

    def query(self, start_node: str, relation_path: List[str]) -> List[str]:
        """
        Query the knowledge graph starting from a node and following a path of relations.
        Returns the end nodes of all paths that match the relation path.
        """
        current_nodes = [start_node]
        for relation in relation_path:
            next_nodes = []
            for node in current_nodes:
                for _, to_node, data in self.graph.out_edges(node, data=True):
                    if data["relation"] == relation:
                        next_nodes.append(to_node)
            current_nodes = next_nodes
            if not current_nodes:
                break
        return current_nodes

    def visualize(self, output_file: str = "knowledge_graph.png"):
        """Visualize the knowledge graph and save it as an image."""
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(12, 8))
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8, font_weight='bold')
        edge_labels = nx.get_edge_attributes(self.graph, 'relation')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Knowledge Graph Visualization")
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()

# Example usage
if __name__ == "__main__":
    kg = KnowledgeGraph()

    # Add nodes
    kg.add_node("Alice", {"age": 30, "occupation": "Engineer"})
    kg.add_node("Bob", {"age": 35, "occupation": "Manager"})
    kg.add_node("TechCorp", {"industry": "Technology"})
    kg.add_node("ProjectX", {"status": "In Progress"})

    # Add relations
    kg.add_edge("Alice", "TechCorp", "works_for")
    kg.add_edge("Bob", "TechCorp", "works_for")
    kg.add_edge("Alice", "ProjectX", "works_on")
    kg.add_edge("Bob", "ProjectX", "manages")

    # Query the knowledge graph
    print("Employees of TechCorp:", kg.query("TechCorp", ["works_for"]))
    print("Projects Alice works on:", kg.query("Alice", ["works_on"]))

    # Visualize the knowledge graph
    kg.visualize()

```
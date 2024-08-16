# app/core/world_ontology.py
from owlready2 import get_ontology

class WorldOntology:
    def __init__(self, ontology_path: str):
        self.onto = get_ontology(ontology_path).load()

    def update(self, new_information):
        # Method to update the ontology with new information
        for key, value in new_information.items():
            if key == "agents":
                for agent_info in value:
                    agent = self.onto.WorldAgent(agent_info["name"])
                    for prop, prop_value in agent_info.items():
                        if prop != "name":
                            setattr(agent, prop, prop_value)
            elif key == "environments":
                for env_info in value:
                    env = self.onto.WorldEnvironment(env_info["name"])
                    for prop, prop_value in env_info.items():
                        if prop != "name":
                            setattr(env, prop, prop_value)
            elif key == "actions":
                for action_info in value:
                    action = self.onto.WorldAction(action_info["name"])
                    for prop, prop_value in action_info.items():
                        if prop != "name":
                            setattr(action, prop, prop_value)
            else:
                # Handle other classes or properties
                pass
        
        self.onto.save()
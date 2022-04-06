from typing import Dict, List, Text, Any, TYPE_CHECKING

import rasa.shared.core.events


if TYPE_CHECKING:
    from rasa.shared.core.events import Event


class Dialogue:
    def __init__(self, name: Text, events: List["Event"]) -> None:
        self.name = name
        self.events = events

    def __str__(self) -> Text:

        return "Dialogue with name '{}' and turns:\n{}".format(
            self.name, "\n\n".join([f"\t{t}" for t in self.events])
        )

    def as_dict(self) -> Dict:

        return {"events": [event.as_dict() for event in self.events], "name": self.name}

    @classmethod
    def create_from_parameters(cls, parameters: Dict[Text, Any]) -> "Dialogue":

        return cls(
            parameters.get("name"),
            rasa.shared.core.events.deserialise_events(parameters.get("events", [])),
        )

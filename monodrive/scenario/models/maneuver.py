from . import BaseModel
from monodrive.scenario.models.event import parse_events


class Maneuver(BaseModel):
    def __init__(self, xml_data):
        self.name = xml_data.get('name')
        self.events = parse_events(xml_data.findall('Event'))

    @property
    def to_json(self):
        return {
            "name": self.name,
            "events": [e.to_json for e in self.events]
        }

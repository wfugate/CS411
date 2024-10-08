from typing import Optional
from ..habitat_management.habitat import Habitat


class MigrationPath:

    def __init__(self, path_id
                 ,start_location: Habitat
                 , destination: Habitat, species: str
                 , duration: Optional[int] = None):
        self.path_id = path_id
        self.start_location = start_location
        self.destination = destination
        self.duration = duration
        self.specied = species
        


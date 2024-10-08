from typing import Optional, List
from .habitat import Habitat
from ..animal_management.animal import Animal


class HabitatManager:

    def __init__(self) -> None:
        habitats: dict[int, Habitat] = {}

    def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass

    def remove_habitat(habitat_id: int) -> None:
        pass

    def get_habitat_by_id(habitat_id: int) -> Habitat:
        pass


    def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]:
        pass

    def get_habitats_by_size(size: int) -> List[Habitat]:
        pass

    def get_habitats_by_type(environment_type: str) -> List[Habitat]:
        pass



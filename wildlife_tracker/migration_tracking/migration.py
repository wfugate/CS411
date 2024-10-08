from typing import Any
from ..migration_tracking.migration_path import MigrationPath

class Migration:

    def __init__(self, migration_id: int, migration_path: MigrationPath,
                 start_date: str, current_location: str, status: str = "Scheduled"):
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.status = status
        self.start_date = start_date
        self.current_location = current_location

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass

        

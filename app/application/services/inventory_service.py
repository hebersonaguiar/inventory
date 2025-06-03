from app.adapters.repositories.inventory_repository import InventoryRepository

class InventoryService:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def get_hostname(self, data: dict):
        return self.repository.get_hostname(data)

    def up_host(self, data: dict):
        self.repository.update_host(data)

    def add_host(self, data: dict):
        self.repository.insert_host(data)
from app.adapters.repositories.inventory_repository import InventoryRepository

class InventoryService:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def get_inventory_by_hostname(self, data: dict):
        return self.repository.get_inventory_by_hostname(data)

    def get_inventory(self):
        return self.repository.get_inventory()

    def up_host(self, data: dict):
        self.repository.update_host(data)

    def insert_inventory(self, data: dict):
        self.repository.insert_inventory(data)

    def send_to_queue(self, data: dict):
        self.repository.send_to_queue(data)
from typing import Protocol

class InventoryRepository(Protocol):
    def get_inventory_by_hostname(self, data: dict) -> str:
        ...

    def get_inventory(self) -> str:
        ...

    def update_host(self, data: dict) -> None:
        ...

    def insert_host(self, data: dict) -> None:
        ...

    def send_to_queue(self, data: dict) -> None:
        ...
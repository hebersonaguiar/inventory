## Inventory

## Structure
inventory/
├── app/
│   ├── __init__.py
│   ├── domain/
│   │   ├── entities/
│   │   │   └── inventory.py
│   │   ├── repositories/
│   │   │   └── inventory_repository.py
│   │   └── services/
│   │       └── inventory_service.py
│   ├── application/
│   │   └── use_cases/
│   │       └── process_inventory.py
│   ├── infrastructure/
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   └── mysql_inventory_repository.py
│   │   ├── messaging/
│   │   │   ├── __init__.py
│   │   │   └── rabbitmq_consumer.py
│   │   └── web/
│   │       ├── __init__.py
│   │       └── routes/
│   │           └── inventory_routes.py
│   ├── config/
│   │   └── settings.py
│   ├── interface/
│   │   └── api/
│   │       └── routes.py
│   ├── adapters/
│   │   └── repositories/
│   │       └── inventory_repository.py 
│   └── main.py
├── tests/
│   ├── domain/
│   ├── application/
│   └── infrastructure/
├── .env
├── requirements.txt
└── README.md

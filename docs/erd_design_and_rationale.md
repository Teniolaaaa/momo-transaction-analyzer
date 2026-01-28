# ERD Design and Rationale

## Overview
The Entity Relationship Diagram (ERD) was designed to model the core entities and relationships in a mobile money transaction system. The main goals were to ensure data integrity, support analytics, and allow for future scalability.

## Key Design Decisions
- **Users**: Central entity for all transactions, uniquely identified by user_id.
- **Transactions**: Captures all money movements, with sender and receiver as foreign keys to Users.
- **Transaction_Categories**: Normalizes transaction types for analytics and reporting.
- **Transaction_Participants**: Supports many-to-many relationships and roles in transactions.
- **System_Logs**: Provides traceability and error tracking for all operations.

## Relationships
- Foreign keys enforce referential integrity between tables.
- Many-to-many relationships are resolved with a junction table (Transaction_Participants).
- All relationships are shown in the ERD with PK and FK labels.

## Rationale
- The design supports efficient queries for user activity, transaction history, and category-based analytics.
- Normalization reduces redundancy and improves data quality.
- The schema is extensible for future features (e.g., new transaction types, audit logs).

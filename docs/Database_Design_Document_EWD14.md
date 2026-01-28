# MoMo Transaction Analyzer
**Database Design Document**  
**Group:** EWD 14  
**Date:** January 2026

---

## Table of Contents
1. Introduction  
2. Team & Collaboration  
3. ERD Diagram  
4. Design Rationale  
5. Data Dictionary  
6. Sample SQL Queries & Results  
7. Security & Accuracy Rules  
8. JSON Data Modeling  
9. AI Usage Log  
10. References

---

## 1. Introduction
The MoMo Transaction Analyzer is a collaborative project by Group EWD 14, designed to transform raw mobile money SMS/XML data into structured, actionable insights. Our goal was to create a robust, scalable database and a user-friendly dashboard, leveraging each team member’s strengths and working closely together throughout the process.

---

## 2. Team & Collaboration
**Team Members & Roles:**
- **Teniola Adam Olaleye** (Team Lead): Coordinated the project, led ETL and database design, and ensured everyone’s voice was heard.
- **Gael Kamunuga Mparaye:** Led XML parsing, collaborating with Michaella for data validation.
- **Kevin Manzi:** Designed the dashboard, working with Rajveer to ensure frontend-backend integration.
- **Michaella Kamikazi Karangwa:** Led testing and data validation, often pairing with Gael for quality checks.
- **Rajveer Singh Jolly:** Documented our process, kept the README up to date, and helped Kevin with user experience.

> **How We Worked:**  
> We split tasks based on strengths, but always reviewed each other’s work. We held regular check-ins, shared screens, and used GitHub Projects to track progress. Every member contributed code, ideas, and feedback.

---

## 3. ERD Diagram
*See below for our Entity Relationship Diagram, exported from Draw.io/Lucidchart based on our team’s design discussions.*

![ERD Diagram](docs/erd_diagram.png)

---

## 4. Design Rationale
Our database design was driven by the need to efficiently store, query, and analyze MoMo transaction data while maintaining integrity and supporting future scalability. We identified key entities (Users, Transactions, Transaction_Categories, System_Logs) and resolved many-to-many relationships with a junction table (Transaction_Participants).  
*For a detailed rationale and attribute list, see `docs/erd_design_and_rationale.md`.*

---

## 5. Data Dictionary
| Table                     | Column             | Type           | Description                                 |
|---------------------------|--------------------|----------------|---------------------------------------------|
| Users                     | user_id            | INT, PK        | Unique user/customer ID                     |
|                           | phone_number       | VARCHAR(20)    | User phone number (unique)                  |
|                           | name               | VARCHAR(100)   | User name (optional)                        |
|                           | created_at         | DATETIME       | Account creation timestamp                  |
| Transactions              | transaction_id     | INT, PK        | Unique transaction ID                       |
|                           | transaction_code   | VARCHAR(30)    | Transaction reference code (unique)         |
|                           | transaction_date   | DATETIME       | Date and time of transaction                |
|                           | amount             | DECIMAL(15,2)  | Transaction amount                          |
|                           | description        | VARCHAR(255)   | Transaction description                     |
|                           | sender_id          | INT, FK        | FK to Users (sender)                        |
|                           | receiver_id        | INT, FK        | FK to Users (receiver, optional)            |
|                           | category_id        | INT, FK        | FK to Transaction_Categories                |
| Transaction_Categories    | category_id        | INT, PK        | Unique category ID                          |
|                           | category_name      | VARCHAR(50)    | Transaction type/category (unique)          |
|                           | description        | VARCHAR(255)   | Category description                        |
| System_Logs               | log_id             | INT, PK        | Unique log entry ID                         |
|                           | log_time           | DATETIME       | Log timestamp                               |
|                           | log_level          | VARCHAR(20)    | Log severity (INFO, ERROR, etc.)            |
|                           | message            | TEXT           | Log message                                 |
|                           | transaction_id     | INT, FK        | FK to Transactions (optional)               |
| Transaction_Participants  | transaction_id     | INT, PK, FK    | FK to Transactions                          |
|                           | user_id            | INT, PK, FK    | FK to Users                                 |
|                           | role               | ENUM           | Role in transaction (sender/receiver/other) |

---

## 6. Sample SQL Queries & Results
**Create:**  
_Add a new user_  
```sql
INSERT INTO Users (phone_number, name) VALUES ('+250799999999', 'Sam Test');
```
*Adds a new user to the Users table. Used for onboarding new customers.*

**Read:**  
_List all transactions with sender and receiver info_  
```sql
SELECT t.transaction_id, t.transaction_code, t.amount, u1.name AS sender, u2.name AS receiver
FROM Transactions t
JOIN Users u1 ON t.sender_id = u1.user_id
LEFT JOIN Users u2 ON t.receiver_id = u2.user_id;
```
*Shows each transaction, who sent it, and who received it. Useful for audits and reports.*

**Update:**  
_Update a user's name_  
```sql
UPDATE Users SET name = 'Samuel Test' WHERE user_id = 6;
```
*Corrects or updates a user’s name in the database.*

**Delete:**  
_Delete a transaction_  
```sql
DELETE FROM Transactions WHERE transaction_id = 5;
```
*Removes a transaction record, e.g., if it was entered in error.*

**[Insert screenshots of query results here]**

---

## 7. Security & Accuracy Rules
- All tables use primary and foreign key constraints to ensure referential integrity.
- The `amount` field in Transactions uses a CHECK constraint to prevent negative values.
- Unique constraints on phone numbers and transaction codes prevent duplicates.
- ENUMs and NOT NULL constraints enforce data validity.
- Only authorized users can access or modify sensitive tables (if implemented).

**[Insert screenshots of constraint enforcement or error messages here]**

---

## 8. JSON Data Modeling
Our API and data exports use JSON structures that mirror our SQL tables, with nested objects for relationships.  
*See `examples/json_schemas.json` for full examples.*

Example (simplified):
```json
{
  "transaction_id": 1,
  "transaction_code": "TXN001",
  "amount": 75000.00,
  "sender": {
    "user_id": 1,
    "name": "John Doe"
  },
  "receiver": {
    "user_id": 2,
    "name": "Jane Smith"
  },
  "category": {
    "category_id": 1,
    "category_name": "received"
  }
}
```

---

## 9. AI Usage Log
**Project:** MoMo Transaction Analyzer  
**Team:** EWD 14  
**Date:** January 2026

- **Diagramming:** Used dbdiagram.io solely for drawing and exporting the ERD diagram image, based on our team’s original database design. No AI was used to generate or design the database structure, relationships, or business logic.
- **Grammar and Syntax Checking:** AI tools were used for grammar and syntax checking in documentation, and for code syntax verification. No business logic, technical explanations, or reflection content was generated by AI.
- **Research:** We used AI tools to research MySQL best practices (such as index usage and constraint recommendations). All research was cited where appropriate.
- **Attribution:** All technical explanations, database design, and documentation are original and team-specific. Any AI-assisted code or text is clearly marked and limited to non-logic tasks.

**Compliance Statement:**  
This project fully complies with the course AI usage policy. All substantive design, logic, and reflection content was created by team members. AI was used only for allowed purposes and is transparently documented here.

---

## 10. References
- MySQL Documentation  
- dbdiagram.io  
- [Any other sources or tools used]

---

**[End of Document]**

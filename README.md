
# MoMo Transaction Analyzer

---

## Team Information

- **Team Name:** MoMo Analytics Team
- **Team Members:**
   <!--
- Web browser
- Git

   # MoMo Transaction Analyzer

### Installation Steps

   ```bash
   git clone https://github.com/Teniolaaaa/momo-transaction-analyzer.git
   cd momo-transaction-analyzer
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the ETL pipeline**
   ```bash
   ```
4. **View the dashboard**
   - Open `index.html` in your web browser.


## Database Design

### Entity Relationship Diagram (ERD)


*See docs/erd_diagram.txt for ASCII version and docs/erd_design_and_rationale.md for rationale.*

### Data Dictionary (Sample)
| Table                     | Column             | Type           | Description                                 |
|---------------------------|--------------------|----------------|---------------------------------------------|
| Users                     | user_id            | INT, PK        | Unique user/customer ID                     |
|                           | phone_number       | VARCHAR(20)    | User phone number (unique)                  |
|                           | name               | VARCHAR(100)   | User name (optional)                        |
| Transactions              | transaction_id     | INT, PK        | Unique transaction ID                       |
|                           | transaction_code   | VARCHAR(30)    | Transaction reference code (unique)         |
|                           | transaction_date   | DATETIME       | Date and time of transaction                |
|                           | amount             | DECIMAL(15,2)  | Transaction amount                          |
|                           | description        | VARCHAR(255)   | Transaction description                     |
|                           | sender_id          | INT, FK        | FK to Users (sender)                        |
|                           | receiver_id        | INT, FK        | FK to Users (receiver, optional)            |
|                           | category_id        | INT, FK        | FK to Transaction_Categories                |
| Transaction_Categories    | category_id        | INT, PK        | Unique category ID                          |
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

## Sample SQL Queries

**Create:**
```sql
INSERT INTO Users (phone_number, name) VALUES ('+250799999999', 'Sam Test');
```
**Read:**
```sql
SELECT t.transaction_id, t.transaction_code, t.amount, u1.name AS sender, u2.name AS receiver
FROM Transactions t
JOIN Users u1 ON t.sender_id = u1.user_id
LEFT JOIN Users u2 ON t.receiver_id = u2.user_id;
```
**Update:**
```sql
UPDATE Users SET name = 'Samuel Test' WHERE user_id = 6;
```
```sql
DELETE FROM Transactions WHERE transaction_id = 5;
```





---

## Project Management

<!--
   MoMo Transaction Analyzer
   ========================
-->

# MoMo Transaction Analyzer

> _Turning raw MoMo SMS data into actionable insights, together._

---

## 👥 Team & Collaboration

- **Team Name:** MoMo Analytics Team
- **Members:**
   - Teniola Adam Olaleye (Team Lead)
   - Kevin Manzi
   - Rajveer Singh Jolly
   - Gael Kamunuga Mparaye
   - Michaella Kamikazi Karangwa
- **How We Work:**
   - We believe in open communication, regular check-ins, and shared responsibility.
   - Each member brings unique strengths—ETL, dashboard, testing, documentation—and we review each other's work for quality.
   - Our scrum board keeps us focused and transparent: [View Scrum Board](https://github.com/users/Teniolaaaa/projects/1/views/1)

---

## 🚀 Project Overview

MoMo Transaction Analyzer is a collaborative project to process, clean, and analyze Mobile Money (MoMo) SMS/XML data. Our ETL pipeline transforms messy real-world data into a structured database, powering a dashboard for insights and reporting. We value teamwork, clean code, and clear documentation.

---


## 🏗️ System Architecture

**Architecture Diagram:**

![Architecture Diagram](docs/architecture_diagram.png)

*This diagram shows the high-level flow: from raw XML ingestion, through ETL processing, to database storage and dashboard presentation. If the image does not display, ensure docs/architecture_diagram.png is a valid PNG and tracked in git.*

---


## 🗂️ Database Design

**ERD Diagram:**

![ERD Diagram](docs/erd_diagram.png)

*See docs/erd_diagram.png for the full ERD. For design rationale and attribute details, see [docs/erd_design_and_rationale.md](docs/erd_design_and_rationale.md).*  

---

## 🗃️ Project Structure

```text
momo-transaction-analyzer/
│
├── app.py, index.html, requirements.txt
├── etl/                  # ETL pipeline modules
│   ├── parse_xml.py      # XML parser
│   ├── clean_normalize.py
│   ├── categorize.py
│   ├── load_db.py
│   └── run.py
├── data/
│   ├── raw/              # Raw XML samples
│   ├── processed/        # JSON output
│   └── logs/             # ETL logs
├── database/
│   └── database_setup.sql
├── docs/
│   ├── erd_diagram.png
│   ├── architecture_diagram.png
│   ├── erd_design_and_rationale.md
│   ├── Database_Design_Document_EWD14.md
│   └── [AI Usage Log PDF]
├── examples/
│   └── json_schemas.json
├── tests/
└── ...
```

---

## 🧩 JSON Data Modeling

- See [examples/json_schemas.json](examples/json_schemas.json) for entity and complex transaction examples.
- Each JSON object maps to a SQL table, with nested objects for relationships (e.g., sender, receiver, category, logs).
- The file is humanized with realistic names and scenarios.

---


## 🤖 AI Usage Log

See [docs/AI Usage Log - Google Docs2.pdf](docs/AI%20Usage%20Log%20-%20Google%20Docs2.pdf) for a detailed log of AI assistance and code generation.

- End-to-end ETL pipeline: parse, clean, categorize, and load MoMo transactions
- Robust database schema for analytics
- JSON export for dashboard/frontend
- Web dashboard for insights
- Modular, testable Python code
- Team-driven documentation and code reviews

---

## ⚡ How to Run

1. **Clone the repo:**
    ```sh
    git clone https://github.com/Teniolaaaa/momo-transaction-analyzer.git
    cd momo-transaction-analyzer
    ```
2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
3. **Set up the database:**
    - Run the SQL in `database/database_setup.sql` using your SQL client (MySQL/MariaDB/TiDB).
4. **Run the ETL pipeline:**
    ```sh
    python etl/run.py --xml data/raw/sample_momo.xml
    ```
5. **View the dashboard:**
    - Open `index.html` in your browser.

---

## 🧑‍💻 Sample SQL Queries

- **Create:**
   ```sql
   INSERT INTO Users (phone_number, name) VALUES ('+250799999999', 'Sam Test');
   ```
- **Read:**
   ```sql
   SELECT t.transaction_id, t.transaction_code, t.amount, u1.name AS sender, u2.name AS receiver
   FROM Transactions t
   JOIN Users u1 ON t.sender_id = u1.user_id
   LEFT JOIN Users u2 ON t.receiver_id = u2.user_id;
   ```
- **Update:**
   ```sql
   UPDATE Users SET name = 'Samuel Test' WHERE user_id = 6;
   ```
- **Delete:**
   ```sql
   DELETE FROM Transactions WHERE transaction_id = 5;
   ```

---

## 🧪 Testing

- **Unit tests:**
   ```sh
   python -m unittest discover tests
   ```
- **Sample data:** `data/raw/sample_momo.xml`

---


## 📄 Documentation

- **Database Design Doc:** [docs/Database_Design_Document_EWD14.md](docs/Database_Design_Document_EWD14.md)
- **ERD & Architecture Diagrams:** [docs/erd_diagram.png](docs/erd_diagram.png), [docs/architecture_diagram.png](docs/architecture_diagram.png)
- **AI Usage Log:** [docs/AI Usage Log - Google Docs2.pdf](docs/AI%20Usage%20Log%20-%20Google%20Docs2.pdf)
- **Design Rationale:** [docs/erd_design_and_rationale.md](docs/erd_design_and_rationale.md)

---



---

## 📬 Contact

For questions, contact the team lead or open an issue in the repository.

---

> _Built with teamwork, transparency, and a passion for clean engineering. Thank you for reviewing our work!_


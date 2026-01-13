# System Architecture

## Overview
This shows how our MoMo Transaction Analyzer works and how the different parts connect.

## Architecture Diagram

```
USER
 |
 v
+------------------+
|  Web Dashboard   |
|  (Browser)       |
+------------------+
 |
 | Fetches JSON
 v
+------------------+
| dashboard.json   |
+------------------+
 ^
 | Created by
 |
+------------------+
|  ETL Pipeline    |
|  - Parse XML     |
|  - Clean data    |
|  - Categorize    |
|  - Save to DB    |
+------------------+
 ^
 | Reads
 |
+------------------+
| SQLite Database  |
+------------------+
 ^
 | From
 |
+------------------+
|   XML Files      |
+------------------+
```

## How It Works

### 1. Data Input (XML Files)
We get transaction data in XML format. Files are stored in \data/raw/\ folder.

### 2. ETL Pipeline (Python)
The main processing happens here:
- **parse_xml.py** - Reads XML and extracts transaction data
- **clean_normalize.py** - Cleans amounts, fixes dates, formats phone numbers  
- **categorize.py** - Assigns category based on transaction type
- **load_db.py** - Saves to database and exports JSON

Run it: \python etl/run.py --xml data/raw/sample_momo.xml\

### 3. Database (SQLite)
Stores all transactions in \db.sqlite3\ file. One table called \	ransactions\.

### 4. Frontend (HTML/CSS/JS)
Dashboard displays the data:
- index.html - page structure
- styles.css - styling
- chart_handler.js - loads and displays data

## Data Flow
1. Put XML file in data/raw folder
2. Run ETL pipeline
3. ETL processes and saves to database
4. ETL exports summary to JSON
5. Open index.html in browser
6. JavaScript loads JSON and displays transactions

## Tech Stack
**Backend:** Python, SQLite, lxml, dateutil  
**Frontend:** HTML, CSS, JavaScript  
**Tools:** VS Code, Git

## What We Learned
- Working with XML data
- Database operations
- Building ETL pipelines
- Frontend-backend integration
- Git collaboration

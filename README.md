# MoMo Transaction Analyzer

## Team Information
**Team Name:** MoMo Analytics Team

**Team Members:**
- Teniola Adam Olaleye (Group Leader)
- Gael Kamunuga Mparaye
- Kevin Manzi
- Michaella Kamikazi Karangwa
- Rajveer Singh Jolly

## Project Description
An enterprise-level fullstack application designed to process MoMo SMS transaction data in XML format. The system performs ETL operations to clean, categorize, and store transaction data in a relational database, with a frontend dashboard for data analysis and visualization.

## System Architecture
[Architecture Diagram Link - To be added]

## Project Management
**Scrum Board:** [Link to be added]

## Project Structure
```
.
├── README.md                 # Project overview and setup
├── .env.example             # Environment variables template
├── requirements.txt         # Python dependencies
├── index.html              # Dashboard entry point
├── web/                    # Frontend files
├── data/                   # Data storage
├── etl/                    # ETL pipeline
├── api/                    # Backend API (optional)
├── scripts/                # Utility scripts
└── tests/                  # Unit tests
```

## Setup Instructions
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and configure
4. Run ETL pipeline: `python etl/run.py --xml data/raw/momo.xml`
5. Start frontend: `python -m http.server 8000`

## Features
- XML data parsing and validation
- Data cleaning and normalization
- Transaction categorization
- SQLite database storage
- Interactive dashboard with visualizations
- RESTful API (bonus feature)

## Technologies
- **Backend:** Python, SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Data Processing:** lxml/ElementTree, dateutil
- **API:** FastAPI (optional)

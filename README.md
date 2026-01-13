# MoMo Transaction Analyzer

## Team Information
**Team Name:** MoMo Analytics Team

**Team Members:**
- Teniola Adam Olaleye (Group Leader)
- Gael Kamunuga Mparaye
- Kevin Manzi
- Michaella Kamikazi Karangwa
- Rajveer Singh Jolly

## Project Overview
A full-stack application for processing mobile money transaction data from XML format. The system implements an ETL pipeline to extract, transform, and load transaction data into a relational database, with a frontend dashboard for visualization and analysis.

## System Architecture

**Architecture Diagram:** [View on Draw.io](https://drive.google.com/file/d/17G9310r-MtVn4tk-Nj7M_gQCHik2_YOf/view?usp=drive_link)

The system follows a typical ETL architecture:
- **Extract:** Parse XML transaction files
- **Transform:** Clean, normalize, and categorize data
- **Load:** Store in SQLite database
- **Present:** JSON export to web dashboard

## Project Management

**GitHub Projects Board:** [View Scrum Board](https://github.com/users/Teniolaaaa/projects/1/views/1)

**Sprint Documentation:** [View SCRUM.md](SCRUM.md)

Task tracking and sprint management for the development team.

## Project Structure
```
momo-transaction-analyzer/
 README.md                 # Project documentation
 requirements.txt          # Python dependencies
 index.html               # Dashboard entry point
 web/
    styles.css          # Dashboard styling
    chart_handler.js    # Frontend logic
 data/
    raw/                # XML input files
    processed/          # JSON output
    logs/               # ETL logs
    db.sqlite3          # SQLite database
 etl/
    parse_xml.py        # XML parser
    clean_normalize.py  # Data cleaning
    categorize.py       # Transaction categorization
    load_db.py          # Database operations
    run.py             # Main ETL script
    config.py          # Configuration
 tests/
    test_parse_xml.py
    test_clean_normalize.py
 api/
     __init__.py         # API endpoints
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Web browser
- Git

### Installation Steps

**1. Clone the repository**
```bash
git clone https://github.com/Teniolaaaa/momo-transaction-analyzer.git
cd momo-transaction-analyzer
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the ETL pipeline**
```bash
python etl/run.py --xml data/raw/sample_momo.xml
```

**4. View the dashboard**

Simply open `index.html` in your web browser by double-clicking it, or right-click and select "Open with" your preferred browser.

## Features

### ETL Pipeline
- XML transaction parsing and validation
- Data cleaning and normalization
- Automatic transaction categorization
- SQLite database storage
- JSON export for frontend consumption

### Web Dashboard
- Transaction summary cards
- Real-time data display
- Transaction table with filtering
- RWF currency formatting
- Responsive design

### Transaction Categories
- AIRTIME: Mobile credit purchases
- TRANSFER: Money sent or received
- BILL_PAYMENT: Utility payments
- WITHDRAWAL: Cash withdrawals
- OTHER: Uncategorized transactions

## Technology Stack

**Backend:**
- Python 3.13
- SQLite3
- lxml for XML parsing
- python-dateutil for date handling

**Frontend:**
- HTML5
- CSS3
- JavaScript (ES6)

**Development Tools:**
- Git & GitHub
- VS Code
- pytest for testing

## Testing

Run the test suite:
```bash
pytest tests/
```

Tests cover XML parsing and data cleaning functionality.

## Contributing

This is an academic project. For suggestions or improvements:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

## License

Academic project for African Leadership University. All rights reserved.

## Contact

**Project Lead:** Teniola Adam Olaleye
**GitHub:** [@Teniolaaaa](https://github.com/Teniolaaaa)

---

*Last Updated: January 2026*



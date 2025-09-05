#  Data Pipeline Mini Project

This project demonstrates a simple ETL (Extract-Transform-Load) pipeline using **Python** and **MySQL**. It loads third-party event sales data from a CSV file into a MySQL database, then queries and displays the most popular events for a given time window (e.g., **August 2020**).

---

##  Project Structure

Data Pipeline Mini Project/  
├── main.py  
├── connection.py  
├── load_third_party.py  
├── third_party_sales_1.csv  
├── .env ← you'll need to create this  
├── .gitignore ← excludes .env to protect credentials  
├── requirements.txt  
└── README.md  

---

##  Getting Started

###  Prerequisites

- Python 3.8 or newer
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) installed and configured
- MySQL Server running locally
- A MySQL database created (e.g., `event_ticket`)
- `pip` and `git` installed

---

##  Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/data-pipeline-project.git](https://github.com/matthew-bevis/DataPipeline)
cd DataPipeline
```
### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
```
#### On Windows:
```bash
venv\Scripts\activate
```
#### On Mac/Linux:
```bash
source venv/bin/activate
```
### 3. Install Required Packages
```bash
pip install -r requirements.txt
```
Environment Variables (for MySQL Workbench)
You’ll need to create a .env file in the root of the project that contains your MySQL Workbench credentials. This file is not committed to Git — the .gitignore is already set up to protect your secrets.

NOTE: You must manually create this file

Example .env File
```bash
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=event_ticket
```
Replace these values with your actual MySQL Workbench credentials.

Running the Project
With your .env file configured and MySQL server running:

```bash
python main.py
```
This will:

Connect to your MySQL database using credentials from .env

Create a sales table if it doesn’t exist

Load records from third_party_sales_1.csv into the table

Query the top-selling events from August 2020

Print a formatted list of event names

Example Output
```bash
Successfully connected to the MySQL database.
CSV data loaded successfully.

Here are the most popular tickets in August 2020:
- Christmas Spectacular
- The North American International Auto Show
- Washington Spirits vs Sky Blue FC
```

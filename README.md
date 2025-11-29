# network-dashboard

A simple Python-based network traffic dashboard.  
This project reads a CSV file that contains network traffic metrics and prints a small summary report to the terminal.

It was implemented as a mini project to demonstrate basic monitoring and reporting logic for network automation use cases.

---

## Features

- Reads network traffic data from a CSV file  
- Calculates total and average incoming/outgoing traffic  
- Counts total error events  
- Finds peak traffic times (max in/out)  
- Prints a clear, text-based summary report  

---

## Project Structure

network-dashboard/  
│  
├── dashboard.py      # Main script that parses the CSV and prints the report  
├── network_data.csv  # Sample network traffic data  
└── README.md         # Project documentation  

---

## How It Works

1. `dashboard.py` opens `network_data.csv`.  
2. Each row contains:  
   - `timestamp`  
   - `traffic_in` (bytes)  
   - `traffic_out` (bytes)  
   - `errors` (count)  
3. The script loops over all rows and:  
   - Sums incoming and outgoing traffic  
   - Computes averages  
   - Sums all errors  
   - Tracks the maximum `traffic_in` and `traffic_out` values and their timestamps  
4. Finally, a formatted report is printed to the terminal.

This simulates a very lightweight network monitoring dashboard that could be extended with alerts, graphs or real-time data.

---

## Running the Project

No external dependencies are required (only Python standard library).

From the project folder:

```bash
python3 dashboard.py

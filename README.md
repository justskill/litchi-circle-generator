# Litchi Circle Generator

This Python script allows users to generate circular waypoints around a central GPS coordinate and save them to a CSV file. The waypoints are calculated using the haversine formula and include altitude, heading, curve size, and other parameters suitable for various drone or mapping applications.

## Features
- **Haversine Formula**: Accurate distance calculation between GPS coordinates.
- **Circular Waypoints**: Generate evenly spaced waypoints in a circular pattern around a specified center.
- **Customizable Parameters**: Specify radius, altitude, and number of waypoints.
- **CSV Export**: Save waypoints to a CSV file with detailed attributes.

## Requirements
- Python 3.x
- `tkinter` for GUI
- `math` and `csv` modules (standard libraries)

## Installation
1. Clone the repository or download the script file.
2. Ensure Python 3.x is installed on your system.
3. Install any missing dependencies (all required modules are part of Python's standard library).

## Usage
1. Run the script:
   ```bash
   python main.py

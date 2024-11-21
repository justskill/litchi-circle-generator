import tkinter as tk
from tkinter import filedialog, messagebox
import math
import csv

def haversine_distance(lon1, lat1, lon2, lat2):
    # Calculate the great-circle distance between two points on the Earth's surface
    R = 6378137  # Earth radius in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi/2) * math.sin(delta_phi/2) + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

def generate_circle_waypoints(center_lat, center_lon, radius, altitude, num_waypoints):
    waypoints = []
    angle_increment = 2 * math.pi / num_waypoints
    curvesize = radius * math.sin(angle_increment / 2)
    
    for i in range(num_waypoints + 2):  # Add two extra waypoints
        angle = i * angle_increment  # Calculate angle between each waypoint
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        
        # Convert dx, dy from meters to decimal degrees (approximate)
        latitude = center_lat + (180 / math.pi) * (dy / 6378137)
        longitude = center_lon + (180 / math.pi) * (dx / 6378137) / math.cos(center_lat * math.pi/180)
        
        # Append waypoint in CSV format
        waypoints.append([
            latitude, longitude, altitude, 0, curvesize, 0, 1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 
            -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 0, center_lat, center_lon, 1, 0, -1, -1
        ])
    
    return waypoints

def save_waypoints_to_csv(filename, waypoints):
    # Define the header for the CSV file
    header = [
        "latitude", "longitude", "altitude(m)", "heading(deg)", "curvesize(m)", "rotationdir", "gimbalmode", 
        "gimbalpitchangle", "actiontype1", "actionparam1", "actiontype2", "actionparam2", "actiontype3", 
        "actionparam3", "actiontype4", "actionparam4", "actiontype5", "actionparam5", "actiontype6", 
        "actionparam6", "actiontype7", "actionparam7", "actiontype8", "actionparam8", "actiontype9", 
        "actionparam9", "actiontype10", "actionparam10", "actiontype11", "actionparam11", "actiontype12", 
        "actionparam12", "actiontype13", "actionparam13", "actiontype14", "actionparam14", "actiontype15", 
        "actionparam15", "altitudemode", "speed(m/s)", "poi_latitude", "poi_longitude", "poi_altitude(m)", 
        "poi_altitudemode", "photo_timeinterval", "photo_distinterval"
    ]

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(waypoints)

def generate_and_save():
    try:
        center_latitude = float(center_latitude_entry.get())
        center_longitude = float(center_longitude_entry.get())
        radius = float(radius_entry.get())
        altitude = float(altitude_entry.get())
        num_waypoints = int(num_waypoints_entry.get())
        
        waypoints = generate_circle_waypoints(center_latitude, center_longitude, radius, altitude, num_waypoints)
        
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            save_waypoints_to_csv(filename, waypoints)
            messagebox.showinfo("Success", "Waypoints have been generated and saved to CSV file.")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main window
root = tk.Tk()
root.title("Waypoint Generator")

# Create and place the labels and entry widgets
tk.Label(root, text="Center Latitude:").grid(row=0, column=0, padx=10, pady=5)
center_latitude_entry = tk.Entry(root)
center_latitude_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Center Longitude:").grid(row=1, column=0, padx=10, pady=5)
center_longitude_entry = tk.Entry(root)
center_longitude_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Radius (meters):").grid(row=2, column=0, padx=10, pady=5)
radius_entry = tk.Entry(root)
radius_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Altitude (meters):").grid(row=3, column=0, padx=10, pady=5)
altitude_entry = tk.Entry(root)
altitude_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Number of Waypoints:").grid(row=4, column=0, padx=10, pady=5)
num_waypoints_entry = tk.Entry(root)
num_waypoints_entry.grid(row=4, column=1, padx=10, pady=5)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate and Save", command=generate_and_save)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()

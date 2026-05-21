import pypsa
import pandas as pd
import matplotlib.pyplot as plt

# Έλεγχος για Cartopy
try:
    import cartopy.crs as ccrs
    has_cartopy = True
except ImportError:
    has_cartopy = False

n = pypsa.Network()

# Δεδομένα μονάδων
greece_data = {
    'name': ['Agios Dimitrios', 'Ptolemaida V', 'Megalopoli IV', 'Alivery 5', 'Megalopoli V', 'Thisvi', 'Aliveri CCGT'],
    'carrier': ['Lignite', 'Lignite', 'Lignite', 'Natural Gas', 'Natural Gas', 'Natural Gas', 'Natural Gas'],
    'p_nom': [1200, 660, 300, 420, 811, 420, 420],
    'x': [21.92, 21.72, 22.11, 23.51, 22.11, 23.15, 23.51],
    'y': [40.39, 40.48, 37.41, 38.39, 37.41, 38.25, 38.39]
}
df_gr = pd.DataFrame(greece_data)

# Προσθήκη Carriers με χρώματα
n.add("Carrier", "Lignite", color="brown")
n.add("Carrier", "Natural Gas", color="blue")

# Δημιουργία Buses και Generators
for i, row in df_gr.iterrows():
    bus_name = f"Bus {row['name']}"
    n.add("Bus", bus_name, x=row['x'], y=row['y'])
    n.add("Generator", row['name'], bus=bus_name, p_nom=row['p_nom'], carrier=row['carrier'])

# ΠΡΟΕΤΟΙΜΑΣΙΑ ΧΡΩΜΑΤΩΝ ΓΙΑ ΤΑ BUSES
# Φτιάχνουμε μια σειρά που αντιστοιχίζει κάθε Bus στο χρώμα του Carrier του
# Χρησιμοποιούμε .astype(str) για να αποφύγουμε το σφάλμα StringDtype
# 1. Υπολογισμός χρωμάτων και μετατροπή σε απλό λεξικό (Dictionary)
# ώστε να μην υπάρχει ίχνος από Pandas Series στο plot
bus_colors_dict = n.generators.set_index("bus").carrier.map(n.carriers.color).to_dict()

# 2. Μετατροπή σε Series, αλλά αναγκάζουμε το dtype να είναι το παλιό 'object' (numpy string)
bus_colors = pd.Series(bus_colors_dict).astype(object)

# Σχεδίαση
fig, ax = plt.subplots(figsize=(10, 10), 
                       subplot_kw={'projection': ccrs.PlateCarree()} if has_cartopy else None)

n.plot(
    ax=ax, 
    geomap=has_cartopy, 
    bus_sizes=0.015,
    bus_colors=bus_colors # Τώρα είναι σε μορφή object που το NumPy δέχεται
)

if has_cartopy:
    ax.coastlines(resolution='10m')
    ax.set_extent([19, 27, 34, 42])
    plt.title("Μονάδες Παραγωγής Ελλάδας (PyPSA)")
else:
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.title("Πλάνο Μονάδων (Lon/Lat Grid)")

plt.show()
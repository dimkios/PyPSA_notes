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

# 1. Ορισμός Δεδομένων
greece_data = {
    'name': ['Agios Dimitrios', 'Ptolemaida V', 'Megalopoli IV', 'Alivery 5', 'Megalopoli V', 'Thisvi', 'Aliveri CCGT'],
    'carrier': ['Lignite', 'Lignite', 'Lignite', 'Natural Gas', 'Natural Gas', 'Natural Gas', 'Natural Gas'],
    'p_nom': [1200, 660, 300, 420, 811, 420, 420],
    'x': [21.92, 21.72, 22.11, 23.51, 22.11, 23.15, 23.51],
    'y': [40.39, 40.48, 37.41, 38.39, 37.41, 38.25, 38.39]
}
df_gr = pd.DataFrame(greece_data)

# 2. Προσθήκη Carriers
n.add("Carrier", "Lignite", color="brown")
n.add("Carrier", "Natural Gas", color="blue")

# 3. Προσθήκη Buses, Generators και Loads
for i, row in df_gr.iterrows():
    bus_name = f"Bus {row['name']}"
    n.add("Bus", bus_name, x=row['x'], y=row['y'])
    
    # Προσθήκη Γεννήτριας
    n.add("Generator", row['name'], bus=bus_name, p_nom=row['p_nom'], carrier=row['carrier'])
    
    # Προσθήκη ενός τυχαίου Φορτίου (Load) σε κάθε κόμβο για την επίδειξη
    n.add("Load", f"Load {row['name']}", bus=bus_name, p_set=row['p_nom'] * 0.6)

# --- ΕΚΤΥΠΩΣΕΙΣ ΣΤΟ ΤΕΡΜΑΤΙΚΟ ---

print("\n" + "="*50)
print("ΣΤΑΤΙΣΤΙΚΑ ΜΟΝΑΔΩΝ ΠΑΡΑΓΩΓΗΣ (Generators)")
print("="*50)
# Εκτύπωση επιλεγμένων στηλών για καθαρότητα
print(n.generators[['bus', 'carrier', 'p_nom']])

print("\n" + "="*50)
print("ΣΤΑΤΙΣΤΙΚΑ ΦΟΡΤΙΩΝ (Loads)")
print("="*50)
print(n.loads[['bus', 'p_set']])

# Συνολική ισχύς ανά καύσιμο
summary = n.generators.groupby("carrier").p_nom.sum()
print("\n" + "="*50)
print("ΣΥΝΟΛΙΚΗ ΙΣΧΥΣ ΑΝΑ ΚΑΥΣΙΜΟ (MW)")
print("="*50)
print(summary)

# --- ΟΠΤΙΚΟΠΟΙΗΣΗ ---

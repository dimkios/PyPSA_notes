import pypsa

# 1. Δημιουργία Δικτύου
n = pypsa.Network()

# 2. Προσθήκη Bus (Κόμβων)
n.add("Bus", "Bus Αθήνα", v_nom=400) # 400kV
n.add("Bus", "Bus Θεσσαλονίκη", v_nom=400)

# 3. Προσθήκη Γραμμής (Transmission Line)
n.add("Line", "Γραμμή 1", 
      bus0="Bus Αθήνα", 
      bus1="Bus Θεσσαλονίκη", 
      r=0.01, x=0.1) # Αντίσταση και Αντίδραση

# 4. Προσθήκη Γεννήτριας και Φορτίου
n.add("Generator", "Γεννήτρια", bus="Bus Αθήνα", p_set=500)
n.add("Load", "Φορτίο", bus="Bus Θεσσαλονίκη", p_set=450)

# 5. ΕΚΤΕΛΕΣΗ (Εδώ εμφανίζεται το μήνυμα που πόσταρες)
n.pf()

print(n.lines_t.p0)

print(n.buses_t.v_mag_pu)

print(n.generators_t.p)
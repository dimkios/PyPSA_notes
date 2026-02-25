import pypsa

#Νέο Δίκτυο (Δήλωση)
net = pypsa.Network()

#Προσθέτουμε 2 Ζυγούς υψηλής τάσης 
net.add("Bus", "Bus A", v_nom=220)
net.add("Bus", "Bus B", v_nom=220)

#Συνδέουμε τους Ζυγούς μέσω γραμμής μεταφοράς
net.add("Line", "Line 1",
        bus0 = "Bus A",
        bus1 = "Bus B",
        length = 50,
        x=0.1,
        r=0.01,
        s_nom = 100)

#Προσθέτουμε μια γεννήτρια (Η/Ζ) στο ΖΥΓΟ Α
net.add("Generator", "Generator A",
        bus="Bus A",
        p_nom = 80,
        marginal_cost=50)

#Προσθέτουμε ένα φορτίο στο ΖΥΓΟ Β
net.add("Load", "Load A",
        bus="Bus B",
        p_set = 70)

#Τρέξε βασική ανάλυση ροής ρεύματος
net.pf()

print(net.lines_t.p0)

print(net.buses_t.v_mag_pu)

print(net.generators_t.p)
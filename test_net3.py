import pypsa

n = pypsa.Network()
n.add("Bus", "Αθήνα", v_nom=400)
n.add("Bus", "Θεσσαλονίκη", v_nom=400)
n.add("Line", "Γραμμή 1", bus0="Αθήνα", bus1="Θεσσαλονίκη", r=2, x=10)
n.add("Generator", "ΔΕΗ", bus="Αθήνα", p_set=100, control="PQ")
n.add("Load", "Πόλη", bus="Θεσσαλονίκη", p_set=90)

# Εκτέλεση
n.pf()

print("\n--- ΑΠΟΤΕΛΕΣΜΑΤΑ ΡΟΗΣ ΙΣΧΥΟΣ ---")
print(f"Ροή από Αθήνα προς Θεσσαλονίκη: {n.lines_t.p0.iloc[0,0]:.2f} MW")
print(f"Απώλειες στη γραμμή: {n.lines_t.p0.iloc[0,0] - abs(n.lines_t.p1.iloc[0,0]):.2f} MW")
print(f"Τάση στη Θεσσαλονίκη: {n.buses_t.v_mag_pu.iloc[0,1]:.4f} p.u.")
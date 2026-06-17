| Κατηγορία (Category) | Παράμετρος / Μεταβλητή (Parameter/Variable) | Σύμβαση Μονάδας (Unit Convention) |
| :--- | :--- | :--- |
| **Ισχύς και Ενέργεια**<br>*(Power and Energy)* | `Pnom`, `Pmax`, `p`, `pnom_opt` | MW |
| | `Enom`, `e_t` (ενέργεια αποθήκευσης) | MWh |
| | `Pmin_pu`, `Pmax_pu` | Ανά μονάδα / Per unit (0–1) |
| | `snom`, `snom_opt` (χωρητικότητα γραμμής/συνδέσμου) | MVA |
| | Κατανομή Γεννήτριας/Αποθήκευσης (Generator/Storage dispatch) | MW |
| | Κατανάλωση Ενέργειας (Energy consumption) | MWh |
| **Παράμετροι Κόστους**<br>*(Cost Parameters)* | Κεφαλαιουχικό κόστος (Capital cost) | €/MW ή €/MWh/έτος (ανάλογα με το πλαίσιο) |
| | Οριακό κόστος (Marginal cost) | €/MWh |
| | Κόστος επένδυσης π.χ. αποθήκευση, σύνδεσμοι (Investment costs) | €/MW ή €/MWh |
| | Κόστος εκπομπών, αν μοντελοποιείται (Emissions cost) | €/tCO2 |
| **Εκπομπές και Απόδοση**<br>*(Emissions and Efficiency)*| Εκπομπές CO2 (CO2 emissions) | tCO2/MWh |
| | Ειδικές εκπομπές ανά γεννήτρια (Specific emissions) | tCO2 |
| | Απόδοση γεννητριών, συνδέσμων (Efficiency) | Χωρίς μονάδα / Unitless (0–1) |
| | Μερίδιο ΑΠΕ / Στόχοι RES (Renewable share / RES targets) | Χωρίς μονάδα / Unitless (0–1) |
| **Ηλεκτρικές Παράμετροι**<br>*(Electrical Parameters)*| `vnom` (ονομαστική τάση) | kV |
| | `x`, `r`, `b` (παράμετροι γραμμής) | Ohm |
| | Γωνίες τάσης θ_n,t (Voltage angles) | Ακτίνια ή μοίρες (το PyPSA χρησιμοποιεί εσωτερικά radians) |
| | Συχνότητα, όπου εφαρμόζεται (Frequency) | Hz |
| **Χρόνος και Διάρκεια**<br>*(Time and Duration)*| Διάρκεια Snapshot - έμμεση (Snapshot duration) | Ώρες (Hours) |
| | Ανάλυση χρονοσειρών (Time series resolution) | Συνήθως ωριαία, ορίζεται από τον χρήστη |
| **Γεωγραφικά Δεδομένα**<br>*(Geographic)* | `x`, `y` (συντεταγμένες κόμβων/buses) | Γεωγραφικό Μήκος, Πλάτος / Longitude, Latitude (μοίρες) |
| | Αποστάσεις π.χ. μήκος συνδέσμου (Distances) | km |
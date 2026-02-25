# def main():
#     print("Hello from pypsa-project!")


# if __name__ == "__main__":
#     main()


import pypsa

n = pypsa.Network()

# required snapshot
n.set_snapshots([0])

# define carrier
n.add("Carrier", "electricity")

# bus with carrier
n.add("Bus", "b", carrier="electricity")

# generator WITH cost
n.add(
    "Generator",
    "g",
    bus="b",
    p_nom=100,
    marginal_cost=10  # <-- critical
)

# load
n.add(
    "Load",
    "l",
    bus="b",
    p_set=50
)

n.optimize(solver_name="highs")

print(n.generators_t.p)

m = n.optimize.create_model()
print(m)

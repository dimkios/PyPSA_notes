### Table B.1: Generator component attributes in PyPSA

| Attribute | Type | Unit | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | string | – | – | Unique identifier for the generator. |
| `bus` | string | – | – | Bus to which the generator is connected. |
| `p_nom` | float | MW | required | Nominal power capacity. |
| `p_nom_min` | float | MW | 0 | Minimum allowed capacity during optimization. |
| `p_nom_max` | float | MW | – | Maximum allowed capacity during optimization. |
| `p_nom_extendable` | bool | – | False | Allows capacity expansion if set true. |
| `p_max_pu` | float/series | per unit | 1.0 | Max dispatch as fraction of capacity. |
| `p_min_pu` | float/series | per unit | 0.0 | Min dispatch as fraction of capacity. |
| `p_set` | float/series | MW | – | Fixed-power dispatch (overrides optimization). |
| `marginal_cost` | float | €/MWh | 0.0 | Cost of producing electricity. |
| `capital_cost` | float | €/MW | – | Annualized capital cost if expandable. |
| `efficiency` | float | – | 1.0 | Conversion efficiency. |
| `carrier` | string | – | – | Fuel/technology type (e.g., wind, gas). |
| `committable` | bool | – | False | Enables unit commitment behavior. |
| `ramp_limit_up` | float | per unit / h | – | Max increase per timestep. |
| `ramp_limit_down` | float | per unit / h | – | Max decrease per timestep. |
| `start_up_cost` | float | € | 0.0 | Cost of starting the unit. |
| `shut_down_cost` | float | € | 0.0 | Cost of shutting down the unit. |
| `min_up_time` | int | hours | – | Min time generator must remain on. |
| `min_down_time` | int | hours | – | Min time generator must remain off. |
| `build_year` | int | year | – | Commissioning year. |
| `lifetime` | int | years | – | Expected operating lifetime. |

### Table B.2: Storage-unit component attributes in PyPSA

| Attribute | Type | Unit | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | string | – | – | Unique identifier for the storage unit. |
| `bus` | string | – | – | The bus where the storage unit is connected. |
| `p_nom` | float | MW | required | Nominal power capacity. |
| `p_nom_extendable` | bool | – | False | Flag to allow capacity expansion. |
| `capital_cost` | float | €/MW | – | Annualized investment cost for power capacity. |
| `efficiency_store` | float | – | 1.0 | Efficiency of charging process. |
| `efficiency_dispatch` | float | – | 1.0 | Efficiency of discharging process. |
| `standing_loss` | float | per unit / h | 0.0 | Fractional loss of stored energy per hour. |
| `max_hours` | float | h | – | Maximum duration of full-power discharge (Enom/Pnom). |
| `state_of_charge_initial` | float | MWh | 0.0 | Initial energy stored at simulation start. |
| `cyclic_state_of_charge` | bool | – | False | Enforces same SoC at beginning and end if true. |
| `carrier` | string | – | – | Type of storage technology (e.g., battery, hydrogen). |
| `marginal_cost` | float | €/MWh | 0.0 | Operational cost per unit of dispatched energy. |
| `build_year` | int | year | – | Year of commissioning. |
| `lifetime` | int | years | – | Expected operational lifetime. |

### Table B.3: Store component attributes in PyPSA

| Attribute | Type | Unit | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | string | – | – | Unique identifier for the store. |
| `bus` | string | – | – | Bus to which the store is connected. |
| `e_nom` | float | MWh | required | Nominal energy storage capacity. |
| `e_nom_extendable` | bool | – | False | Allows optimization of energy-storage capacity. |
| `capital_cost` | float | €/MWh | – | Annualized cost of installing energy capacity. |
| `marginal_cost` | float | €/MWh | 0.0 | Operational cost per unit of energy used. |
| `carrier` | string | – | – | Type of storage medium (e.g., hydrogen, thermal). |
| `standing_loss` | float | per unit / h | 0.0 | Fractional energy loss over time. |
| `e_initial` | float | MWh | 0.0 | Initial stored energy at simulation start. |
| `cyclic_state_of_charge` | bool | – | False | Enforces cyclic state-of-charge over the time horizon. |
| `build_year` | int | year | – | Year the storage unit was added. |
| `lifetime` | int | years | – | Expected operational lifetime. |

### Table B.4: Load component attributes in PyPSA

| Attribute | Type | Unit | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | string | – | – | Unique identifier for the load. |
| `bus` | string | – | – | Bus where the load is connected. |
| `p_set` | float / time series | MW | required | Fixed-power demand over time. |
| `q_set` | float / time series | MVar | 0.0 | Optional reactive power demand. |
| `scaling` | float | – | 1.0 | Scales the time series of p_set (and q_set if defined). |
| `carrier` | string | – | – | Category of consumption (e.g., electricity, heat). |
| `build_year` | int | year | – | Year the load was added to the system. |
| `lifetime` | int | years | – | Duration for which the load is active in the model. |

### Table B.5: Bus component attributes in PyPSA

| Attribute | Type | Unit | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | string | – | – | Unique identifier for the bus. |
| `carrier` | string | – | – | Type of energy vector (e.g., electricity, heat, hydrogen). |
| `x` | float | degrees or km | 0.0 | X-coordinate for plotting or spatial analysis. |
| `y` | float | degrees or km | 0.0 | Y-coordinate for plotting or spatial analysis. |
| `v_nom` | float | kV | 1.0 | Nominal voltage level. |
| `sub_network` | int | – | 0 | Defines network partitioning for multi-subnetwork analysis. |
| `control_area` | string | – | – | Optional field to group buses by balancing area or region. |
| `build_year` | int | year | – | Commissioning year of the bus (for scenario evolution). |
| `lifetime` | int | years | – | Operational duration considered in the model. |

### Table B.6: Link component attributes in PyPSA

| Attribute | Type | Unit | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | string | – | – | Unique identifier for the link. |
| `bus0` | string | – | – | Input/source bus of the link. |
| `bus1` | string | – | – | Output/target bus of the link. |
| `p_nom` | float | MW | required | Nominal power transfer capacity. |
| `p_nom_extendable` | bool | – | False | Allows optimization of transfer capacity. |
| `efficiency` | float | – | 1.0 | Conversion efficiency from input to output. |
| `efficiency2` | float | – | 1.0 | Efficiency to second output bus (if defined). |
| `bus2` | string | – | – | Optional second output bus (e.g., for CHP or split flows). |
| `p_set` | float / time series | MW | – | Fixed dispatch if specified, overrides optimization. |
| `marginal_cost` | float | €/MWh | 0.0 | Operational cost per unit transferred. |
| `capital_cost` | float | €/MW | – | Annualized capital cost for the link. |
| `build_year` | int | year | – | Commissioning year of the link. |
| `lifetime` | int | years | – | Duration for which the link remains operational. |

### Table B.7: Line component attributes in PyPSA

| Attribute | Type | Unit | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | string | – | – | Unique identifier for the transmission line. |
| `bus0` | string | – | – | Sending end bus of the line. |
| `bus1` | string | – | – | Receiving end bus of the line. |
| `r` | float | ohm | required | Series resistance of the line. |
| `x` | float | ohm | required | Series reactance of the line. |
| `b` | float | Siemens | 0.0 | Line charging susceptance (optional). |
| `s_nom` | float | MVA | required | Nominal apparent power capacity. |
| `s_nom_extendable` | bool | – | False | Allows capacity optimization. |
| `length` | float | km | 1.0 | Physical length of the line. Used to scale ‘r’, ‘x’, ‘b’. |
| `capital_cost` | float | €/MW | – | Investment cost if expansion is enabled. |
| `marginal_cost` | float | €/MWh | 0.0 | Operating cost per unit of transmitted power. |
| `num_parallel` | int | – | 1 | Number of identical lines in parallel. |
| `build_year` | int | year | – | Year the line was constructed. |
| `lifetime` | int | years | – | Expected operational lifetime. |


# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in US dollars.

| Parameter | Type | Description |
|-----------|------|-------------|
| `weight_kg` | `float` | Parcel weight; must be positive. |
| `zone` | `str` | `"local"` or `"regional"`. |
| `service` | `str` | `"standard"` (default) or `"express"`. Express adds a $7 surcharge. |

**Examples (Python):**

```python
from warehouse.rates import shipping_quote

shipping_quote(2, "local")                      # -> 8.0  (standard)
shipping_quote(2, "local", service="express")   # -> 15.0 (express)
shipping_quote(2, "regional")                   # -> 11.0 (standard)
shipping_quote(2, "regional", service="express")# -> 18.0 (express)
```

**CLI usage:**

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

```
$ python -m warehouse.cli 2 local
$8.00

$ python -m warehouse.cli 2 local --service express
$15.00
```

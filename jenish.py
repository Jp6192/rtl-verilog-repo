import cocotb, pkgutil, importlib.util
print("cocotb path:", list(cocotb.__path__))
print("subpackages:", sorted([m.name for m in pkgutil.iter_modules(cocotb.__path__)]))
print("runner spec:", importlib.util.find_spec("cocotb.runner"))
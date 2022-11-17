from .param_priority import reorder_items

def pytest_collection_modifyitems(items):
    # separate parametrized setups
    items[:] = reorder_items(items)


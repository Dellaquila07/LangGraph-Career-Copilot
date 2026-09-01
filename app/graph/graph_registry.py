_registry = {"graph": None}

def set_graph(graph):
    _registry["graph"] = graph

def get_graph():
    if _registry["graph"] is None:
        raise RuntimeError("The graph has not yet been compiled/registered.")
    return _registry["graph"]

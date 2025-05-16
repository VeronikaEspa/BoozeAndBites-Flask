from resolvers.queries import Query

def test_query_productos(monkeypatch):
    dummy_data = [
        {"id": 1, "nombre": "Test", "precio": 1.0, "stock": 5, "disponible": True, "img": ""}
    ]

    monkeypatch.setattr("resolvers.queries.products_db", dummy_data)

    query = Query()
    productos = query.resolve_productos(None)
    assert len(productos) == 1
    assert productos[0]["nombre"] == "Test"
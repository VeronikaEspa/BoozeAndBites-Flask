from resolvers.mutations import ModificarStock

# Test 1: Incremento de stock normal, sin cambio en disponibilidad
def test_modificar_stock_incremento_sin_cambio_de_estado(monkeypatch):
    db = [{"id": 1, "nombre": "Activo", "precio": 1.0, "stock": 3, "disponible": True, "img": ""}]
    monkeypatch.setattr("resolvers.mutations.products_db", db)

    mutations = ModificarStock()
    result = mutations.mutate(None, id=1, cantidad=2)
    assert result.producto["stock"] == 5
    assert result.producto["disponible"] is True

# Test 2: Aumenta stock desde 0, este debe poner disponible en True
def test_modificar_stock_desde_cero_activa_disponible(monkeypatch):
    db = [{"id": 1, "nombre": "Test", "precio": 1.0, "stock": 0, "disponible": False, "img": ""}]
    monkeypatch.setattr("resolvers.mutations.products_db", db)

    mutations = ModificarStock()
    result = mutations.mutate(None, id=1, cantidad=5)
    assert result.producto["stock"] == 5
    assert result.producto["disponible"] is True

# Test 3: Resta stock hasta agotar, este debe poner disponible en False
def test_modificar_stock_hasta_agotar(monkeypatch):
    db = [{"id": 1, "nombre": "Test", "precio": 1.0, "stock": 3, "disponible": True, "img": ""}]
    monkeypatch.setattr("resolvers.mutations.products_db", db)

    mutations = ModificarStock()
    result = mutations.mutate(None, id=1, cantidad=-3)
    assert result.producto["stock"] == 0
    assert result.producto["disponible"] is False

# Test 4: Intento de reducir más allá de 0, el stock se queda en 0 y disponible en False
def test_modificar_stock_no_negativo(monkeypatch):
    db = [{"id": 1, "nombre": "Test", "precio": 1.0, "stock": 1, "disponible": True, "img": ""}]
    monkeypatch.setattr("resolvers.mutations.products_db", db)

    mutations = ModificarStock()
    result = mutations.mutate(None, id=1, cantidad=-5)
    assert result.producto["stock"] == 0
    assert result.producto["disponible"] is False
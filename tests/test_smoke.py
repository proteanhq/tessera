"""Smoke tests: the scaffold imports and the cx command surface is registered."""


def test_cx_app_imports():
    from cx.cli import app

    assert app is not None


def test_all_contexts_import():
    import importlib

    contexts = [
        "shared",
        "ledger",
        "accounts",
        "payments",
        "cards",
        "fraud",
        "compliance",
        "reporting",
        "notifications",
        "insights",
    ]
    for name in contexts:
        assert importlib.import_module(f"src.{name}") is not None

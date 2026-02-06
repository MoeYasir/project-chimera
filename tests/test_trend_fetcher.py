def test_trend_contract_exists():
    """
    Failing-by-design test to define the Trend contract slot.
    """
    from chimera.schemas import TREND_SCHEMA  # noqa: F401

    assert isinstance(TREND_SCHEMA, dict)
    assert TREND_SCHEMA.get("type") == "object"
    assert "required" in TREND_SCHEMA

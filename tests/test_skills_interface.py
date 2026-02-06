def test_skill_entrypoints_exist():
    """
    These imports should fail until skills are implemented.
    This defines the empty slot for the agent swarm.
    """
    from chimera.skills.trend_fetcher import handler as trend_handler  # noqa: F401
    from chimera.skills.content_generator import handler as gen_handler  # noqa: F401
    from chimera.skills.social_publisher import handler as pub_handler  # noqa: F401

    assert callable(trend_handler)
    assert callable(gen_handler)
    assert callable(pub_handler)

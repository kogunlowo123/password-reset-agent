"""Test configuration for Password Reset Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "password-reset-agent", "category": "IT Operations"}

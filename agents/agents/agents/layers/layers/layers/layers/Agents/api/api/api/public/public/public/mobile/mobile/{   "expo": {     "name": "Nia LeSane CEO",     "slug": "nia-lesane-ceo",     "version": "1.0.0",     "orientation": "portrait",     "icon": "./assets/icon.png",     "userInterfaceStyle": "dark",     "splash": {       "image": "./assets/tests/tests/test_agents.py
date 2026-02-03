import pytest
from agents.nia import NiaAgent

def test_nia():
    agent = NiaAgent()
    governed = agent.govern("Test plan")
    assert "governed" in governed

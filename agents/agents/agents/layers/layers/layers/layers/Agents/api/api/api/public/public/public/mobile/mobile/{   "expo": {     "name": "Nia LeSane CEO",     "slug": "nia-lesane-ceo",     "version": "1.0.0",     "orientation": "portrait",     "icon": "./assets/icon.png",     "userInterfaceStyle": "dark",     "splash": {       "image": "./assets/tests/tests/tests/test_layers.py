import pytest
from layers.planning import PlanningLayer

def test_planning():
    layer = PlanningLayer()
    plan = layer.decompose("Test")
    assert "steps" in plan.lower()

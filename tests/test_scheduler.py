import pytest
from src.scheduler import ContainerScheduler

@pytest.fixture
def scheduler():
    return ContainerScheduler()

def test_add_container(scheduler):
    scheduler.add_container("test", cpu=1, memory=2)
    assert len(scheduler.pending_containers) == 1

def test_schedule_containers(scheduler):
    scheduler.add_container("high_prio", priority=2)
    scheduler.add_container("low_prio", priority=1)
    scheduler.schedule()
    assert len(scheduler.containers) == 2

def test_resource_limits(scheduler):
    scheduler.add_container("big", cpu=5, memory=20)
    scheduler.schedule()
    assert len(scheduler.containers) == 0

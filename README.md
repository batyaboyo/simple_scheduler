# Container Resource Scheduler

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![Docker Build](https://img.shields.io/badge/docker%20build-passing-success)]()

A container resource scheduler with priority-based scheduling and Docker support.

## Features

- Priority-based container scheduling
- Resource limits enforcement
- Docker containerization
- Comprehensive logging
- Unit testing

## Installation

### Local Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Docker Setup
```bash
docker-compose build
docker-compose up
```

## Usage

```python
from src.scheduler import ContainerScheduler

scheduler = ContainerScheduler()

# Add containers with priority
scheduler.add_container("critical", cpu=2, memory=4, priority=3)
scheduler.add_container("background", cpu=1, memory=1, priority=1)

# Schedule containers
scheduler.schedule()
```

## API Documentation

| Method | Parameters | Description |
|--------|------------|-------------|
| `add_container` | name, cpu, memory, priority | Add container to pending queue |
| `schedule` | - | Allocate resources to containers |
| `get_usage` | - | Get current resource statistics |

## Development

```bash
# Run tests
docker-compose run scheduler pytest tests/

# Debug mode
docker-compose run --env LOG_LEVEL=DEBUG scheduler
```

## Architecture

![System Diagram](docs/design.md)

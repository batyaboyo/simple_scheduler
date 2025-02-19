import os
import logging
import heapq

class ContainerScheduler:
    def __init__(self):
        self.total_cpu = int(os.getenv('TOTAL_CPU', 4))
        self.total_memory = int(os.getenv('TOTAL_MEMORY', 16))
        self.containers = {}
        self.pending_containers = []
        self.resource_usage = {'cpu': 0, 'memory': 0}
        self.logger = logging.getLogger(__name__)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def add_container(self, name, cpu=1, memory=2, priority=0):
        if name in self.containers:
            raise ValueError(f"Container {name} already exists")
        
        heapq.heappush(self.pending_containers, (
            -priority,  # Negative for max-heap behavior
            len(self.pending_containers),  # FIFO for same priority
            {
                'name': name,
                'cpu': cpu,
                'memory': memory
            }
        ))
        self.logger.info(f"Added container {name} (CPU: {cpu}, Memory: {memory})")

    def schedule(self):
        temp_pending = []
        while self.pending_containers:
            priority, _, container = heapq.heappop(self.pending_containers)
            if self._can_allocate(container):
                self._allocate(container)
            else:
                temp_pending.append((priority, container))
        
        # Re-add containers that couldn't be scheduled
        for priority, container in temp_pending:
            heapq.heappush(self.pending_containers, (priority, container))

    def _can_allocate(self, container):
        return (
            self.resource_usage['cpu'] + container['cpu'] <= self.total_cpu and
            self.resource_usage['memory'] + container['memory'] <= self.total_memory
        )

    def _allocate(self, container):
        self.containers[container['name']] = container
        self.resource_usage['cpu'] += container['cpu']
        self.resource_usage['memory'] += container['memory']
        self.logger.info(f"Allocated resources for {container['name']}")

    # Rest of the methods from previous implementation...

if __name__ == "__main__":
    scheduler = ContainerScheduler()
    scheduler.add_container("web", cpu=2, memory=4, priority=1)
    scheduler.add_container("db", cpu=1, memory=8, priority=2)
    scheduler.schedule()

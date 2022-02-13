class IEngine:

    def spawn(self, fn: Callable, *args, **kwargs):
        """Spawns processes with specified ``fn`` and ``args``/``kwargs``."""
        pass
    
    def setup(self, local_rank: int, world_size: int):
        """Initialize DDP variables and processes if required."""
        pass
    
    def cleanup(self):
        """Cleans DDP variables and processes."""
        pass
    
    
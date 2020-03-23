from brain_layers.memory_state import MemoryState
from brain_layers.true_processor import TrueProcessor
from brain_layers.accepting_processing_layer import APL
from brain_layers.sensor_input_layer import Sensor
class Brain:
    def __init__(self):
        # Declare Layers

        # Sensory Layer and Motor Output Layer
        sensor = Sensor()
        # Accepting Processing Layer = Thalamus
        action_processor = APL()

        # Memory Data State = Hippocampus
        memory_inst = MemoryState()

        # True Data Processor = Brainstem components
        t_processor = TrueProcessor()

        # Refresh Rate = 60 ticks/second
    
    def start(self):
        # begins a loop of activity
        self.sensor.open_sensors()
    
    

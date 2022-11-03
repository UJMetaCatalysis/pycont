import json
import pycont.controller


with open("single_pump_test.json") as file:
    config = json.load(file)


pump_params = config["default"]
pump_address = config["pumps"]["valve1"]

pump_params.update(pump_address)

pump_io = pycont.controller.PumpIO("COM3")

controller = pycont.controller.C3000Controller.from_config(pump_io, "valve1", pump_params)

controller.initialize_valve_only()

controller.set_valve_position('3')

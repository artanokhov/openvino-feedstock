from openvino.runtime import Core
from openvino.frontend import FrontEndManager
import platform

core = Core()
core.get_property("CPU", "AVAILABLE_DEVICES")
core.get_property("AUTO", "SUPPORTED_PROPERTIES")
core.get_property("MULTI", "SUPPORTED_PROPERTIES")
core.get_property("BATCH", "SUPPORTED_PROPERTIES")
core.get_property("HETERO", "SUPPORTED_PROPERTIES")

fem = FrontEndManager()
assert len(fem.get_available_front_ends()) == 6

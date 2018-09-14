from regex_file_collector import Collector
import os
import yaml

pattern = r"simulation_param1_(\d+).*param2_(\d+).*test\.log"
path = os.path.join(os.path.dirname(__file__), os.path.pardir, "tests", "test_hierarchy")


files = Collector(path=path, pattern = pattern, fields=('param1', 'param2'))
flat = files.get_flat()

files.print_tree()

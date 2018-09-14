from regex_file_collector import Collector
import os
import yaml

pattern = r"simulation_param1_(\d+).*param2_(\d+).*test\.log"
path = os.path.join(os.path.dirname(__file__), os.path.pardir, "tests", "test_hierarchy")


files = Collector(path=path, pattern = pattern, fields=('param1', 'param2'))
flat = files.get_flat()

tree1 = files.get_tree()
print(yaml.dump(tree1, default_flow_style=False))
tree2 = files.get_tree(custom_ordering=('param2', 'param1'))
print(yaml.dump(tree2, default_flow_style=False))

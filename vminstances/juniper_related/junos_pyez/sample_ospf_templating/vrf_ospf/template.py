import sys 
from jinja2 import Template
import yaml

with open("intf.yml","r") as yaml_file:
	yaml_data = yaml.load(yaml_file.read())

with open("template.j2","r") as jinja_file:
	jinja_data = jinja_file.read()
	template   = Template(jinja_data)
print("Config redered from Jinja Template")
final_config = template.render(yaml_data)
print final_config


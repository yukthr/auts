import os
import sys
from jinja2 import Template
import yaml

with open("vrf.yml",'r') as yamlfile:
	yaml_data = yaml.load(yamlfile.read())

with open("vrf.j2",'r') as jinjafile:
	jinja_data = jinjafile.read()
	template   = Template(jinja_data)


final_config = template.render(yaml_data)
print final_config

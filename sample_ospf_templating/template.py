from jinja2 import Template
import yaml
import sys

with open('intf.yml','r') as yamlfile:
	yaml_data = yaml.load(yamlfile.read())

with open('template.j2','r') as jinjafile:
	jinja_template = jinjafile.read()
	template = Template(jinja_template)

final_config = template.render(yaml_data)
print final_config

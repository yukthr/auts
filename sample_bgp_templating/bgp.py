import sys
import yaml
from jinja2 import Template
with open("/home/ubuntu/auts/auts/sample_bgp_templating/bgp.yml",'r') as yamlfile:
	yaml_data = yaml.load(yamlfile.read())

with open("/home/ubuntu/auts/auts/sample_bgp_templating/bgp.j2",'r') as jinjafile:
	jinja_data = jinjafile.read()
	template = Template(jinja_data)

final_config = template.render(yaml_data)
print final_config

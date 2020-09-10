from jnpr.junos import Device as d
from jnpr.junos.utils.fs import FS as fs
dev = d(host='192.168.48.91',user='lab',password='lab123')
dev.open()

print("Available Functions")
print("-------------------")
print(dir(fs(dev)))
print("-------------------")
print("directory usage on /var/tmp")
print(fs(dev).directory_usage('/var/tmp'))
print("\n")


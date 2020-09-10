Simple script
 
-----
#!/bin/bash
cd /opt/unetlab
unl_wrapper -a backupdb
tar -czvf /root/backup-eve.tgz evedb.gz labs addons eve-ng.lic html/templates html/images/icons html/includes/config.yml
-----
 
 
This will create a backup file under /root
 
 
 
To restore:
 
---
#!/bin/bash
cd /opt/unetlab
tar -zxvf /root/backup-eve.tgz
systemctl restart licserver
sleep 15
unl_wrapper -a restoredb
---

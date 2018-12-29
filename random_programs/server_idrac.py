#!/usr/bin/env python3

import paramiko
import sys
import logging
logging.basicConfig(level=logging.INFO)


"""

serveraction
Description	Enables you to perform power management operations on the host system.
To run this subcommand, you must have the Execute Server Control Commands permission.

Synopsis	
racadm serveraction <action> -f 
Input	
<action> — Specifies the power management operation to perform. The options are:

hardreset — Performs a force reset (reboot) operation on the managed system.
powercycle — Performs a power-cycle operation on the managed system. This action is similar to pressing the power button on the system’s front panel to turn off and then turn on the system.
powerdown — Powers down the managed system.
powerup — Powers up the managed system.
powerstatus — Displays the current power status of the server (ON or OFF).
graceshutdown — Performs a graceful shutdown of the server. If the operating system on the server cannot shut down completely, then this operation is not performed.
-f — Force the server power management operation.
This option is applicable only for the PowerEdge-VRTX platform. It is used with powerdown, powercycle, and hardreset options.

NOTE: The action powerstatus is not allowed with -a option.
Output	Displays an error message if the requested operation is not completed, or a success message if the operation is completed.
Examples	
Get Power Status on iDRAC,
racadm serveraction powerstatus
                                                   Server Power Status: ON
                                                
racadm serveraction powercycle
                                                   Server power operation successful                                                
"""


def poweron():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname='x.x.x.x',port='22',username='xxxx',password='xxxx',look_for_keys=False)
    stdin,stdout,stderr = client.exec_command('racadm serveraction powerstatus')
    output_read = stdout.read()
    if 'ON' in str(output_read):
        logging.info('\nSystem is already Powered on! Exiting the program')
        sys.exit(1)
    elif 'OFF' in str(output_read):
        logging.info('\n****Powering on System! Hold on  ****')
        stdin, stdout, stderr = client.exec_command('racadm serveraction poweron')
        output_poweron = stdout.read()
        logging.info(str(output_poweron))
    else:
        logging.exception('Exception occured. Probably SSH Timeout! Exiting.')
        sys.exit(1)

poweron()

#Do not use this, always poweroff from the host operating system. This is only for a backup scenario

def poweroff():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname='x.x.x.x',port='22',username='xxxx',password='xxxx',look_for_keys=False)
    stdin,stdout,stderr = client.exec_command('racadm serveraction powerstatus')
    output_read = stdout.read()
    if 'OFF' in str(output_read):
        logging.info('\nSystem is already Powered off! Exiting the program')
        sys.exit(1)
    elif 'ON' in str(output_read):
        logging.info('\n****Powering off System! Hold on  ****')
        stdin, stdout, stderr = client.exec_command('racadm serveraction powerdown')
        output_poweron = stdout.read()
        logging.info(str(output_poweron))
    else:
        logging.exception('Exception occured. Probably SSH Timeout! Exiting.')
        sys.exit(1)
        import paramiko
import sys
import logging
logging.basicConfig(level=logging.INFO)


"""
serveraction
Description	Enables you to perform power management operations on the host system.
To run this subcommand, you must have the Execute Server Control Commands permission.

Synopsis	
racadm serveraction <action> -f 
Input	
<action> — Specifies the power management operation to perform. The options are:

hardreset — Performs a force reset (reboot) operation on the managed system.
powercycle — Performs a power-cycle operation on the managed system. This action is similar to pressing the power button on the system’s front panel to turn off and then turn on the system.
powerdown — Powers down the managed system.
powerup — Powers up the managed system.
powerstatus — Displays the current power status of the server (ON or OFF).
graceshutdown — Performs a graceful shutdown of the server. If the operating system on the server cannot shut down completely, then this operation is not performed.
-f — Force the server power management operation.
This option is applicable only for the PowerEdge-VRTX platform. It is used with powerdown, powercycle, and hardreset options.

NOTE: The action powerstatus is not allowed with -a option.
Output	Displays an error message if the requested operation is not completed, or a success message if the operation is completed.
Examples	
Get Power Status on iDRAC,
racadm serveraction powerstatus
                                                   Server Power Status: ON
                                                
racadm serveraction powercycle
                                                   Server power operation successful                                                
"""


def poweron():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname='192.168.1.77',port='22',username='root',password='openseseme',look_for_keys=False)
    stdin,stdout,stderr = client.exec_command('racadm serveraction powerstatus')
    output_read = stdout.read()
    if 'ON' in str(output_read):
        logging.info('\nSystem is already Powered on! Exiting the program')
        sys.exit(1)
    elif 'OFF' in str(output_read):
        logging.info('\n****Powering on System! Hold on  ****')
        stdin, stdout, stderr = client.exec_command('racadm serveraction poweron')
        output_poweron = stdout.read()
        logging.info(str(output_poweron))
    else:
        logging.exception('Exception occured. Probably SSH Timeout! Exiting.')
        sys.exit(1)

poweron()

#Do not use this, always poweroff from the host operating system. This is only for a backup scenario

def poweroff():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname='192.168.1.77',port='22',username='root',password='openseseme',look_for_keys=False)
    stdin,stdout,stderr = client.exec_command('racadm serveraction powerstatus')
    output_read = stdout.read()
    if 'OFF' in str(output_read):
        logging.info('\nSystem is already Powered off! Exiting the program')
        sys.exit(1)
    elif 'ON' in str(output_read):
        logging.info('\n****Powering off System! Hold on  ****')
        stdin, stdout, stderr = client.exec_command('racadm serveraction powerdown')
        output_poweron = stdout.read()
        logging.info(str(output_poweron))
    else:
        logging.exception('Exception occured. Probably SSH Timeout! Exiting.')
        sys.exit(1)
        

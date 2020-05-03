import subprocess 
import io
import time

def check_status_eve():
    check_output_list = []

    try:

        out_bytes = subprocess.check_output(['gcloud', 'compute', 'instances', 'list'])
        output = out_bytes.decode('utf-8')
        for line in io.StringIO(output.strip('\n')):
            check_output_list.append(line)
    
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        codd      = e.returncode
    if check_output_list[1].split(' ')[0] == 'eve-ng-pro':
        return check_output_list[1].split(' ')[-1]

def power_on():
    

    try:
        if check_status_eve() == 'TERMINATED':
            print('Powering on the Instance -> eve-ng-pro')
            out_bytes = subprocess.check_output(['gcloud', 'compute', 'instances', 'start','eve-ng-pro'])
            output = out_bytes.decode('utf-8')
            time.sleep(5)    
            print(f'Instance current state is: {check_status_eve()}')
        else:
            print('Instance is already Running!')

    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        code      = e.returncode
    
power_on()

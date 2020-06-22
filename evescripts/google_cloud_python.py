
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import time

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)


def list_instances(compute, project, zone, filter=None):
    result = compute.instances().list(project=project, zone=zone, filter=filter).execute()
    return result['items'] if 'items' in result else None


def start_instance(compute, project, zone, instance):
    response = compute.instances().start(project=project, zone=zone, instance=instance).execute()

    while list_instances(compute, project, zone, filter=f"labels.name eq '{instance}'")[0]['status'] != 'RUNNING':
        print('Instance has not started yet!, re-attempting in 20 seconds')
        time.sleep(20)
        response = compute.instances().start(project=project, zone=zone, instance=instance).execute()

    return response


def stop_instance(compute, project, zone, instance):
    response = compute.instances().stop(project=project, zone=zone, instance=instance).execute()

    while list_instances(compute, project, zone, filter=f"labels.name eq '{instance}'")[0]['status'] != 'TERMINATED':
        print('Instance is not stopped!, re-attempting in 20 seconds')
        time.sleep(20)
        response = compute.instances().stop(project=project, zone=zone, instance=instance).execute()

    return response

"""
Planning to put this in Docker, the most important thing is that exporting the credential path, the reason for Docker is that 
multiple GCE instances can now easily be managed with different dockers instead of relying on one computer, 
publihsing this to docker hub, will enable me to deploy the container anywhere, without having to worry about crash of 
raspberry pi if at all if that happens

-> export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

second, intresting thing is that variable 'filter' , it took some time to figure out how to extract information
only for a specific instance, using f-string made is very easy,

-> 'list_instances(compute, project, zone, filter=f"labels.name eq '{instance}'")[0]['status'] != 'RUNNING''

Lastly, making a note of variables here, it generally happens that i forget variables and spend a lot of time
searching for them in functions again. 

gce_eve.stop_instance(service, 'glossy-surge-276114', 'europe-west1-b', instace='eve-ng-pro')
gce_eve.start_instance(service, 'glossy-surge-276114', 'europe-west1-b', instace='eve-ng-pro')
gce_eve.list_instances(service, 'glossy-surge-276114', 'europe-west1-b')
 





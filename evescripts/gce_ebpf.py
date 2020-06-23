from pprint import pprint
from collections import defaultdict
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import time
import os

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)


def list_instances(compute, project, zone, filter=None):
    result = compute.instances().list(project=project, zone=zone, filter=filter).execute()
    return result['items'] if 'items' in result else None


def start_instance(compute, project, zone, instance):
    response = compute.instances().start(project=project, zone=zone, instance=instance).execute()

    while list_instances(compute, project, zone, filter=f"labels.name eq '{instance}'")[0]['status'] != 'RUNNING':
        print('Instance is not Running Yet!, re-attempting in 20 seconds')
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

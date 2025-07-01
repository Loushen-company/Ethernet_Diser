import subprocess

def disable_services(service_list):
    for service in service_list:
        subprocess.call(f"sc stop {service}", shell=True)

def enable_services(service_list):
    for service in service_list:
        subprocess.call(f"sc start {service}", shell=True)

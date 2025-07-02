import subprocess

def stop_service(service_name):
    subprocess.call(f"sc stop {service_name}", shell=True)
    subprocess.call(f"sc config {service_name} start= disabled", shell=True)

def start_service(service_name):
    subprocess.call(f"sc config {service_name} start= demand", shell=True)
    subprocess.call(f"sc start {service_name}", shell=True)

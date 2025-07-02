import subprocess

def block_apps(app_list):
    for app in app_list:
        subprocess.call(f'netsh advfirewall firewall add rule name="{app}" dir=out program="{app}" action=block', shell=True)

def unblock_apps(app_list):
    for app in app_list:
        subprocess.call(f'netsh advfirewall firewall delete rule name="{app}"', shell=True)

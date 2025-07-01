import subprocess

def block_apps(app_list):
    for app in app_list:
        subprocess.call(f'netsh advfirewall firewall add rule name="Block_{app}" dir=out action=block program="{app}" enable=yes', shell=True)

def unblock_all():
    subprocess.call('netsh advfirewall firewall delete rule name=all', shell=True)

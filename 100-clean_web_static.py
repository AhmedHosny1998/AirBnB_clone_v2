from fabric.api import env, local, run, cd
import os

# Define the list of web servers
env.hosts = ['52.91.154.128', '54.236.41.153']

def do_clean(number=0):
    """Delete out-of-date archives."""
    number = 1 if int(number) <= 1 else int(number)

    # Delete unnecessary archives in the versions folder locally
    local_archives = sorted(os.listdir("versions"))
    local_archives_to_keep = local_archives[-number:]
    local_archives_to_delete = [a for a in local_archives if a not in local_archives_to_keep]
    for archive in local_archives_to_delete:
        local("rm versions/{}".format(archive))

    # Delete unnecessary archives in the /data/web_static/releases folder remotely
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        remote_archives_to_keep = remote_archives[-number:]
        remote_archives_to_delete = [a for a in remote_archives if a not in remote_archives_to_keep]
        for archive in remote_archives_to_delete:
            run("rm -rf {}".format(archive))



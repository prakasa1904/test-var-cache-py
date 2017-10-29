# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
from fabric.api import *

env.hosts = [
  # 'localhost'
  # 'server.domain.tld',
  # 'ip.add.rr.ess
  # 'server2.domain.tld',
]
# Set the username
env.user   = "root"

# Set the password [NOT RECOMMENDED]
# env.password = "mautauajah"

def trippedia_front_php():
  repoPath = 'git@bitbucket.org:mypermatawisatagroup/frontend-php-version.git'
  basePath = '/data/apps/trippedia.co.id'
  result = local("ls -l " + basePath, capture=True)
  if result.failed:
    local('cd /data/apps && mkdir trippedia.co.id && cd ' + basePath + 'git clone ' + repoPath)
  else:
    run('git checkout . && git pull')
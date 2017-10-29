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

def update_upgrade():
  """
  Update the default OS installation's
  basic default tools.
  """
  #run("aptitude    update")
  #run("aptitude -y upgrade")
  pass
  
def install_memcached():
  """ Download and install memcached. """
  #run("aptitude install -y memcached")
  pass

def trippedia_front_php():
  #update_upgrade()
  #install_memcached()
  run("cd /data/apps")
  run("mkdir trippedia.co.id")

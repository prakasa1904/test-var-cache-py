# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
from fabric.api import *
import os

SENDMAIL = '/usr/sbin/sendmail'

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

def trippedia_front_php(repository, branch, action, author, commit):
  repoPath = 'git@bitbucket.org:mypermatawisatagroup/frontend-php-version.git'
  basePath = '/data/apps/'
  if os.path.isdir(basePath) == False:
    args = 'cd /data/apps && git clone ' + repoPath + ' trippedia.co.id && yes'
    local(args)
  else:
    local('git checkout . && git pull')

  sender = 'prakasa@devetek.com'
  receiver = ['nedya.prakasa@tokopedia.com, office@mypermatawisata.com']
  subject = 'MPW Hook'
  text = author + ' ' + action + ' to ' + repository + ' with ID ' + commit
  message = """\
  From: %s
  To: %s
  Subject: %s
  %s
  .
  """ % (sender, ", ".join(receiver), subject, text)
  p = os.popen("%s -t -i" % SENDMAIL, "w")
  p.write(message)
  status = p.close()
  if status:
    print "Sendmail exit status %s" % status
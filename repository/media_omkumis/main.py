# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
import os
from fabric.api import *
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

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

def deploy(config, repository, branch, action, author, commit):
  repoPath = config['repository']
  basePath = config['path']

  if branch == config['branch']:
    if os.path.isdir(basePath) == False:
      args = 'cd /data/apps && git clone ' + repoPath + ' trippedia.co.id'
      local(args)
    else:
      args = 'cd ' + basePath + ' && git checkout . && git pull'
      local(args)

  # send mail to list email
  msg = MIMEText(author + ' ' + action + ' to ' + repository + ' with ID ' + commit)
  msg["From"] = config['email']['from']
  msg["To"] = config['email']['to']
  msg["Subject"] = config['email']['subject']
  p = Popen([SENDMAIL, '-t', '-oi'], stdin=PIPE)
  p.communicate(msg.as_string())
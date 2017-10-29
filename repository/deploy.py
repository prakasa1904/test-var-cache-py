# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
from fabric.api import *
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

SENDMAIL = '/usr/sbin/sendmail'
FROM = 'prakasa@devetek.com'
TO = 'prakasa@devetek.com,office@mypermatawisata.com'
SUBJECT = 'MPW Hook'

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
  basePath = '/data/apps/trippedia.co.id'
  if os.path.isdir(basePath) == False:
    args = 'cd /data/apps && git clone ' + repoPath + ' trippedia.co.id'
    local(args)
  else:
    args = 'cd ' + basePath + ' && git checkout . && git pull'
    local(args)

  # send mail to list email
  msg["From"] = FROM
  msg["To"] = TO
  msg["Subject"] = SUBJECT
  msg = MIMEText(author + ' ' + action + ' to ' + repository + ' with ID ' + commit)
  p = Popen([SENDMAIL + ' ' + msg["To"], "-i"], stdin=PIPE)
  p.communicate(msg.as_string())
# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
from fabric.api import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

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
  receiver = 'nedya.prakasa@tokopedia.com, office@mypermatawisata.com'
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Link"
  msg['From'] = sender
  msg['To'] = receiver
  html = """\
  <html>
    <head></head>
    <body>
      <p>%s %s to %s with ID %s<br>
        <br>
        More detail visit <a href="https://trippedia.co.id">Trippedia</a>
      </p>
    </body>
  </html>
  """ % (author, action, repository, commit)
  content = MIMEText(html, 'html')
  msg.attach(content)
  send = smtplib.SMTP('localhost')
  send.sendmail(sender, receiver, msg.as_string())
  send.quit()
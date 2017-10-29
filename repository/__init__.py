import json

class repoValidation:
  engine = 'bitbucket'
  repository = ''
  branch = ''
  action = ''
  author = ''
  commit = ''

  def __init__(self, hookData):
    self.repository = self.set_repository(hookData)
    self.branch = self.set_branch(hookData)
    self.action = self.set_action(hookData)
    self.author = self.set_author(hookData)
    self.commit = self.set_commit(hookData)

  def set_repository(self, hookData):
    try:
      return hookData['repository']['name']
    except NameError:
      return False

  def set_branch(self, hookData):
    try:
      if 'push' in hookData:
        return hookData['push']['changes'][0]['new']['name']
    except NameError:
      return False

  def set_action(self, hookData):
    try:
      if 'push' in hookData:
        return 'push'
    except NameError:
      return False

  def set_author(self, hookData):
    try:
      author = '%s - (%s)' % hookData['actor']['display_name'], hookData['actor']['username']
      return author
    except NameError:
      return False

  def set_commit(self, hookData):
    try:
      if 'push' in hookData:
        return hookData['push']['changes'][0]['new']['target']['hash']
    except NameError:
      return False

  def is_valid_hook(self):
    if (self.repository != False and 
    self.branch != False and 
    self.action != False and 
    self.author != False and 
    self.commit != False):
      return True
    return False

  def success(self, customMessage=''):
    print 'Repo : %s' % self.repository
    print 'Branch : %s' % self.branch
    print 'Action %s' % self.action
    print 'Author %s' % self.author
    print 'Hash %s' % self.commit

    if customMessage != '':
      return json.dumps({
        'message' : customMessage,
        'status': 8
      }) 
    return json.dumps({
      'message' : 'Success Deploy',
      'status': 8
    })

  def error(self, customMessage=''):
    if customMessage != '':
      return json.dumps({
        'message' : customMessage,
        'status': 0
      }) 
    return json.dumps({
      'message' : 'Error Deploy',
      'status': 0
    })
from repository.media_omkumis.main import deploy as media_omkumis
from repository.trippedia.main import deploy as trippedia

def trippedia_front_php(config, repository, branch, action, author, commit):
  trippedia(config, repository, branch, action, author, commit)

  def media_api_omkumis_php(config, repository, branch, action, author, commit):
    media_omkumis(config, repository, branch, action, author, commit)

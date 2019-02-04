import os

def setup_openrefine():
  path = os.path.join(os.environ['HOME'], 'openrefine')
  return {
    'command': ['$HOME/.openrefine/openrefine-2.8/refine', '-p', '{port}','-d',path],
    'port': 3333,
    #The following needs a the labextension installing.
    #eg in postBuild: jupyter labextension install jupyterlab-server-proxy
    'launcher_entry': {
        'title': 'OpenRefine',
    },
  }

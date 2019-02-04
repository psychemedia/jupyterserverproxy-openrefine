# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['/home/jovyan/.openrefine/openrefine-2.8/refine', '-p', '{port}','-d','/home/jovyan/openrefine'],
        'port': 3333,
        'timeout': 120,
        'launcher_entry': {
            'title': 'OpenRefine'
        },
    },
}

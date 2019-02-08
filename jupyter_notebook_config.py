# Traitlet configuration file for jupyter-notebook.
#Can we guarantee access to environment vars in this file?
#The start command is tied to the OpenRefine version number
#unless we rename it earlier in the setup process
c.ServerProxy.servers = {
    'openrefine': {
        'command': ['/home/jovyan/.openrefine/openrefine-3.1/refine','-ip','0.0.0.0', '-p', '{port}','-d','/home/jovyan/openrefine'],
        'port': 3333,
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'icon_path': '/home/jovyan/.jupyter/open-refine-logo.svg',
            'title': 'OpenRefine',
        },
    },
}

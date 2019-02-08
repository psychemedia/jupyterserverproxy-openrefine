# jupyterserverproxy-openrefine
Jupyter-server-proxy config for running OpenRefine.


Open to Notebook homepage: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/reconciler)

Open to OpenRefine: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/reconciler?urlpath=openrefine)

*Early original work on getting OpenRefine running in MyBinder was done by @betatim ([betatim/openrefineder](https://github.com/betatim/openrefineder)) and @yuvipanda helped me get my head round various bits of [jupyterhub/jupyter-server-proxy/](https://github.com/jupyterhub/jupyter-server-proxy/) which is key to proxying web services via Jupyter. @manics PR for handling predefined, rather than allocated, port mappings also made life much easier...*

This `reconciler` branch demonstrates:

- using serverproxy (traitlet definition) to add an *OpenRefine* menu option to the notebook start menu. The configuration uses a fixed port assigment so that we can work with the client package.
- the launching of a kernel gateway API service.

OpenRefine can now be started and launched from the notebook homepage New menu or from the JupyterLab launcher.

The OpenRefine client can be found on the `openrefine` path or on a path explictly via the predefined port (`proxy/3333/`).

Calling the path directly (eg starting MyBinder with the path `openrefine`, or adding `?urlpath=openrefine` to the Bunder URL) will launch the Binder container directly into the OpenRefine GUI application.

Note that OpenRefine needs to be launched or otherwise started in order for it to be availagle to the Python Openrefine client.

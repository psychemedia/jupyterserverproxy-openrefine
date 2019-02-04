# jupyterserverproxy-openrefine
Jupyter-server-proxy config for running OpenRefine.


Open to Notebook homepage: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/master)

Open to OpenRefine: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/master?urlpath=openrefine)

Open to Jupyterlab: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/master?urlpath=lab)


*Early original work on getting OpenRefine running in MyBinder was done by @betaim ([betatim/openrefineder](https://github.com/betatim/openrefineder)) and @yuvipanda helped me get my head round various bits of [jupyterhub/jupyter-server-proxy/](https://github.com/jupyterhub/jupyter-server-proxy/) which is key to proxying services via Jupyter. @manics PR for handling predefined, rather than allocated, port mappings also made like much easier...*

This `master` branch demonstrates:

- using serverproxy (traitlet definition) to add an *OpenRefine* menu option to the notebook start menu. The configuration uses a fixed port assigment so that we can work with the client package.
- a button is also enabled and added to the JupyterLab launcher.

OpenRefine can now be started and launched from the notebook homepage New menu or from the JupyterLab launcher.

The OpenRefine client can be found on the `openrefine` path or on a path explictly via the predefined port (`proxy/3333/`).

Calling the path directly (eg starting MyBinder with the path `openrefine`, or adding `?urlpath=openrefine` to the Bunder URL) will launch the Binder container directly into the OpenRefine GUI application.

Note that OpenRefine needs to be launched or otherwise started in order for it to be availagle to the Python Openrefine client.

There are several other branches in this repo that demonstrate other ways of working with OpenRefine in MyBinder/using `repo2docker`.

- `start`: a simple setup that installs OpenRefine and autostarts it. This OpenRefine server can be accessed by the Python OpenRefine client (eg via the demo Jupyter notebook(s)) but the UI is not available;
- `simpleproxy`: a container that installs and autoruns the OpenRefine server, and also makes it available as a proxied URL against known port (the port the OpenRefine server is explicitly started on);
- `setup`: a script that uses the Python package `setup.py` method of installing the serverproxy extension, preconfigured for proxying OpenRefine.
- `traitlet-nolab`: a simple traitlet definition that does not install an OpenRefine icon into the JupyterLab launcher.

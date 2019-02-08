# jupyterserverproxy-openrefine
Jupyter-server-proxy config for running OpenRefine

Start on Jupyter notebook homepage: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/pgdemo)

Start in OpenRefine client: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/pgdemo?urlpath=openrefine)

This `pgdemo` branch demonstrates:

- using serverproxy (traitlet definition) to add an *OpenRefine* menu option to the notebook start menu. The configuration uses a fixed port assigment so that we can work with the client package.
- postgres running in the Binder image

OpenRefine can now be started and launched from the notebook homepage New menu.

The OpenRefine client can be found on the `openrefine` path or on a path explictly via the predefined port (`proxy/3333/`).

Calling the path directly (eg starting MyBinder with the path `openrefine`, or adding `?urlpath=openrefine` to the Bunder URL) will launch the Binder container directly into the OpenRefine GUI application.

Note that OpenRefine needs to be launnched or otherwise started in order for it to be availagle to the Python Openrefine client.

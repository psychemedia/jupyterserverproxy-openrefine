# jupyterserverproxy-openrefine
Jupyter-server-proxy config for running OpenRefine

Start in Jupyter notebook homepage: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/setup)

Start in OpenRefine client: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/setup?urlpath=openrefine)


This `setup` branch demonstrates:

- using serverproxy (setup definition) to add an *OpenRefine* menu option to the notebook start menu. The configuration uses a fixed port assigment so that we can work with the client package.

An OpenRefine option is added to the start menu and can be used to start the OpenRefine server and launch the UI client on the path `openrefine`. (As we started the server on a known port, can also find it explictly at `proxy/3333`.)

Calling the aliased URL directly will also start the server. This means we can tell MyBinder to open on the `openrefine` path (or add `?urlpath=openrefine` to the Binder URL) and the container will open into the OpenRefine application.

Note that if you try to use the Python client without starting the OpenRefine server by launching it, there will be no OpenRefine server for the client to connect to.

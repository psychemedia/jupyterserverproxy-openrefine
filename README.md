# jupyterserverproxy-openrefine
Jupyter-server-proxy config for running OpenRefine

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/simpleproxy)

This `simpleproxy` branch demonstrates:

- using a `binder/start` file to auto start OpenRefine;
- a notebook/client demo; this essentially runs in a headless mode, though you will need to ensure that a project exists before you try to open one! (There are no projects provided as a default in this example.)
- using *serverproxy* to proxy the OpenRefine port to `/proxy/3333/`; note that __the trailing slash is important__. Without it, the static files (CSS etc) required to render the page are not resolved correctly..

# jupyterserverproxy-openrefine
Jupyter-server-proxy config for running OpenRefine.


Open to Notebook homepage: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/reconciler)

Open to OpenRefine: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-openrefine/reconciler?urlpath=openrefine)

__CURRENTLY BROKEN - OPENREFINE HANGS WHEN TRYING TO RECONCILE AGAINST THE RECONCILIATION SERVICE__


This `reconciler` branch demonstrates:

- using serverproxy (traitlet definition) to add an *OpenRefine* menu option to the notebook start menu. The configuration uses a fixed port assigment so that we can work with the client package.
- the launching of a kernel gateway API service.

OpenRefine can now be started and launched from the notebook homepage New menu or from the JupyterLab launcher.

The OpenRefine client can be found on the `openrefine` path or on a path explictly via the predefined port (`proxy/3333/`).

Calling the path directly (eg starting MyBinder with the path `openrefine`, or adding `?urlpath=openrefine` to the Bunder URL) will launch the Binder container directly into the OpenRefine GUI application.

## Reconciler:

The reconciler is on:

`https://hub.mybinder.org/PATH/proxy/8895/parliament/reconcile/`

(You need the trailing slash. That is perhaps one problem?)

reate a simple OpenRefine project from clipboard with a sincle row, eg *Diana Abbot*

Reconcile:

`https://hub.mybinder.org/user/PATH/proxy/8895/parliament/reconcile/?queries={%22q1%22:{%22query%22:%22Diana%20Abbot%22}}`

The service is defined in `notebooks/Reconciler.ipynb` using the Jupyter Kernel Gateway, which allows you to create simple API servers in a Juptyer notebook and serve them using Jupyter machinery.

I would have expected to also be able to register the service in OpenRefine with:

`http://localhost:8895/parliament/reconcile`

but that seems not to work?

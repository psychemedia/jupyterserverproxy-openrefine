import setuptools

setuptools.setup(
  name="jupyter-openrefine-server",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['openrefine'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'openrefine = openrefine:setup_openrefine',
      ]
  },
)

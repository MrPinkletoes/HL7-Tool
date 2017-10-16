from distutils.core import setup
import py2exe

setup(console=['S360_Cleardown.py'],
      options={
          'py2exe': {
              'packages': ['pypyodbc']
          }
      })

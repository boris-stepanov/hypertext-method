#!virtualenv/bin/python

from source import source

source.run(host="0.0.0.0", port="41337", threaded=True, debug=True)

#!/bin/bash

export MACOSX_DEPLOYMENT_TARGET=10.9
$PYTHON setup.py install --single-version-externally-managed --record=record.txt   # Python command to install the script.

# Add more build steps here, if they are necessary.

# See
# http://docs.continuum.io/conda/build.html
# for a list of environment variables that are set during the build process.

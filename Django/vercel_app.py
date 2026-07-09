import os
import sys

# Add the Django directory to the python path to allow importing CryptoSight
sys.path.append(os.path.dirname(__file__))

from CryptoSight.wsgi import application

# Expose WSGI handler as 'app' for Vercel
app = application

#!/bin/bash
echo "Installing dependencies..."
python3 -m pip install -r Django/requirements.txt

echo "Collecting static files..."
python3 Django/manage.py collectstatic --noinput

#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python ./StyleTattoo/manage.py collectstatic --no-input
python ./StyleTattoo/manage.py migrate
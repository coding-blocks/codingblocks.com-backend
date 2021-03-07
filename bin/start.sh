#! /bin/sh

nginx && gunicorn cbdb.wsgi -b 0.0.0.0:8000

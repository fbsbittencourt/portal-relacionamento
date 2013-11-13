#!/bin/bash

# Developed by Henrique Leal <hm.leal@hotmail.com>
# =============================================================================

# Activate the virtualenv
source ~/public_html/venvs/mr2digital_env/bin/activate

# Run django app
python ~/public_html/mr2digital/manage.py runserver 0.0.0.0:4000
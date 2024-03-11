#!/bin/bash

git clone https://github.com/KasRoudra/MaxPhisher

cd MaxPhisher

pip install -r files/requirements.txt --break-system-packages

python3 maxphisher.py
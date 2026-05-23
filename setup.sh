#!/bin/bash
echo "Installing SITE-BUSTER dependencies..."
pkg install python
pip install requests
python script.py

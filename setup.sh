#!/bin/bash
echo "Installing SITE-BUSTER dependencies..."
pkg install python
pip install requests
echo "alias SITE-BUSTER='cd ~/SITE-BUSTER && bash setup.sh'" >> ~/.SITE-BUSTER_short_cut

python script.py

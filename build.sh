#!/bin/bash
set -e

apt-get update
apt-get install -y \
  build-essential \
  cmake \
  libopenblas-dev \
  liblapack-dev \
  libx11-dev \
  libgtk-3-dev \
  tesseract-ocr \
  libgl1

pip install --upgrade pip
pip install -r requirements.txt

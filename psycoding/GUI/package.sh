#!/bin/bash

pyinstaller --windowed --onefile --clean --noconfirm main.py
pyinstaller --clean --noconfirm --windowed --onefile main.spec
cat:
	cat Makefile

all:
	pyuic5 window.ui -o showMainGui.py

designer:
	designer window.ui

run:
	uv run main.py

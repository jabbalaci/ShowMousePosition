all:
	pyuic5 window.ui -o showMainGui.py

cat:
	cat Makefile

designer:
	designer window.ui

run:
	python3 main.py

poetry_run:
	poetry run python main.py

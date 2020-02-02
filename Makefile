setup:
	# You may want to do this
	virtualenv --python $(which python3) ~/.delivery
	# afterward then source
	# source ~/.hellovenv/bin/activate


install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py

all: 
    install lint test
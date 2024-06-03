.PHONY: install run 


install:
		pip install -r requirements.txt
		python -m pip install --upgrade pip
		echo "-dependencies installed"


run:
		flask run --debug --port 5000
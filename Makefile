build_deb: 
	sudo apt-get install python3-stdeb fakeroot python-all dh-python
	/usr/bin/python3 setup.py --command-packages=stdeb.command bdist_deb

build_wheel:
	python3 setup.py bdist-build_wheel

default: build_deb build_wheel

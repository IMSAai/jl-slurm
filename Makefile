build_deb: 
	sudo apt-get install python3-stdeb fakeroot python-all dh-python
	/usr/bin/python3 setup.py --command-packages=stdeb.command bdist_deb
clean:
	rm -rf deb_dist/
	rm -rf dist/
	rm -f jl-slurm-*.tar.gz
	rm -rf *.egg-info/
	rm -f *.out
build_wheel:
	python3 setup.py bdist-build_wheel

default: clean build_deb build_wheel

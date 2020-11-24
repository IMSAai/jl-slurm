# jup_sched
Scheduler for Jupyter Notebook on clusters where compute nodes are hidden behind head/login nodes

This version of the scheduler is forked from [NCSA](https://github.com/ncsa/jup_sched).
## Usage
```
usage: jup_sched [-h] [-e EMAIL] [-t TIME] [-r RESERVATION]
                 [-py2] [--password] [-d]

Jupyter Notebook Scheduler

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        specify an email address for the scheduler
                        communication
  -t TIME, --time TIME  specify the running time for the scheduler in the
                        format HH:MM:SS
  -r RESERVATION, --reservation RESERVATION
                        specify a reservation to submit the job to
  -py2, --python2       use a Python 2.x environment (Python 3.x is used by
                        default)
  --password            re-print the password and address for the jupyter
                        notebook WILL IGNORE ALL OTHER ARGUMENTS
  -d, --debug           keep the scheduler's transcript of the console output
                        (off by default)
```

## Building packages
**Debian/Ubuntu**

Run `make build_deb` and install the `.deb` file that is outputted in folder `deb_dist`.

**Other platforms**

Run `make build_wheel` and install the `.whl` file (outputted in `dist` folder) using `pip3`.

## Supported schedulers
 - Slurm

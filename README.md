# jup_sched
Scheduler for Jupyter Notebook on clusters where compute nodes are hidden behind head/login nodes

## Usage
```
usage: jup_sched [-h] [-e EMAIL] [-t TIME] [-r RESERVATION] [-E CONDAENV]
                 [--gpu] [-py2] [--password] [-d]

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
  -E CONDAENV, --condaenv CONDAENV
                        specify a Conda environment to use (Default is
                        powerai)
  --gpu                 use this option if you require a GPU to be scheduled
  -py2, --python2       use a Python 2.x environment (Python 3.x is used by
                        default)
  --password            re-print the password and address for the jupyter
                        notebook WILL IGNORE ALL OTHER ARGUMENTS
  -d, --debug           keep the scheduler's transcript of the console output
                        (off by default)
```

## Supported schedulers
 - PBS-based (TORQUE, Moab, PBSPro, etc.)
 - Slurm

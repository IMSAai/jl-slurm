# jl-slurm
Scheduler for Jupyter Notebook on SLURM clusters where compute nodes are hidden behind head/login nodes. This software is deployed on the [EpochML](https://epochml.org) cluster.

This version of the scheduler is forked from [NCSA](https://github.com/ncsa/jup_sched).

## Usage
```
usage: jl-slurm [-h] [-t TIME] [-p PARTITION] [-e CONDAENV] [-n NCPUS] [--ngpus NGPUS] [-d]

Jupyter Notebook Scheduler

optional arguments:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  specify the running time for the scheduler in the format HH:MM:SS
  -p PARTITION, --partition PARTITION
                        specify the partition to run the job in (default cpu-long)
  -e CONDAENV, --condaenv CONDAENV
                        specify the conda environment to activate
  -n NCPUS, --ncpus NCPUS
                        specify the number of CPUs for the lab environment (default 2)
  --ngpus NGPUS         specify the number of GPUs for the lab environment (default 0)
  -d, --debug           keep the scheduler's transcript of the console output (off by default)
```
## Web Proxy
This tool assumes that there is a web proxy that is running on some other node that proxies JupyterLab requests based on the hostname and port. 

For example, a request to "cpu1.jl.epochml.org:10043" should be routed to SLURM node cpu1 on port 10043. This allows for effective SSL termination, logging, etc. 

Here is a sample NGINX server block:
```
server {
    server_name     ~^(?<name>.+)\.jl\.epochml\.org$;
    listen 10000-10400 ssl;
    ssl_certificate <ssl cert>;
    ssl_certificate_key <ssl key>;
    ssl_protocols TLSv1.2 TLSv1.3;
    resolver <ip of DNS resolver that can resolve SLURM hostnames>;
    location / {
        proxy_pass http://$name.<hostname domain>:$server_port;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # websocket headers
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_set_header X-Scheme $scheme;
    }
    error_page 500 502 503 504 /500.html; # 'no jupyterlab running' page
    location = /500.html {
            root /var/www/html;
            internal;
    }
}
```

## Building packages
**Debian/Ubuntu**

Run `make build_deb` and install the `.deb` file that is outputted in folder `deb_dist`.

**Other platforms**

Run `make build_wheel` and install the `.whl` file (outputted in `dist` folder) using `pip3`.

## Supported schedulers
 - Slurm

# company-ontology

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Docker](https://img.shields.io/badge/docker-v3+-blue.svg)
![Docker-Compose](https://img.shields.io/badge/docker_compose-v3.0+-blue.svg)
[![GitHub Issues](https://img.shields.io/github/issues/cbadenes/company-ontology.svg)](https://github.com/cbadenes/company-ontology/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## Basic Overview
Ontology to represent companies and related information. 

## Quick Start

It is based on the TBFY platform.

1. Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/install/)
1. Clone this repo

	```
	git clone https://github.com/cbadenes/company-platform.git
	```
1. Download the latest [data dump](https://doi.org/10.5281/zenodo.3712322) from Zenodo into a temporal folder (e.g  `/tmp`).  
1. Run the service by:
    ```
    docker-compose up -d
    ```
1. Wait for all services to be available (e.g. `Started Application in xx.xx seconds`). The first time it may take a few minutes to download the Docker images.
    ```
    docker-compose logs -f
	```
1. Initialize the RDF repository
    1. Log into the Fuseki administration GUI, [http://localhost:3030](http://localhost:3030), using the `admin` user and the password that you set in the `fuseki.env` file.
    1. Create a new dataset `companies` with the dataset type `Persistent (TDB2)`.
    2. Set the environment variable `TBFY_FUSEKI_URL` to:     
       ```
        export TBFY_FUSEKI_URL=http://localhost:3030
	   ```
    3. Upload the NACE and OpenCorporates identifer system data files from [here](https://github.com/cbadenes/company-ontology/tree/master/ids).
    4. Follow [these instructions](https://github.com/TBFY/knowledge-graph/tree/master/python-scripts) to prepare and publish the input data. 
1. That's all! 




# company-ontology

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Docker](https://img.shields.io/badge/docker-v3+-blue.svg)
![Python](https://img.shields.io/badge/docker_compose-v3+-blue.svg)
[![GitHub Issues](https://img.shields.io/github/issues/cbadenes/company-ontology.svg)](https://github.com/cbadenes/company-ontology/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## Basic Overview
Ontology and KG where companies and related information are represented. 

## Quick Start

It is built on top of the [TBFY platform](https://github.com/TBFY/) and the [euBusinessGraph model](https://github.com/euBusinessGraph).

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
1. Load data into the RDF repository
    1. Log into the Fuseki administration GUI, [http://localhost:3030](http://localhost:3030), using the `admin` user and the password that you set in the `fuseki.env` file.
    1. Create a new dataset `tbfy` with the dataset type `Persistent (TDB2)`.
    1. Upload the NACE and OpenCorporates identifer system data files from [here](https://github.com/cbadenes/company-ontology/tree/master/ids).
    1. Create the environment variable `TBFY_FUSEKI_URL` in your localhost:     
       ```
        export TBFY_FUSEKI_URL=http://localhost:3030
	   ```
    1. Follow [these instructions](https://github.com/TBFY/knowledge-graph/tree/master/python-scripts) to prepare and publish the input data. 
1. That's all! 

## Local Resources

A [yasgui-based interface](http://localhost:3040) and a REST API based on [R4R](https://github.com/cbadenes/r4r) are available:

|               service                                                   |            description                             |
|-------------------------------------------------------------------------|----------------------------------------------------|
|    [/organisation](http://localhost:8082/kg-api/organisation)                  |    organizations                                   |
|    [/contract](http://localhost:8082/kg-api/contract)                          |    contracts                                       |
|    [/tender](http://localhost:8082/kg-api/tender)                              |    tenders                                         |
|    [/supplier](http://localhost:8082/kg-api/supplier)                              |    suppliers                                         |
|    [/award](http://localhost:8082/kg-api/award)                                |    awards                                          |
|    [/contractingProcess](http://localhost:8082/kg-api/contractingProcess)      |    contracting processes                           |

## Online Demo

A remote [yasgui-based interface](http://yasgui.tbfy.eu/) and a remote REST API based on [R4R](https://github.com/cbadenes/r4r) are available:

|               service                                                   |            description                             |
|-------------------------------------------------------------------------|----------------------------------------------------|
|    [/organisation](http://data.tbfy.eu/kg-api/organisation)                  |    organizations                                   |
|    [/contract](http://data.tbfy.eu/kg-api/contract)                          |    contracts                                       |
|    [/tender](http://data.tbfy.eu/kg-api/tender)                              |    tenders                                         |
|    [/supplier](http://data.tbfy.eu/kg-api/supplier)                              |    suppliers                                         |
|    [/award](http://data.tbfy.eu/kg-api/award)                                |    awards                                          |
|    [/contractingProcess](http://data.tbfy.eu/kg-api/contractingProcess)      |    contracting processes                           |






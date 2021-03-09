# ccloud-manager

The ccloud-manager allows users to create, describe and delete components in the Confluent Cloud (ccloud) clusters. 
Currently, ccloud-manager supports the management of the following components:

* Connectors
* ksqlDBs
* Service Accounts
* Api-Keys

Ccloud-Manager serves as a python wrapper for the ccloud CLI. 
This provides a reusable and testable artifact for those who need to create and manage ccloud resources.

It also can be easily integrated with CICD pipelines such as Jenkins, TravisCI and CircleCI. 

When using the ccloud-manager script, one must specify the component (connector, ksqlDB, service-account etc.)
and the action (create, describe, delete, list and update) as required parameters. 

The optional parameters (which in some cases aren't optional) specify resource locators that identify which resources need to have an action performed on.
Below are the resource locators parameters for the ccloud components:

* --config, The path to the connector config file 
* --cluster,  The id of the cluster
* --description, The description of the service account
* --id,  The id of the ccloud component
* --name, The name of the ksql db app or service account  

## Connector Management

### Create
In order to create a new connector, one must specify the cluster and the config file with the connector's properties.

`python3 ccloud_component.py connector create --cluster {cluster-id} --config </path/to/connector/config.json>`

### Describe
In order to describe an existing connector, one must specify the connector id.
`python3 ccloud_component.py connector describe --id {connector-id}`

### Delete
In order to delete an existing connector, one must specify the connector id.
`python3 ccloud_component.py connector delete --id {connector-id}`

### List 
In order to list all the existing connectors, just add list.
`python3 ccloud_component.py connector list`

## ksqlDB Management

### Create
In order to create a new ksqlDB, just give the name of the new ksqlDB app.
`python3 ccloud_component.py ksqlDB create --name {name}`

### Describe
In order to describe an existing ksqlDB, one must specify the ksqlDB id.
`python3 ccloud_component.py ksqlDB describe --id {ksqlDB-id}`

### Delete
In order to delete an existing ksqlDB, one must specify the ksqlDB id.
`python3 ccloud_component.py ksqlDB delete --id {ksqlDB-id}`

### List 
In order to list all the existing ksqlDBs, just add list.
`python3 ccloud_component.py ksqlDB list`

## Service Account Management

### Create
In order to create a new service account, just give the name of the new service account app.
`python3 ccloud_component.py service-account create --name {name}`

### Describe
In order to describe an existing service account, one must specify the service account id.
`python3 ccloud_component.py service-account describe --id {service-account-id}`

### Delete
In order to delete an existing service account, one must specify the service account id.
`python3 ccloud_component.py service-account delete --id {service-account-id}`

### List 
In order to list all the existing service accounts, just add list.
`python3 ccloud_component.py service-account list`

### Update 
In order to update an existing service account, one must specify the service account id and it's description.
`python3 ccloud_component.py service-account describe --id {service-account-id} --description {description}`


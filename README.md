# tackle-btp-deployment-poc

A POC for building a CLI for managing the BTP deployment process. 

### Install 

```shell
git clone https://github.com/sudoblockio/tackle-btp-deployment-poc.git
cd tackle-btp-deployment-poc
pip install tackle-box 
```

### Usage 

For a selector on which action to take:
```shell
tackle help 
```

> This could be deprecated in favor of requiring calling hooks as below

For deploying eth:

```shell
tackle deploy --chain eth  
```

### Running Tests 

```shell
pip install -r requirements-dev.txt
pytest . 
```
# simple-file-storage-api
    A simple file storage api to store and manipulate files on filesystem or aws
    
### Installation
    Install requirements from requirements file using : ```pip install -r requirements.txt```
    
### Function documentation:
    The global variable flag contains a numberic value set according to the type of storage mechanism as following:
    1 - for aws(s3)
    2 - for filesystem
    
    The settings file contains aws configuration and bucket name to store files to. This needs to be set before using 
    the api for s3.
    

# simple-file-storage-api
  A simple file storage api to store and manipulate files on filesystem or aws
    
### Installation
  Install requirements from requirements file using  
    ``` pip install -r requirements.txt ```
   
    
### Function documentation:
    The global variable flag contains a numberic value set according to the type of storage mechanism as following:
      1 - for aws(s3)
      2 - for filesystem
    
    The settings file contains aws configuration and bucket name to store files to. This needs to be set before using 
      the api for s3.
    
    File Operations:
    1.Create File:
      Creates a new file. If bukcet name is incorrect, returns string "Bucket does not exists"
      
    2.Open File:
      If file is present, opens it or creates a new file and opens the file in read mode. Returns string from the file.
      
    3.Rename File:
      If file is present renames it, else if not present returns "File does not exists" message.
    
    4. Get File Attributes:
      Returns a json object containing file atrributes like:
      a. LastModified : in the format : 'Y m d H:M:S'
      b. Type: String
      c. Size: In bytes
      If file not present, returns "File not found" message.
    
    4.Delete File:
      If file present deletes if else returns "File does not exists" message.


===
## Project Information
- Title:  `API - Text To Speach`


## Install & Dependence
- python 3.10
- Docker


## Use
- using python
  ```
  python3 pip install -r requirements.txt
  python3 -m uvicorn app:app --host 0.0.0.0 --port 8082 --reload --timeout-keep-alive 600
  ```
- using docker
  ```
  docker build -t tts:latest .
  docker run -d -p 8082:8082 tts:latest
  ```
## Execute

- using python
  ```
  import requests
  import json
  import os
  import shutil

  def download_file(url,params):
      
      headers = {"Content-Type": "application/json; charset=utf-8"}
      
      local_filename = "download.wav"
      with requests.get(url,params=params,headers=headers, stream=True) as r:
          with open(local_filename, 'wb') as f:
              shutil.copyfileobj(r.raw, f)
      return local_filename


  if __name__ == "__main__":
    params = {'context': '​hola, ¿cómo estás?','lang': 'es'}
    url="http://localhost:8082/audio"
    context="""hola, ¿cómo estas?"""
    response = download_file(url,params)
    os.system(f"start {response}") 

  ```

## Directory Hierarchy
```
|—— .gitignore
|—— Dockerfile
|—— LICENCE
|—— app.py
|—— readme.MD
|—— requirements.txt
```

## References
- N/A
  
## License
- MIT

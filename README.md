# Image pre-processing API 

this project is to expose a REST API to pre-process an Image and return the pre-processed image

# Getting started

```
git clone git@github.com:anirbankonar123/imageProcessingAPIDemo.git

```

## Pre-requisites
python 3.9 <br>
pip install opencv-contrib-python <br>
pip install fastapi <br>
pip install python-multipart <br>
pip install "uvicorn[standard]" <br>
pip install pybase64 <br>
pip install scikit-image<br>
pip install docker<br>
pip install pytest<br>
 
1. To deploy REST Endpoint locally 
```
uvicorn app.main:app --reload
```
To prepare base64 encoded string from image
```
python img_encode.py --image <img file name>
```

This will give results in tmp.txt file. Use this String in the image field 
of input JSON, POST request.

input_format = png by default (optional) accepts jpg also

2. To build docker image and deploy REST Endpoint:
```
docker build . -t image-process -f deploy-container.dockerfile
docker run --name imageprocess -d -p 8000:8000 image-process
docker ps
```

To check Swagger API interface, go to http://127.0.0.1:8000/docs

REST API signature for pre-processing of image:

 host:8000/process/encodedimage , and send base64 encoded string as image

Response is JSON with base64 encoded pre-processed image

for local use 127.0.0.1:8000 as host
for docker build use 0.0.0.0:8000

3. Some useful docker cmds:
```
docker stop <container id>
docker rm <container name>
sudo service docker restart
```

4. To run unit test on your api layer:
```
pytest

```




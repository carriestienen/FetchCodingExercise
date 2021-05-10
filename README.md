# Fetch Coding Exercise - Text Similarity

An application to compare two sets of text and rate their similarity on a scale of 0 to 1. Returns 1 when the text files are exactly the same.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Docker
Python3.8 (dev mode)
```

### Installing

For local builds

```
docker build . -t classify:latest
```

This will create a docker image for this project locally.


For developer mode

```
pip install -r requirements.txt
```

## Deployment

For local builds

```
docker run -p 5000:5000 -it classify:latest
```

For developer mode
```
python3.8 ./server.py
```



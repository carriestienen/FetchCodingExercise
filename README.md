# Fetch Coding Exercise - Text Similarity

An application to compare two sets of text and rate their similarity on a scale of 0 to 1. Returns 1 when the text files are exactly the same.

Flask app that accepts a JSON body at `http://localhost:5000/classify`. Expects two arguments named `txt1` and `txt2` in the JSON body. 

Example request body:

```
{
    "txt1":"The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.",
    "txt2":"The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
}
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

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

### Running

For local builds

```
docker run -p 5000:5000 -it classify:latest
```

For developer mode
```
python3.8 ./server.py
```

## Jupyter Notebook

This repository also contains a jupyter notebook explaining the text similarity calculation and what metrics were considered and used.

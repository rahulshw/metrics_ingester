# metrics_ingester
Simple metrics ingester and report generator using Flask

# how to use
1. build the docker image using:
```sudo docker build -t metrics_ingester .```
2. run the container:
```sudo docker run -d --network=host metrics_ingester```

# test
Run the `test.py` from outside the container

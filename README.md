# Spark and Docker Image and Compose

Docker image with Spark to study purposes.

It's a good starting point to learn about Apache Spark using a multi-node environment only using Docker.

## How to configure

You can control master and worker configurations in both the docker-compose and Dockerfile.

The `shared_environment` folder contains both data and codes shared with all nodes.

## How to run

Build image:
```docker build -t spark_docker:0.0.1 spark_docker/```

Compose:
```docker-compose up --build```

Running an example code:
```docker exec spark_docker-spark-master-1 spark-submit /opt/shared_environment/jobs/adventureworks_products.py```
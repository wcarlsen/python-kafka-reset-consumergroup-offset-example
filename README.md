# Python Kafka reset consumergroup offset example

This is a simple example of how to reset consumergroup offset for a given topic without creating new unique consumergroup names.


## Requirements

* Python 3.10
* pipenv
* docker


## Setup description

We will use spotify/kafka for quickly spinning up a kafka broker on localhost:9092. We now have two main Python scripts. A producer that will produce 10 new messages on the same topic with a random UUID as payload and a consumer with auto_commit disabled, that will always reset the offset for a given topic when started.

## How to run

```bash
# 1) Spin up spotify/kafka on localhost:9092
docker compose up

# 2) Start consumer (this will run indefinitely)
pipenv run consume

# 3) Start producer to produce 10 messages
pipenv run produce

# 4) Kill consumer and restart
pipenv run consume

# 5) Optionally produce more messages to test to your own satisfaction
```
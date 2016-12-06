
# Agent 1

## Build
```
docker build -t agent1 .
```


## Run

### Run the environment
```
docker run --privileged --cap-add=SYS_ADMIN --ipc=host -p 5900:5900 -p 15900:15900 quay.io/openai/universe.flashgames
```

### Run the agent
```
docker run --net=host agent1 
```

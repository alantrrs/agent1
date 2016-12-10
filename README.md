
# Agent 1

Test [Open AI Universe](https://github.com/openai/universe) in 3 commands

## Build
First, build the image of the test agent
```
docker build -t agent1 .
```

## Run

### Game environment
Execute the game environment
```
docker run --privileged --cap-add=SYS_ADMIN --ipc=host -p 5900:5900 -p 15900:15900 quay.io/openai/universe.flashgames
```

### Agent
Start the test agent
```
docker run --net=host agent1 
```

That's it, watch your agent at [http://localhost:15900/viewer/?password=openai](http://localhost:15900/viewer/?password=openai)

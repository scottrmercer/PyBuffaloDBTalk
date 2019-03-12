Using docker-compose to launch postgres instance
------------------------------------------------

If you are not interested in installing postgres on your computer and know how to  use docker compose here is every thing you need to launch a postgres and python container with docker compose

Instructions
------------
download the repo 

```
git clone https://github.com/scottrmercer/PyBuffaloDBTalk
```

change directory to `docker/`

```
cd PyBuffaloTalk/docker
```

start the docker containers using docker compose in detachted mode

```
docker-compose up -d
```

run bash inside the python instance

```
docker-compose run python sh
```

run the example python file to play around with your shiny new environment 
should work, dont sue me


credit
------

as always standing on shoulders of giants like [@jgoerner](https://github.com/jgoerner/beyond-jupyter) and [@alysivji](https://github.com/alysivji/talks/tree/master/data-science-workflows-using-docker-containers)

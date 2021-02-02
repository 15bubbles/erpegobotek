# Erpegobotek

## Requirements

- Python 3.8
- Poetry for dependency management
- Docker
- docker-compose

## Installing locally

To install development dependencies you can use Makefile's `install` target.

```
make install
```

It assumes that you have Python 3.8 installed on your machine, because it will use `pip` to install `Poetry` as it is used as a dependency manager. After installing dependency manager it will use it to create a virtual environment and install all dev dependencies.

## Running

### Setting up token

Discord bots need a token to succesfully connect. Token is read from an environment variable. In case of running bot locally you need to set `DISCORD_TOKEN` environment variable. You can do that by copying `example.env` that is in root directory of this project to `.env` and supplementing `DISCORD_TOKEN` variable there. Then you can run

```
export $(cat .env | xargs)
```

This will read `.env` file and set up environment variables into current shell.

When running bot in container, you just need to copy `example.env` to `.env` and supplement `DISCORD_TOKEN` variable. `.env` file will be read with the start of the container and proper environment variables will be set automatically.

### Running locally

When installing project's dependencies, Poetry also creates a virtual environment for you and will install all dependencies into this virtual environment.

So after you install project dependencies you can use Makefile's `local-run` target, that uses Poetry to run everything using virtual environment Poetry created.

```
make local-run
```

### Running in containers

If you prefer to run application in a containerized environment, you can use Makefile's `run` target, which will first build a container with all dependencies and then it will run the application.

```
make run
```

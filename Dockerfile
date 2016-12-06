FROM alantrrs/openai-universe

COPY . /code
WORKDIR /code

ENTRYPOINT python main.py

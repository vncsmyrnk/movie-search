# Movie Search

API for searching movies by its synopsis

## Development with docker

```bash
docker run --rm -it \
    -v "$(pwd)"/src:/var/app \
    -p 5000:5000 \
    --workdir /var/app \
    --cpus 2 \
    --name movie-search \
    python:3.9-slim bash
```

```bash
# Inside container
pip install -r requirements.txt
flask --app server run --host 0.0.0.0
```

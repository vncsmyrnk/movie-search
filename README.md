![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<br>
![CI](https://github.com/vncsmyrnk/movie-search/actions/workflows/ci.yml/badge.svg)
![Release](https://github.com/vncsmyrnk/movie-search/actions/workflows/release.yml/badge.svg)
[![cov](https://vncsmyrnk.github.io/movie-search/coverage.svg)](https://github.com/vncsmyrnk/movie-search/actions)

# Movie Search

API for searching movies by its synopsis

## Run with docker

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

## Examples

```bash
curl -X GET http://localhost:5000/api/query?q=music%20play -s | jq .
```

Returns:

```json
[
  {
    "movie": {
      "avg_score": 70,
      "description": "Six urbanites play musical beds.",
      "description_cleaned": "six urbanit play music bed",
      "movie_uri": "/movie/your-friends-neighbors/",
      "platform": "metacritic",
      "scores": [
        {
          "reviewer_name": "The A.V. Club",
          "score": "100"
        },
        {
          "reviewer_name": "Newsweek",
          "score": "90"
        },
        {
          "reviewer_name": "TV Guide Magazine",
          "score": "80"
        },
        {
          "reviewer_name": "San Francisco Examiner",
          "score": "75"
        },
        {
          "reviewer_name": "The New Republic",
          "score": "70"
        },
        {
          "reviewer_name": "Los Angeles Times",
          "score": "50"
        },
        {
          "reviewer_name": "San Francisco Chronicle",
          "score": "25"
        }
      ],
      "title": "Your Friends & Neighbors",
      "year": "1998"
    },
    "movie_id": 3304,
    "score_jaccard": 0.4
  },
  {...}
]
```

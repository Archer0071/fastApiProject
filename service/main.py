import fastapi.exceptions
from fastapi import FastAPI
import service.movie_data as movie_data
from service.models.movie_model import MovieModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "WELCOME TO FAST-API DEMO"}


@app.get('/api/movie/{title}', response_model=MovieModel)
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)
    else:
        return movie.dict()

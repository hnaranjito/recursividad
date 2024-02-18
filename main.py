from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from data import movies

from model.Movie import Movie
from model.Category import Category


app = FastAPI()
app.title = "Mi aplicación con FastApi"
app.version = "0.0.1"


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return JSONResponse(content=movies)


@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int = Path(ge=1, le=2000)):
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(content=[])


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(min_length=5)):
    data = [item for item in movies if item["category"] == category]
    return JSONResponse(content=data)


@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return JSONResponse(content={"message": "Se ha registrado la película"})


@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(content={"message": "Se ha modificado la película"})


@app.delete('movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "Se ha eliminado la película"})

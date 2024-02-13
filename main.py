from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Mi aplicación con FastApi"
app.version = "0.0.1"


class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi,",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Kingsman: El círculo de oro",
        "overview": "Cuando el cuartel general de la agencia británica Kingsman es destruido, los espías unen sus fuerzas con una organización aliada estadounidense. Su objetivo es colaborar para intentar derrotar a su enemigo común y salvar al mundo",
        "year": 2017,
        "rating": 7.7,
        "category": "Acción"
    },
    {
        "id": 3,
        "title": "Resistencia",
        "overview": "Un antiguo agente de las fuerzas especiales se encuentra al mando de un comando que debe cazar y matar al creador de una inteligencia artificial extraordinaria que tiene la capacidad de aniquilar a toda la humanidad",
        "year": 2023,
        "rating": 7.4,
        "category": "Acción"
    },
    {
        "id": 4,
        "title": "Resistencia",
        "overview": "Un antiguo agente de las fuerzas especiales se encuentra al mando de un comando que debe cazar y matar al creador de una inteligencia artificial extraordinaria que tiene la capacidad de aniquilar a toda la humanidad",
        "year": 2023,
        "rating": 7.4,
        "category": "Acción"
    }
]


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item["category"] == category]


@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies


@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies


@app.delete('movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies

from flask import Blueprint, render_template, request
from pathlib import Path
from .helpers import load_model, predecir_likes_dislikes_views, predecir_dia_semana, recomendar_tags_por_categoria
from datetime import datetime

path_models = Path(__file__).parent.parent / "models"

model_predict_likes = load_model(path_models / "model_like.joblib")
model_predict_dislikes = load_model(path_models / "model_dislikes.joblib")
model_predict_views = load_model(path_models / "model_views.joblib")
model_predict_dia_semana = load_model(path_models / "model_dia_semana.joblib")

dia_semana = datetime.now().weekday()

app_routes = Blueprint('routes', __name__)

@app_routes.route("/")
def index():
    return render_template('index.html')

@app_routes.post("/recomendaciones")
def predict():
    data:dict = request.get_json()

    title = data.get("title")
    title_len = len(title)

    description = data.get("description")
    category_id = int(data.get("category_id"))
    tags = data.get("tags").split(",")

    pred_dia_semana, predict_dia_semana_str = predecir_dia_semana(model_predict_dia_semana, [category_id, title_len])
    
    mejor_dia_semana = None
    if pred_dia_semana == dia_semana:
        mejor_dia_semana = "hoy"
    else:
        mejor_dia_semana = predict_dia_semana_str

    tags_recomendados = recomendar_tags_por_categoria(path_models.parent / "datasets", category_id)
    diff_tags = set(tags_recomendados) - set(tags)
    print(diff_tags)

    return {
        "likes": predecir_likes_dislikes_views(model_predict_likes, dia_semana, category_id),
        "dislikes": predecir_likes_dislikes_views(model_predict_dislikes, dia_semana, category_id),
        "views": predecir_likes_dislikes_views(model_predict_views, dia_semana, category_id),
        "dia_semana": mejor_dia_semana,
        "tags": list(diff_tags)
    }




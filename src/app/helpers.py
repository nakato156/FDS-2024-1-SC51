import joblib
import pandas as pd
from collections import Counter

def load_model(path):
    return joblib.load(path)

def asingnar_popularidad(percentiles, category_id, views):
    if views <= percentiles.loc[category_id, 1/3]:
        return 'Poco popular'
    elif views <= percentiles.loc[category_id, 2/3]:
        return 'Moderadamente popular'
    else:
        return 'Muy popular'


def predecir_likes_dislikes_views(model, dia_semana, category_id):
    features = [dia_semana, category_id, 0]
    return int(model.predict([features])[0])

def predecir_dia_semana(model, features):
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    dia = int(model.predict([features])[0])
    return dia, (dias[dia] if dia in range(7) else "Error")

def recomendar_tags_por_categoria(datasets_path, categoria):
    df = pd.read_csv(datasets_path / "DEvideos.csv")[["video_id","category_id", "tags"]]
    df = df.drop_duplicates("video_id", keep="last")
    df.tags = df.tags.apply(lambda x: x.replace('"', "").lower().replace("[none]", "").split("|"))

    tags = df[df["category_id"] == categoria].agg({
        "tags": "sum"
    })["tags"]

    count_tags = Counter(tags)
    return [x[0] for x in count_tags.most_common(10) if x[0]]
    

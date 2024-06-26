import json
from pathlib import Path

path_json = Path(__file__).parent / "src" / "datasets"
json_ds = path_json / "comments_12961.json"

json_data = json.load(json_ds.open())

def limpiar_datos():
    for comments in json_data:
        for comment in comments:
            comment["text"] = comment["text"].replace("\"", "'")
            comment["text"] = comment["text"].replace("\n", " ")
            comment["text"] = comment["text"].replace("\t", " ").replace("  ", " ")


    mitad = len(json_data)//2
    m1 = json_data[:mitad]
    m2 = json_data[mitad:]

    with open(path_json / "comments_1.json", "w") as f:
        json.dump(m1, f, indent=4)

    with open(path_json / "comments_2.json", "w") as f:
        json.dump(m2, f, indent=4)

data = []
total_comments = 0

for comments in json_data:
    cant_filtrados = 0
    filtrados = []
    for comment in comments:
        comment["text"] = comment["text"].replace("\n", " ")
        comment["text"] = comment["text"].replace("\t", " ")
        if comment["like_count"] > 5:
            filtrados.append(comment)
            cant_filtrados = 1
            total_comments += 1

    if cant_filtrados == 0:
        data.append([comment for comment in comments if len(comment["text"]) > 15])
        total_comments += 10
    else:
        data.append(filtrados)

process = {}
for comentarios in data:
    comentarios_ = comentarios.copy()
    if not comentarios_:
        continue
    id_video = comentarios_[0]['video_id']
    process[id_video] = [{"text":comentario["text"], "like_count": comentario["like_count"]} for comentario in comentarios_]

json.dump(process, open("process_comments.json", "w"), indent=4)
print(len(json_data), len(data), total_comments)
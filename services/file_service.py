import json


FILE_PATH = "data/tickets.json"


def load_objectives():
    with open(FILE_PATH,"r",encoding="utf-8") as file:
        return json.load(file)


def save_objectives(objectives):
    with open(FILE_PATH,"w",encoding="utf-8") as file:
        json.dump(objectives,file,ensure_ascii=False,indent=4)
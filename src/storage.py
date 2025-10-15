import os
import json
from datetime import datetime, date

DATABASE_URL = "database.json"

if not os.path.exists(DATABASE_URL):
    with open(DATABASE_URL, "w") as f:
        f.write("[]")


def read_database() -> list[dict]:
    with open(DATABASE_URL, "r") as f:
        return json.load(f)


def save_database(tasks: list[dict]):
    with open(DATABASE_URL, "w") as f:
        json.dump(tasks, f, indent=4)


def create_task(name: str, description: str, category: str, date: date) -> None:
    tasks = read_database()
    last_task = max(tasks, key=lambda t: t["id"], default={"id": 0})

    new_task = {
        "id": last_task["id"] + 1,
        "name": name,
        "description": description,
        "category": category,
        "due_date": date.strftime("%d/%m/%Y"),
        "created_date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "status": False
    }

    tasks.append(new_task)
    save_database(tasks)


def get_tasks():
    tasks = read_database()
    return [
        {
            "id": t["id"],
            "name": t["name"],
            "description": t["description"],
            "category": t["category"],
            "due_date": datetime.strptime(t["due_date"], "%d/%m/%Y"),
            "created_date": datetime.strptime(t["created_date"], "%d/%m/%Y, %H:%M:%S"),
            "status": t["status"],
        }
        for t in tasks
    ]


def update_task_by_id(task_id: int, name: str, description: str, category: str, due_date: date):
    tasks = read_database()
    for t in tasks:
        if t["id"] == task_id:
            t["name"] = name
            t["description"] = description
            t["category"] = category
            t["due_date"] = due_date.strftime("%d/%m/%Y")
            break
    save_database(tasks)


def delete_task_by_id(task_id: int):
    tasks = read_database()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break

    save_database(tasks)


def mark_task_completed(task_id: int) -> bool:
    tasks = read_database()
    found = False
    for t in tasks:
        if t.get("id") == task_id:
            t["status"] = not t.get("status", False)
            found = True
            break
    if found:
        save_database(tasks)
    return found

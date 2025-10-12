from datetime import datetime
from src.storage import read_file, save_file


def add_task(name, description, category):
    tasks = read_file()

    if tasks:
        new_id = max(tasks, key=lambda n: n["id"])["id"] + 1
    else:
        new_id = 1

    new_task = {
        "id": new_id,
        "name": name,
        "description": description,
        "category": category,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "completed": False
    }

    tasks.append(new_task)
    save_file(tasks)
    print(f"Vazifa #{new_id} muvaffaqiyatli qo'shildi!")


def list_tasks():
    tasks = read_file()
    if not tasks:
        print("Vazifalar mavjud emas.")
        return

    print("\n--- Barcha Vazifalar ---")
    for t in tasks:
        status = "Bajarilgan" if t["completed"] else "Bajarilmagan"
        print(f"{t['id']}. {t['name']} ({t['category']}) - {t['date']} - {status}")


def update_task(task_id, name=None, description=None, category=None):
    tasks = read_file()
    for t in tasks:
        if t["id"] == task_id:
            if name:
                t["name"] = name
            if description:
                t["description"] = description
            if category:
                t["category"] = category
            save_file(tasks)
            print("Vazifa yangilandi!")
            return
    print("Bunday ID topilmadi.")


def delete_task(task_id):
    tasks = read_file()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("Bunday ID topilmadi.")
        return
    save_file(new_tasks)
    print("Vazifa o'chirildi!")


def mark_completed(task_id):
    tasks = read_file()
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            save_file(tasks)
            print("Vazifa bajarildi deb belgilandi!")
            return
    print("Bunday ID topilmadi.")

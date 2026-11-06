import json
import os
import sys

DATA = "todo.json"


def load():
    if os.path.exists(DATA):
        with open(DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save(items):
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def add(text):
    items = load()
    items.append({"text": text, "done": False})
    save(items)
    print("已添加:", text)


def list_all():
    items = load()
    if not items:
        print("暂无待办")
        return
    for i, it in enumerate(items, 1):
        mark = "√" if it["done"] else " "
        print(f"{i}. [{mark}] {it['text']}")


def main():
    if len(sys.argv) < 2:
        print("用法: python todo.py add <内容> | list")
        return
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_all()
    else:
        print("命令错误")


if __name__ == "__main__":
    main()
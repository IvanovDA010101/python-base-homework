import io
import os
import random


def read_file(name):
    with io.open(name, encoding='utf-8') as file:
        text = file.read()
    return text


def read_tasks():
    result = []
    total_tasks = len(os.listdir('src/tasks'))
    print(total_tasks + 1)
    for i in range(1, total_tasks):
        result.append([])
        total_variants = len(os.listdir(f'src/tasks/{i}'))
        for k in range(1, total_variants):
            result[i - 1].append(read_file(f'src/tasks/{i}/{k}.tex'))
    return result


def read_students():
    with io.open("src/students.txt", encoding='utf-8') as file:
        result = file.readlines()
    return result


def generate_variants(tasks, total):
    counts = [len(task) for task in tasks]
    result = set()
    while len(result) < total:
        result.add(generate_variant(counts))
    return list(result)


def generate_variant(counts):
    return tuple(random.randint(1, count) for count in counts)


def create_tex_file(file_name, head, qStart, qStart2, qFinish, tail, tasks, students, variants):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with io.open(file_name, "w", encoding='utf-8') as out:
        print(f"Making {file_name} file...")
        out.write(head)
        for i, student in enumerate(students):
            out.write(qStart + str(student) + qStart2)
            for task_number, task in enumerate(tasks):
                out.write(task[variants[i][task_number] - 1])
            out.write(qFinish)
        out.write(tail)


def create_dump_file(file_name, head, qStart, qStart2, qFinish, tail, tasks):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with io.open(file_name, "w", encoding='utf-8') as out:
        print(f"Making {file_name} file...")
        out.write(head)
        for i in range(len(tasks)):
            out.write(qStart + str(i + 1) + qStart2)
            for task in tasks[i]:
                out.write(task)
            out.write(qFinish)
        out.write(tail)

import random
import file_operations

def main():
    random.seed(1183)
    # Чтение шаблонов
    print("Reading templates...")
    head = file_operations.read_file('src/templates/head.tex')
    qStart = file_operations.read_file('src/templates/qStart.tex')
    qStart2 = file_operations.read_file('src/templates/qStart2.tex')
    qFinish = file_operations.read_file('src/templates/qFinish.tex')
    tail = file_operations.read_file('src/templates/tail.tex')

    # Чтение задач
    print("Reading tasks...")
    tasks = file_operations.read_tasks()

    # Чтение студентов
    print("Reading students...")
    students = file_operations.read_students()

    # Генерация вариаций
    print("Generating variants...")
    variants = file_operations.generate_variants(tasks, len(students))
    random.shuffle(variants)

    # Создание файла main.tex
    file_operations.create_tex_file("output/main.tex", head, qStart, qStart2, qFinish, tail, tasks, students, variants)

    # Создание файла dump.tex
    file_operations.create_dump_file("output/dump.tex", head, qStart, qStart2, qFinish, tail, tasks)

    print("Done!")


if __name__ == "__main__":
    main()


import re
import model.test
import model.vector
from create import examination_poof
from save_data import save
from load_data import load


def creating_first_vector(queue_vector):
    start = model.test.Hash_word('START')
    queue_vector.append(model.vector.Vector(0, start))


def education():
    queue_vector = []
    creating_first_vector(queue_vector)

    patern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|DEBUG|WARN|ERROR) (\[.*\] .*)'

    with open('test_data/test_log.txt', 'r') as f:
        file_log = re.findall(patern, f.read())

    for i in file_log:
        poof = model.test.Hash_word(i[2])
        examination_poof(poof, queue_vector)

    return queue_vector


def view_data(queue_vector):
    print('---------------')
    print('---------------')

    for i in queue_vector:
        try:
            print('---------------')
            print(f'{i.get_start().get_word()} {i.get_start()} => {i.get_end().get_word()} {i.get_end()}')
        except AttributeError:
            print()

    print('---------------')
    print('---------------')
    print('---------------')


if __name__ == '__main__':

    view_data(education())
    # view_data(load())
    # save(queue_vector)

    # from graphviz import Digraph
    # # Создание объекта Digraph с комментарием
    # dot = Digraph(comment='A Round Graph')
    #
    # # Добавление узлов
    # dot.node('A', 'Alex')
    # dot.node('B', 'Rishu')
    # dot.node('C', 'Mohe')
    # dot.node('D', 'Satyam')
    #
    # # Добавление рёбер
    # dot.edges(['AB', 'AC', 'AD'])
    # dot.edge('B', 'C', constraint='false')
    # dot.edge('C', 'D', constraint='false')
    #
    # # Сохранение графика в файл (по умолчанию в формате PDF)
    # dot.format = 'png'
    # dot.render(r"C:/Users/ignat/Documents/python/log/my_file.png", view=True)
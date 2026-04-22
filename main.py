import re
import model.test
import model.vector
from create import examination_poof
from save_data import save
from load_data import load
import view.graph as graph

def creating_first_vector(queue_vector):
    start = model.test.Hash_word('START')
    queue_vector.append(model.vector.Vector(model.test.Hash_word('0'), start))


def education(queue_vector=[]):
    # queue_vector = []
    creating_first_vector(queue_vector)

    # patern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (INFO|DEBUG|WARN|ERROR) (\[.*\] .*)'
    patern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (INFO|DEBUG|WARN|ERROR)\: (.* .*)'

    with open('test_data/test_log3.txt', 'r') as f:
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


def delete_duble_vector(queue_vector):

    for vector in queue_vector:

        try:
            for i in range(len(queue_vector)):
                if ((queue_vector[i].get_end() == vector.get_end()) and
                    (queue_vector[i].get_start() == vector.get_start()) and 
                    (queue_vector[i] != vector)):
                    print('true')
                    queue_vector.pop(i)
        except IndexError:
            print('delete_doble_queue_vector_load')
    return queue_vector

            # else:
            #     print('false')


if __name__ == '__main__':

    # view_data(education())
    # view_data(load())

    # queue_vector = education()
    # save(queue_vector)

    # graph.create(load())



  
    queue_vector_load = load()
    t = len(queue_vector_load)
    delete_doble_queue_vector_load = delete_duble_vector(queue_vector_load)
    t = len(delete_doble_queue_vector_load)
    tt = education(delete_doble_queue_vector_load)
    graph.create(delete_duble_vector(tt), t - 1) 

    print(t)
    graph.create(queue_vector_load, t - 1)


    # delete_doble_queue_vector_load = delete_duble_vector(queue_vector_load)
    # print(len(queue_vector_load), len(delete_doble_queue_vector_load))

    # graph.create(delete_doble_queue_vector_load, len(delete_doble_queue_vector_load) - 1)




        


    # for i in range(len(queue_vector_new)):
    #     print(queue_vector_new[i], queue_vector_load[i]) 
    #     examination_poof(queue_vector_new[i], queue_vector_load)

    # view_data(load())


    # view_data(queue_vector_load)



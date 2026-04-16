from graphviz import Digraph


def create(queue_vector):

    dot = Digraph(comment='A Round Graph')
    v = []
    n = []

 
    
    for i in range(len(queue_vector)):
        # dot.node(" ".join(queue_vector[i].get_end().get_word()), str(queue_vector[i].get_end().get_hex()))

        v.append(str(queue_vector[i].get_end().get_hex()))
        n.append(str(queue_vector[i].get_end().get_word()))

    try:
        list(set(v))
        list(set(n))

        for i in range(len(v)):
            dot.node(str(v[i]), str(n[i]))

        for i in range(len(queue_vector)):
            dot.edge(str(queue_vector[i].get_start().get_hex()), 
                     str(queue_vector[i].get_end().get_hex()), color='blue')
            
            print(i)

    except AttributeError:
        print(queue_vector[i])



    # for i in range(len(queue_vector)):
    #     dot.edge(" ".join(queue_vector[i].get_end().get_word()), 
    #              " ".join(queue_vector[i].get_start().get_word()), constraint='false')
    
    # # Создание объекта Digraph с комментарием
    # dot = Digraph(comment='A Round Graph')
    
    # # Добавление узлов
    # dot.node('A', 'Alex')
    # dot.node('B', 'Rishu')
    # dot.node('C', 'Mohe')
    # dot.node('D', 'Satyam')
    
    # # Добавление рёбер
    # dot.edges(['AB', 'AC', 'AD'])
    # dot.edge('B', 'C', constraint='false')
    # dot.edge('C', 'D', constraint='false')
    
    # # Сохранение графика в файл (по умолчанию в формате PDF)
    dot.format = 'png'
    dot.render(r"./view/my_file", view=True)
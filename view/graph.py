from graphviz import Digraph


def create(queue_vector):

    dot = Digraph(comment='A Round Graph')

 
    
    for i in range(len(queue_vector)):
        dot.node(" ".join(queue_vector[i].get_end().get_word()), str(queue_vector[i].get_end().get_hex()))

        print(queue_vector[i])
    #     print(" ".join(queue_vector[i].get_end().get_word()), 
    #              " ".join(queue_vector[i].get_start().get_word()), constraint='false')



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
    # dot.format = 'png'
    # dot.render(r"./view/my_file", view=True)
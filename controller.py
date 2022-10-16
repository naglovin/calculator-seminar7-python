import model_degree as model
import view

def click():
    num_a = view.get_num()
    num_b = view.get_num()
    model.init(num_a, num_b)
    result = model.do_it()
    view.view_data("Ответ: ",result)
    
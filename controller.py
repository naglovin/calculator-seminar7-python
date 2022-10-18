import model_degree as model
import view
import logger as log


def click():
    num_a = view.get_num()
    num_b = view.get_num()
    model.init(num_a, num_b)
    result = model.do_it()
    log.record(result)
    view.view_data("Ответ: ",result)
    
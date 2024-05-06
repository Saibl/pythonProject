## 1. Moduł main - główny moduł, który administruje zasobami wypożyczalni
## musi zawierać:  def __main__() ( uruchamia program)

import customers

def __main__():
    customers.manage_customer_data()
    customers.output2()
    customer_id = input("Podaj ID klienta: ")
    customers.manage_borrow_return(customer_id)

if __name__ == "__main__":
    __main__()

## 1. Moduł main - główny moduł, który administruje zasobami wypożyczalni
## musi zawierać:  def __main__() ( uruchamia program)

import customers2

def __main__():
    customers2.control_panel()
    customers2.output2()

if __name__ == "__main__":
    __main__()

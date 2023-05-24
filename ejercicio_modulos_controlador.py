from tkinter import Tk
import ejercicio_modulos_vistas


class ControladorPoo:
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = ejercicio_modulos_vistas.ventana_interfaz(
            self.root_controler
        )

    if __name__ == "__main__":
        main = Tk()
        objeto1_controlador = ejercicio_modulos_vistas.VistaPoo(main)
        main.mainloop()

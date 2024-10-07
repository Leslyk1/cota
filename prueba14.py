import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PuntoEquilibrioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Punto de Equilibrio")
        self.create_widgets()

    def create_widgets(self):
        # Entradas de datos
        tk.Label(self.root, text="Precio Por Unidad Q.").grid(row=0, column=0)
        self.precio_var = tk.Entry(self.root)
        self.precio_var.grid(row=0, column=1)

        tk.Label(self.root, text="Costo Fijo Q.").grid(row=1, column=0)
        self.costo_fijo_var = tk.Entry(self.root)
        self.costo_fijo_var.grid(row=1, column=1)

        tk.Label(self.root, text="Costo Variable Por Unidad Q.").grid(row=2, column=0)
        self.costo_variable_var = tk.Entry(self.root)
        self.costo_variable_var.grid(row=2, column=1)

        tk.Label(self.root, text="Margen de Contribución por Unidad Q.").grid(row=0, column=2)
        self.margen_var = tk.Entry(self.root)
        self.margen_var.grid(row=0, column=3)

        tk.Label(self.root, text="Punto de Equilibrio").grid(row=1, column=2)
        self.pe_var = tk.Entry(self.root)
        self.pe_var.grid(row=1, column=3)

        # Botones de acción
        self.calcular_btn = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.calcular_btn.grid(row=0, column=4)

        self.graficar_btn = tk.Button(self.root, text="Graficar", command=self.graficar)
        self.graficar_btn.grid(row=1, column=4)

        self.borrar_btn = tk.Button(self.root, text="Borrar Datos", command=self.borrar_datos)
        self.borrar_btn.grid(row=2, column=4)

        # Tablas de resultados alineadas horizontalmente
        tk.Label(self.root, text="REPRESENTAN LAS UNIDADES PARA ENCONTRAR EL PUNTO DE EQUILIBRIO").grid(row=3, column=0, columnspan=2)
        self.unidades_frame = tk.Frame(self.root)
        self.unidades_frame.grid(row=4, column=0, columnspan=2)

        tk.Label(self.root, text="REPRESENTA LOS DATOS PARA CALCULAR LA GRAFICA DE PUNTO DE EQUILIBRIO").grid(row=3, column=2, columnspan=2)
        self.grafica_frame = tk.Frame(self.root)
        self.grafica_frame.grid(row=4, column=2, columnspan=2)

        # Crear entradas para la tabla de unidades (izquierda)
        self.entradas_tabla_izquierda = {}
        conceptos = ["Ventas", "Costos Variables", "Margen de Contribución", "Costos Fijos", "Utilidad o Pérdida"]
        for i, concepto in enumerate(conceptos):
            tk.Label(self.unidades_frame, text=concepto).grid(row=i, column=0)
            self.entradas_tabla_izquierda[concepto] = []
            for j in range(4):  # 4 columnas
                entry = tk.Entry(self.unidades_frame, width=10)
                entry.grid(row=i, column=j+1)
                self.entradas_tabla_izquierda[concepto].append(entry)

        # Crear entradas para la tabla de graficar (derecha)
        self.entradas_tabla_derecha = {}
        conceptos_grafica = ["Total de unidades", "Ingresos Totales", "Costos Totales", "Costos Variables", "Costos Fijos"]
        for i, concepto in enumerate(conceptos_grafica):
            tk.Label(self.grafica_frame, text=concepto).grid(row=i, column=0)
            self.entradas_tabla_derecha[concepto] = []
            for j in range(4):  # 4 columnas
                entry = tk.Entry(self.grafica_frame, width=10)
                entry.grid(row=i, column=j+1)
                self.entradas_tabla_derecha[concepto].append(entry)

    def calcular(self):
        # Cálculos y actualizaciones de las tablas
        try:
            precio = float(self.precio_var.get())
            costo_fijo = float(self.costo_fijo_var.get())
            costo_variable = float(self.costo_variable_var.get())

            margen_contribucion = precio - costo_variable
            self.margen_var.delete(0, tk.END)
            self.margen_var.insert(0, str(margen_contribucion))

            punto_equilibrio = costo_fijo / margen_contribucion
            self.pe_var.delete(0, tk.END)
            self.pe_var.insert(0, str(punto_equilibrio))

            # Actualizar tabla izquierda
            for i in range(4):
                self.entradas_tabla_izquierda["Ventas"][i].delete(0, tk.END)
                self.entradas_tabla_izquierda["Ventas"][i].insert(0, str(precio * (i + 1)))

                self.entradas_tabla_izquierda["Costos Variables"][i].delete(0, tk.END)
                self.entradas_tabla_izquierda["Costos Variables"][i].insert(0, str(costo_variable * (i + 1)))

                self.entradas_tabla_izquierda["Margen de Contribución"][i].delete(0, tk.END)
                self.entradas_tabla_izquierda["Margen de Contribución"][i].insert(0, str(margen_contribucion * (i + 1)))

                self.entradas_tabla_izquierda["Costos Fijos"][i].delete(0, tk.END)
                self.entradas_tabla_izquierda["Costos Fijos"][i].insert(0, str(costo_fijo))

                utilidad = (precio * (i + 1)) - (costo_variable * (i + 1)) - costo_fijo
                self.entradas_tabla_izquierda["Utilidad o Pérdida"][i].delete(0, tk.END)
                self.entradas_tabla_izquierda["Utilidad o Pérdida"][i].insert(0, str(utilidad))

            # Actualizar tabla derecha para la gráfica
            for i in range(4):
                self.entradas_tabla_derecha["Total de unidades"][i].delete(0, tk.END)
                self.entradas_tabla_derecha["Total de unidades"][i].insert(0, str(i + 1))

                self.entradas_tabla_derecha["Ingresos Totales"][i].delete(0, tk.END)
                self.entradas_tabla_derecha["Ingresos Totales"][i].insert(0, str(precio * (i + 1)))

                self.entradas_tabla_derecha["Costos Totales"][i].delete(0, tk.END)
                self.entradas_tabla_derecha["Costos Totales"][i].insert(0, str((costo_variable * (i + 1)) + costo_fijo))

                self.entradas_tabla_derecha["Costos Variables"][i].delete(0, tk.END)
                self.entradas_tabla_derecha["Costos Variables"][i].insert(0, str(costo_variable * (i + 1)))

                self.entradas_tabla_derecha["Costos Fijos"][i].delete(0, tk.END)
                self.entradas_tabla_derecha["Costos Fijos"][i].insert(0, str(costo_fijo))

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def graficar(self):
        try:
            # Crear una nueva ventana para la gráfica
            graph_window = tk.Toplevel(self.root)
            graph_window.title("Gráfica de Punto de Equilibrio")
            graph_window.geometry("600x400")  # Establecer tamaño inicial
            graph_window.minsize(400, 300)    # Establecer tamaño mínimo

            fig, ax = plt.subplots()

            unidades = list(range(1, 21))  # Ejemplo de 20 unidades
            precio = float(self.precio_var.get())
            costo_variable = float(self.costo_variable_var.get())
            costo_fijo = float(self.costo_fijo_var.get())

            ingresos_totales = [precio * u for u in unidades]
            costos_variables_totales = [costo_variable * u for u in unidades]
            costos_fijos_totales = [costo_fijo] * len(unidades)
            costos_totales = [costos_variables_totales[i] + costos_fijos_totales[i] for i in range(len(unidades))]

            # Graficar
            ax.plot(unidades, ingresos_totales, label="Ingresos Totales", color="blue")
            ax.plot(unidades, costos_totales, label="Costos Totales", color="red")
            ax.plot(unidades, costos_variables_totales, label="Costos Variables", color="orange")
            ax.plot(unidades, costos_fijos_totales, label="Costos Fijos", color="green")

            ax.set_xlabel('Unidades')
            ax.set_ylabel('Quetzales')
            ax.set_title('Punto de Equilibrio')
            ax.legend()

            canvas = FigureCanvasTkAgg(fig, master=graph_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except ValueError:
            messagebox.showerror("Error", "Asegúrate de ingresar valores correctos para graficar.")

    def borrar_datos(self):
        self.precio_var.delete(0, tk.END)
        self.costo_fijo_var.delete(0, tk.END)
        self.costo_variable_var.delete(0, tk.END)
        self.margen_var.delete(0, tk.END)
        self.pe_var.delete(0, tk.END)

        for concepto in self.entradas_tabla_izquierda:
            for entry in self.entradas_tabla_izquierda[concepto]:
                entry.delete(0, tk.END)

        for concepto in self.entradas_tabla_derecha:
            for entry in self.entradas_tabla_derecha[concepto]:
                entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PuntoEquilibrioApp(root)
    root.mainloop()

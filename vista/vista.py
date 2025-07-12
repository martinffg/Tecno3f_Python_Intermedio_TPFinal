import tkinter as tk
from tkinter import ttk, messagebox
import modelo.consultas_dao as consulta


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_peli = None
        self.fondo = "#FBFCDD"
        self.config(bg=self.fondo)  # se pueden usar clores hexa o el nombre

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=("Arial", 12, "bold"), bg="#FBFCDD", fg="#1931E8")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text="Duración: ")
        self.label_nombre.config(font=("Arial", 12, "bold"), bg="#FBFCDD", fg="#1931E8")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text="Género: ")
        self.label_nombre.config(font=("Arial", 12, "bold"), bg="#FBFCDD", fg="#1931E8")
        self.label_nombre.grid(row=2, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text="Año Estreno: ")
        self.label_nombre.config(font=("Arial", 12, "bold"), bg="#FBFCDD", fg="#1931E8")
        self.label_nombre.grid(row=3, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text="Director: ")
        self.label_nombre.config(font=("Arial", 12, "bold"), bg="#FBFCDD", fg="#1931E8")
        self.label_nombre.grid(row=4, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text="Estudio: ")
        self.label_nombre.config(font=("Arial", 12, "bold"), bg="#FBFCDD", fg="#1931E8")
        self.label_nombre.grid(row=5, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text="País del Film: ")
        self.label_nombre.config(font=("Arial", 12, "bold"), bg="#FBFCDD", fg="#1931E8")
        self.label_nombre.grid(row=6, column=0, padx=10, pady=10)

    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width=50, state="disabled")
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.duracion)
        self.entry_duracion.config(width=50, state="disabled")
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10)

        x_gen = consulta.listar_generos()
        y_gen = []
        for i in x_gen:
            y_gen.append(i[1])

        self.generos = ["Selecione Uno"] + y_gen
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero.config(width=25, state="disabled")
        self.entry_genero["values"] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10)

        self.anioEstreno = tk.StringVar()
        self.entry_anioEstreno = tk.Entry(self, textvariable=self.anioEstreno)
        self.entry_anioEstreno.config(width=50, state="disabled")
        self.entry_anioEstreno.grid(row=3, column=1, padx=10, pady=10)

        x_dir = consulta.listar_directores()
        y_dir = []
        for i in x_dir:
            y_dir.append(i[1])

        self.directores = ["Selecione Uno"] + y_dir
        self.entry_director = ttk.Combobox(self, state="readonly")
        self.entry_director.config(width=25, state="disabled")
        self.entry_director["values"] = self.directores
        self.entry_director.current(0)
        self.entry_director.bind("<<ComboboxSelected>>")
        self.entry_director.grid(row=4, column=1, padx=10, pady=10)

        x_est = consulta.listar_estudios()
        y_est = []
        for i in x_est:
            y_est.append(i[1])

        self.estudios = ["Selecione Uno"] + y_est
        self.entry_estudio = ttk.Combobox(self, state="readonly")
        self.entry_estudio.config(width=25, state="disabled")
        self.entry_estudio["values"] = self.estudios
        self.entry_estudio.current(0)
        self.entry_estudio.bind("<<ComboboxSelected>>")
        self.entry_estudio.grid(row=5, column=1, padx=10, pady=10)

        x_pais = consulta.listar_paises()
        y_pais = []
        for i in x_pais:
            y_pais.append(i[1])

        self.paises = ["Selecione Uno"] + y_pais
        self.entry_pais = ttk.Combobox(self, state="readonly")
        self.entry_pais.config(width=25, state="disabled")
        self.entry_pais["values"] = self.paises
        self.entry_pais.current(0)
        self.entry_pais.bind("<<ComboboxSelected>>")
        self.entry_pais.grid(row=6, column=1, padx=10, pady=10)

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.btn_alta.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#FFFFFF",
            bg="#1C500B",
            cursor="hand2",
            activebackground="#3FD83F",
            activeforeground="#000000",
        )
        self.btn_alta.grid(row=8, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text="Guardar", command=self.guardar_campos)
        self.btn_modi.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#FFFFFF",
            bg="#0D2A83",
            cursor="hand2",
            activebackground="#7594F5",
            activeforeground="#000000",
            state="disabled",
        )
        self.btn_modi.grid(row=8, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text="Cancelar", command=self.bloquear_campos)
        self.btn_cance.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#FFFFFF",
            bg="#A90A0A",
            cursor="hand2",
            activebackground="#F35B5B",
            activeforeground="#000000",
            state="disabled",
        )
        self.btn_cance.grid(row=8, column=2, padx=10, pady=10)

    def mostrar_tabla(self):

        self.lista_p = consulta.listar_peli()

        self.lista_p.reverse()

        self.tabla = ttk.Treeview(
            self,
            columns=(
                "Nombre",
                "Duracion",
                "Genero",
                "AnioEstreno",
                "Director",
                "Estudio",
                "Pais",
            ),
        )
        self.tabla.grid(row=9, column=0, columnspan=4, sticky="nse")

        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=9, column=8, sticky="nse")
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Duracion")
        self.tabla.heading("#3", text="Genero")
        self.tabla.heading("#4", text="Año")
        self.tabla.heading("#5", text="Director")
        self.tabla.heading("#6", text="Estudio")
        self.tabla.heading("#7", text="Pais")

        for p in self.lista_p:
            self.tabla.insert(
                "", 0, text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7])
            )

        self.btn_editar = tk.Button(self, text="Editar", command=self.editar_registro)
        self.btn_editar.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#FFFFFF",
            bg="#1C500B",
            cursor="hand2",
            activebackground="#3FD83F",
            activeforeground="#000000",
        )
        self.btn_editar.grid(row=10, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(self, text="Delete", command=self.eliminar_registro)
        self.btn_delete.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#FFFFFF",
            bg="#A90A0A",
            cursor="hand2",
            activebackground="#F35B5B",
            activeforeground="#000000",
        )
        self.btn_delete.grid(row=10, column=1, padx=10, pady=10)

    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())["text"]

            self.nombre_peli = self.tabla.item(self.tabla.selection())["values"][0]
            self.dura_peli = self.tabla.item(self.tabla.selection())["values"][1]
            self.gene_peli = self.tabla.item(self.tabla.selection())["values"][2]
            self.anio_peli = self.tabla.item(self.tabla.selection())["values"][3]
            self.dire_peli = self.tabla.item(self.tabla.selection())["values"][4]
            self.estu_peli = self.tabla.item(self.tabla.selection())["values"][5]
            self.pais_peli = self.tabla.item(self.tabla.selection())["values"][6]

            self.habilitar_campos()
            self.nombre.set(self.nombre_peli)
            self.duracion.set(self.dura_peli)
            self.entry_genero.current(self.generos.index(self.gene_peli))
            self.anioEstreno.set(self.anio_peli)
            self.entry_director.current(self.directores.index(self.dire_peli))
            self.entry_estudio.current(self.estudios.index(self.estu_peli))
            self.entry_pais.current(self.paises.index(self.pais_peli))

        except:
            pass

    def eliminar_registro(self):
        self.id_peli = self.tabla.item(self.tabla.selection())["text"]

        response = messagebox.askyesno("Confirmar", "Desea borrar el registro ?")

        if response:
            consulta.borrar_peli(int(self.id_peli))
        else:
            messagebox.showinfo("¡CUIDADO!", "POR POCO Y BORRAS ALGO EQUIVOCADO")

        self.id_peli = None
        self.mostrar_tabla()

    def guardar_campos(self):
        pelicula = consulta.Peliculas(
            self.nombre.get(),
            self.duracion.get(),
            self.entry_genero.current(),
            self.anioEstreno.get(),
            self.entry_director.current(),
            self.entry_estudio.current(),
            self.entry_pais.current(),
        )

        if self.id_peli == None:
            consulta.guardar_peli(pelicula)
        else:
            consulta.editar_peli(pelicula, int(self.id_peli))

        self.mostrar_tabla()
        self.bloquear_campos()

    def habilitar_campos(self):
        self.entry_nombre.config(state="normal")
        self.entry_duracion.config(state="normal")
        self.entry_genero.config(state="normal")
        self.entry_anioEstreno.config(state="normal")
        self.entry_director.config(state="normal")
        self.entry_estudio.config(state="normal")
        self.entry_pais.config(state="normal")
        self.btn_modi.config(state="normal")
        self.btn_cance.config(state="normal")
        self.btn_alta.config(state="disabled")

    def bloquear_campos(self):
        self.entry_nombre.config(state="disabled")
        self.entry_duracion.config(state="disabled")
        self.entry_genero.config(state="disabled")
        self.entry_anioEstreno.config(state="disabled")
        self.entry_director.config(state="disabled")
        self.entry_estudio.config(state="disabled")
        self.entry_pais.config(state="disabled")
        self.btn_modi.config(state="disabled")
        self.btn_cance.config(state="disabled")
        self.btn_alta.config(state="normal")
        self.nombre.set("")
        self.duracion.set("")
        self.entry_genero.current(0)
        self.anioEstreno.set("")
        self.entry_director.current(0)
        self.entry_estudio.current(0)
        self.entry_pais.current(0)
        self.id_peli = None

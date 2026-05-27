import customtkinter as ctk
import tkinter as tk
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from services.sheets.sheets_connection import sheet
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import pandas as pd

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ColfenixApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("COLFENIX APP")
        self.geometry("1700x950")
        self.minsize(1400, 850)

        self.frames = {}

        self.crear_layout()

    # =====================================================
    # LAYOUT PRINCIPAL
    # =====================================================

    def crear_layout(self):

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.crear_header()
        self.crear_sidebar()
        self.crear_contenedor()

        self.crear_dashboard()
        self.crear_captura()
        self.crear_datos()
        self.crear_logs()

        self.mostrar_vista("dashboard")

    # =====================================================
    # HEADER
    # =====================================================

    def crear_header(self):

        header = ctk.CTkFrame(
            self,
            height=70,
            corner_radius=0
        )

        header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        header.grid_columnconfigure(0, weight=1)

        titulo = ctk.CTkLabel(
            header,
            text="COLFENIX APP",
            font=ctk.CTkFont(size=28, weight="bold")
        )

        titulo.grid(
            row=0,
            column=0,
            padx=25,
            pady=15,
            sticky="w"
        )

        estado = ctk.CTkLabel(
            header,
            text="WhatsApp conectado",
            text_color="#4CAF50",
            font=ctk.CTkFont(size=14, weight="bold")
        )

        estado.grid(
            row=0,
            column=1,
            padx=20
        )

    # =====================================================
    # SIDEBAR
    # =====================================================

    def crear_sidebar(self):

        sidebar = ctk.CTkFrame(
            self,
            width=260,
            corner_radius=0
        )

        sidebar.grid(
            row=1,
            column=0,
            sticky="nsw"
        )

        sidebar.grid_rowconfigure(20, weight=1)

        logo = ctk.CTkLabel(
            sidebar,
            text="PANEL",
            font=ctk.CTkFont(size=30, weight="bold")
        )

        logo.grid(
            row=0,
            column=0,
            padx=20,
            pady=(30, 40)
        )

        botones = [
            ("Dashboard", "dashboard"),
            ("Captura WhatsApp", "captura"),
            ("Datos", "datos"),
            ("Logs", "logs")
        ]

        for i, (texto, frame) in enumerate(botones):

            btn = ctk.CTkButton(
                sidebar,
                text=texto,
                height=50,
                anchor="w",
                font=ctk.CTkFont(size=15, weight="bold"),
                command=lambda f=frame: self.mostrar_vista(f)
            )

            btn.grid(
                row=i + 1,
                column=0,
                padx=15,
                pady=8,
                sticky="ew"
            )

    # =====================================================
    # CONTENEDOR PRINCIPAL
    # =====================================================

    def crear_contenedor(self):

        self.container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.container.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    # =====================================================
    # CAMBIO DE VISTAS
    # =====================================================

    def mostrar_vista(self, nombre):

        for frame in self.frames.values():
            frame.grid_forget()

        self.frames[nombre].grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # =====================================================
    # DASHBOARD
    # =====================================================

    def crear_dashboard(self):

        frame = ctk.CTkFrame(self.container)

        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.frames["dashboard"] = frame

        titulo = ctk.CTkLabel(
            frame,
            text="Dashboard General",
            font=ctk.CTkFont(size=30, weight="bold")
        )

        titulo.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20, 10)
        )

        cards_frame = ctk.CTkFrame(frame)

        cards_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20
        )

        cards_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        mes_actual = datetime.now().strftime("%B %Y").capitalize()

        cards = [
            ("Mantenimientos Hoy", "24", "#1f538d"),
            (f"{mes_actual}", "482", "#2e7d32"),
            ("Pendientes", "5", "#ef6c00"),
            ("Errores", "1", "#c62828")
        ]

        for i, (titulo, valor, color) in enumerate(cards):

            self.crear_card(
                cards_frame,
                titulo,
                valor,
                color,
                i
            )

        resumen = ctk.CTkTextbox(
            frame,
            font=("Consolas", 14)
        )

        resumen.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=20
        )

        resumen.insert(
            "0.0",
            """
ESTADO GENERAL DEL SISTEMA

✔ WhatsApp conectado
✔ Captura activa
✔ IA funcionando
✔ Base de datos operativa

MANTENIMIENTOS RECIENTES

[14:20] MTTO móvil 4587
[14:22] Cambio DVR
[14:25] Instalación cámara lateral
"""
        )

    # =====================================================
    # CAPTURA WHATSAPP
    # =====================================================

    def crear_captura(self):

        frame = ctk.CTkFrame(self.container)

        frame.grid_columnconfigure(0, weight=2)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        self.frames["captura"] = frame

        titulo = ctk.CTkLabel(
            frame,
            text="Captura WhatsApp",
            font=ctk.CTkFont(size=28, weight="bold")
        )

        titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=20
        )

        # MENSAJES

        mensajes_frame = ctk.CTkFrame(frame)

        mensajes_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=(0, 20)
        )

        mensajes_frame.grid_rowconfigure(1, weight=1)
        mensajes_frame.grid_columnconfigure(0, weight=1)

        mensajes_label = ctk.CTkLabel(
            mensajes_frame,
            text="Mensajes Detectados",
            font=ctk.CTkFont(size=20, weight="bold")
        )

        mensajes_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=15
        )

        mensajes_box = ctk.CTkTextbox(
            mensajes_frame,
            font=("Consolas", 14)
        )

        mensajes_box.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=15,
            pady=(0, 15)
        )

        mensajes_box.insert(
            "0.0",
            """
[14:22]

MTTO móvil 4587 placa JKL210
Cambio disco DVR

-----------------------------------

[14:24]

Instalación cámara lateral
Vehículo 7821
"""
        )

        # PREVISUALIZACIÓN

        preview_frame = ctk.CTkFrame(frame)

        preview_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=(0, 20)
        )

        preview_label = ctk.CTkLabel(
            preview_frame,
            text="Previsualización",
            font=ctk.CTkFont(size=20, weight="bold")
        )

        preview_label.pack(
            anchor="w",
            padx=15,
            pady=15
        )

        campos = [
            ("VEH", "4587"),
            ("PLACA", "JKL210"),
            ("TIPO", "Mantenimiento"),
            ("TECNICO", "Juan"),
            ("TRABAJO", "Cambio DVR")
        ]

        for campo, valor in campos:

            fila = ctk.CTkFrame(preview_frame)

            fila.pack(
                fill="x",
                padx=15,
                pady=5
            )

            lbl1 = ctk.CTkLabel(
                fila,
                text=campo,
                width=120,
                font=ctk.CTkFont(weight="bold")
            )

            lbl1.pack(
                side="left",
                padx=10,
                pady=10
            )

            lbl2 = ctk.CTkLabel(
                fila,
                text=valor
            )

            lbl2.pack(
                side="left"
            )

        botones = ctk.CTkFrame(
            preview_frame,
            fg_color="transparent"
        )

        botones.pack(
            pady=20
        )

        ctk.CTkButton(
            botones,
            text="Guardar",
            fg_color="#2e7d32"
        ).grid(row=0, column=0, padx=5)

        ctk.CTkButton(
            botones,
            text="Editar"
        ).grid(row=0, column=1, padx=5)

        ctk.CTkButton(
            botones,
            text="Descartar",
            fg_color="#c62828"
        ).grid(row=0, column=2, padx=5)

    # =====================================================
    # DATOS
    # =====================================================

    def crear_datos(self):

        frame = ctk.CTkFrame(self.container)

        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.frames["datos"] = frame

        titulo = ctk.CTkLabel(
            frame,
            text="Base de Datos de Mantenimientos",
            font=ctk.CTkFont(size=28, weight="bold")
        )

        titulo.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20, 10)
        )

        top = ctk.CTkFrame(frame)

        top.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 10)
        )

        top.grid_columnconfigure(0, weight=1)

        buscar = ctk.CTkEntry(
            top,
            placeholder_text="Buscar mantenimiento..."
        )

        buscar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=10,
            pady=10
        )

        btn_refrescar = ctk.CTkButton(
            top,
            text="Refrescar",
            command=self.cargar_datos_sheets
        )

        btn_refrescar.grid(
            row=0,
            column=1,
            padx=5
        )

        exportar = ctk.CTkButton(
            top,
            text="Exportar Excel",
            fg_color="#2e7d32",
            command=self.exportar_excel
        )

        exportar.grid(
            row=0,
            column=2,
            padx=10
        )

        # =================================================
        # TABLA
        # =================================================

        table_frame = tk.Frame(frame)

        table_frame.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # =================================================
        # LEER GOOGLE SHEETS
        # =================================================

        if sheet is None:
            encabezados = ["ID", "Nombre", "Valor", "Fecha"]  # Encabezados por defecto
        else:
            encabezados = sheet.row_values(1)

        self.tabla = ttk.Treeview(
            table_frame,
            columns=encabezados,
            show="headings"
        )

        for col in encabezados:

            self.tabla.heading(
                col,
                text=col
            )

            self.tabla.column(
                col,
                width=180,
                anchor="center"
            )

        scroll_y = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tabla.yview
        )

        scroll_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tabla.xview
        )

        self.tabla.configure(
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        self.tabla.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scroll_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scroll_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.cargar_datos_sheets()
    # =====================================================
    # LOGS
    # =====================================================

    def crear_logs(self):

        frame = ctk.CTkFrame(self.container)

        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.frames["logs"] = frame

        titulo = ctk.CTkLabel(
            frame,
            text="Logs del Sistema",
            font=ctk.CTkFont(size=28, weight="bold")
        )

        titulo.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=20
        )

        logs = ctk.CTkTextbox(
            frame,
            font=("Consolas", 13)
        )

        logs.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        logs.insert(
            "0.0",
            """
[14:20] WhatsApp conectado
[14:21] Captura iniciada
[14:22] Mensaje detectado
[14:22] Regex placa OK
[14:22] IA clasificó mantenimiento
[14:23] Registro guardado
[14:25] Exportación Excel completada
"""
        )

    # =====================================================
    # CARD
    # =====================================================

    def crear_card(self, parent, titulo, valor, color, columna):

        card = ctk.CTkFrame(
            parent,
            fg_color=color,
            height=120,
            corner_radius=15
        )

        card.grid(
            row=0,
            column=columna,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        titulo_lbl = ctk.CTkLabel(
            card,
            text=titulo,
            font=ctk.CTkFont(size=16)
        )

        titulo_lbl.pack(
            anchor="nw",
            padx=15,
            pady=(15, 5)
        )

        valor_lbl = ctk.CTkLabel(
            card,
            text=valor,
            font=ctk.CTkFont(size=36, weight="bold")
        )

        valor_lbl.pack(
            expand=True
        )

    # =====================================================
    # EXPORTAR EXCEL
    # =====================================================

    def exportar_excel(self):

        datos = []

        for item in self.tabla.get_children():
            datos.append(self.tabla.item(item)["values"])

        columnas = self.tabla["columns"]

        df = pd.DataFrame(
            datos,
            columns=columnas
        )

        archivo = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel", "*.xlsx")]
        )

        if archivo:

            try:

                df.to_excel(
                    archivo,
                    index=False
                )

                messagebox.showinfo(
                    "Exportación",
                    "Excel exportado correctamente"
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

    # =====================================================
    # CARGAR DATOS DESDE GOOGLE SHEETS
    # =====================================================

    def cargar_datos_sheets(self):
        """Recarga los datos de la tabla desde Google Sheets."""
        try:
            # Limpiar tabla existente
            for item in self.tabla.get_children():
                self.tabla.delete(item)
            
            # Importar función para obtener datos
            from services.sheets.sheets_reader import obtener_datos
            datos = obtener_datos()
            
            # Insertar datos en tabla
            for fila in datos:
                self.tabla.insert("", "end", values=fila)
            
            messagebox.showinfo("Éxito", "Datos recargados correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar datos: {str(e)}")


if __name__ == "__main__":

    app = ColfenixApp()
    app.mainloop()
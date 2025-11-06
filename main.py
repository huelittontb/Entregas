from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from entregas import SistemaEntregas


class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sistema = SistemaEntregas()

    def adicionar_entrega(self):
        self.sistema.adicionar_entrega()
        self.mostrar_popup("Entrega adicionada com sucesso.")

    def listar_entregas(self):
        resultado = self.sistema.listar_entregas()
        self.mostrar_popup(resultado)

    def listar_bairros(self):
        resultado = self.sistema.listar_bairros()
        self.mostrar_popup(resultado)

    def gerar_relatorio(self):
        resultado = self.sistema.gerar_relatorio_diario()
        self.mostrar_popup(resultado)

    def mostrar_popup(self, texto):
        layout = BoxLayout(orientation="vertical")
        scroll = ScrollView(size_hint=(1, 0.8))
        label = Label(text=texto, size_hint_y=None)
        label.bind(texture_size=label.setter("size"))
        scroll.add_widget(label)
        layout.add_widget(scroll)
        fechar = Label(text="\nToque fora para fechar", size_hint_y=0.2)
        layout.add_widget(fechar)
        popup = Popup(title="Resultado", content=layout, size_hint=(0.9, 0.9))
        popup.open()


class EntregasApp(App):
    def build(self):
        return Menu()


if __name__ == "__main__":
    EntregasApp().run()


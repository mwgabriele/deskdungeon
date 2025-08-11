from textual.app import ComposeResult
from textual.widgets import (
    Header, Footer, Label, Input, Static,
    Button, Select, ListItem
)
from textual.screen import Screen
from textual.containers import VerticalGroup
from textual.binding import Binding
from ddmodel import *

class TelaInicial(Screen):

    CSS = """
    #game_title {
        color: magenta;
    }

    Static {
        content-align: center middle;        
        color: cyan;        
    }

    VerticalGroup {
        align: center middle;
        height: 100%;
    }
"""

    def compose(self) -> ComposeResult:
        yield Header()

        yield VerticalGroup(
            Static("𝕯𝖊𝖘𝕶 𝕯𝖚𝖓𝖌𝖊𝖔𝖓", id="game_title"),
            Static(),
            Static("𝓾𝓶 𝓭𝓾𝓷𝓰𝓮𝓸𝓷 𝓬𝓻𝓪𝔀𝓵𝓮𝓻"),
            Static("𝓮𝓶 𝓶𝓸𝓭𝓸 𝓽𝓮𝔁𝓽𝓸")
        )        
        yield Footer()
    
    def on_screen_resume(self):
        if not JOGADOR.nome == "sem nome":
            self.sub_title = f"({JOGADOR.nome})"

class TelaNovoJogador(Screen):

    CSS = '''
    Static {
        content-align: center middle;
        color: cyan;
        padding: 1;
    }
'''
    BINDINGS = [
        Binding("ctrl+s", "salvar", "Salvar"),
    ]

    def compose(self):
        yield Header()
        yield Static("𝕹𝖔𝖛𝖔 𝕵𝖔𝖌𝖆𝖉𝖔𝖗")
        yield Label("Nome")
        yield Input(id="tx_nome")
        yield Label("Classe")   
        yield Select([
            ("Mago", "mago"),
            ("Cavaleiro", "cavaleiro"),
            ("Assassina", "assassina")], id="sl_classe")
        yield Footer()

    def action_salvar(self):
        nome = self.query_one("#tx_nome",Input).value
        classe = self.query_one("#sl_classe", Select).value
        # Atualizamos a model
        JOGADOR.nome = nome
        JOGADOR.classe = classe
        self.notify("Jogador salvo")
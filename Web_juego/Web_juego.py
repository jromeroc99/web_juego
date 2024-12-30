"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from Web_juego.views.body import *
from Web_juego.views.navbar import navbar
from Web_juego.components.cartas import cartas
from Web_juego.components.link_button import link_button
from Web_juego.estilos.tema import Tema
from Web_juego.views.footer import footer



class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:    
    return rx.vstack(
        navbar(),
        cabecera(),
        cartas(),
        como_se_juega(),
        Dominium_mundi(),
        footer(),
        width="100%",
        align_items="center",

    ),


app = rx.App(theme=Tema)
app.add_page(index)

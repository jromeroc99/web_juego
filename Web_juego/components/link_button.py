import reflex as rx

def link_button(Titulo: str, url: str):
    return rx.link(
        rx.button(Titulo),
        href=url,
        is_external=True,
    ),
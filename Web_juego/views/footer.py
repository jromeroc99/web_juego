import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/logoJuego.png", height="150px"),
        rx.link(
            rx.box(
                f"© 2023-{datetime.date.today().year} ",
                rx.text(
                    "Javier Romero Caparrós",
                    as_="span",
                    color="orange"
                ),
            ),
            href="https://sites.google.com/lasuncionmalaga.com/geh-games/inicio",
            is_external=True,

        ),
        rx.link(
            rx.text("CREADO CON ♥ PARA DIVERTIRSE APRENDIENDO"),
            href="https://sites.google.com/lasuncionmalaga.com/geh-games/inicio",
            is_external=True
        ),
        align="center",
        color="orange"
    )
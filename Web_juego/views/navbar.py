import reflex as rx

def navbar() -> rx.Component:
    return rx.flex(
        rx.image(src="/logoJuego.png", height="75px"),
        rx.heading("GEH GAMES", size="7"),
        rx.badge(
            "2024-2025 curso",
            radius="full",
            align="center",
            color_scheme="orange",
            variant="surface",
        ),
        rx.link(
            rx.text("Enlace web original"),
            href="https://sites.google.com/lasuncionmalaga.com/geh-games/inicio",
            is_external=True,
        ),
        rx.color_mode.button(),
        spacing="2",
        flex_direction="row",
        bg=rx.color("orange", 4),
        align="center",
        position="sticky",
        width="100%",
        top="0px",
        z_index="999",

    )

def navbares():
    return rx.flex(
        rx.hstack(
            rx.image(src="/logoJuego.png", height="75px"),
            rx.heading("GEH GAMES", size="7"),
            rx.badge(
                "2024-2025 curso",
                radius="full",
                align="center",
                color_scheme="orange",
                variant="surface",
            ),
            align="center", # alinea los elementos que esten a la misma altura
            bg=rx.color("orange", 4),
            
        ),
        rx.spacer(),
        rx.hstack(
            rx.color_mode.button(),
            align="center",
            spacing="3",
        ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        bg=rx.color("orange", 4),
        align="center",
        position="sticky",
        width="100%",
        top="0px",
    )
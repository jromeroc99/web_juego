import reflex as rx

def carta(Title: str,SubTitle: str, SRC: str,Tam,URL):
     return rx.flex(
        rx.card(
                rx.link(
                    rx.vstack(
                        rx.image(src=SRC, height=Tam),
                        rx.heading(Title),
                        rx.text(SubTitle),
                        align="center",
                        spacing="2",
                    ),
                    
                    href=URL,
                    is_external=True,
                ),
                #as_child=True,
                size="5"
        ),
        justify="center",


     )
def cartas():
    return rx.flex(
        carta("Cartas","Aquí podras ver tus cartas","/carta.png","200px","https://sites.google.com/lasuncionmalaga.com/geh-games/inicio/cartas-y-objetos?authuser=0"),
        carta("Mercado","Compra nuevas cartas","/mercado.png","200px","https://sites.google.com/lasuncionmalaga.com/geh-games/inicio/compras-mercado?authuser=0"),
        carta("Ranking","Consulta tu posición","/logoJuego.png","200px","https://sites.google.com/lasuncionmalaga.com/geh-games/inicio/ranking?authuser=0"),
        spacing="2",
        align_items="flex-start",
        align="center",
        justify="center",
        flex_wrap="wrap",
        width="80%"
    )
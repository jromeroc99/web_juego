import reflex as rx

from Web_juego.components.link_button import *
from Web_juego.components.cartas import *

def cabecera():
    return rx.flex(
        rx.heading("¡Bienvenido a GEH GAMES!", align="center" ,size="7"),
        rx.text("Si has llegado a esta web, es porque participas en GEH GAMES. Un juego para aprender y divertirte con tus compañeros de clase de la Asignatura de GEOGRAFÍA E HISTORIA."),
        rx.text("No es un juego para competir con tus compañeros, es un juego para ponerte metas y superarte a ti mismo. No hay ni mejores ni peores. Solo tú, tu trabajo y tu esfuerzo."),
        rx.text("Tus profesores son tus GAME MASTER, ellos te guiarán en el juego.  Recuerda, son MAGOS TODOPODEROSOS, no los enfades."),
        rx.text("Escoge algunas de las opciones que tienes debajo para continuar..."),
        rx.text("¡¡¡¡¡Qué tengas buena suerte en el juego!!!"),
        direction="column",
        spacing="3",
        width="80%",
        
        
    )

def como_se_juega():
    return rx.flex(
        rx.heading("¿COMO SE JUEGA?", align="center" ,size="7"),
        rx.text("Es bastante sencillo, debes ir completando las tareas que se te vayan pidiendo en el día a día de clase, estas tareas serán calificadas con notas de 1 a 10. Estas notas tienen una equivalencia en puntos de experiencia y monedas. Cuanta más alta es la nota mas PUNTOS DE EXPERIENCIA y MONEDAS. Sencillo, ¿verdad?."),
        rx.text("Estos PUNTOS DE EXPERIENCIA y MONEDAS, se irán acumulando en la ficha personal de cada ALUMNO (AVATAR), esta ficha y los datos que contienen son secretos, solo tú lo conoces. Lo único que es público son tus puntos de experiencia para el Ranking."),
        rx.text('Los PUNTOS DE EXPERIENCIA solo suman, nunca se restan, salvo que hagas trampas en el juego. Las MONEDAS sirven para comprar CARTAS, las cuales te darán ciertas "ventajas" en tu día a día, pero cuidado, las CARTAS sólo tienen un único uso y el número de las mismas es limitado, úsalas sabiamente. '),
        carta("Instrucciones","Aprende a jugar","/pergamino.jpg","250px","https://sites.google.com/lasuncionmalaga.com/geh-games/inicio/instrucciones?authuser=0"),
        direction="column",
        spacing="3",
        width="80%",
        
    )

def Dominium_mundi():
    return rx.flex(
        rx.heading("DOMINIUM MUNDI", align="center" ,size="7"),
        carta("DOMINIUM MUNDI","Proximamente...","/Domini.png","400px","https://sites.google.com/lasuncionmalaga.com/geh-games/inicio?authuser=0"),
        direction="column",
        spacing="3",
        width="80%",
        
    )
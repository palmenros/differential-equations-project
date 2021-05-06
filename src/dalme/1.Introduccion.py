from manim import *


class EDScene(Scene):

    def construct(self):
        title = TextMobject("Juegos")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1/1.5)
        )

        l = BulletedList(r"Al menos dos jugadores involucrados", "Diferentes estrategias disponibles", "Las estrategias determinan el resultado del juego", "Cada resultado lleva asociado un payoff o pago")

        self.play(
            Write(l[0])
        )

        self.wait(3)
        self.play(
            Write(l[1])
        )

        self.wait(3)
        self.play(
            Write(l[2])
        )

        self.wait(3)

        self.play(
            Write(l[3])
        )
        self.wait(3)

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )

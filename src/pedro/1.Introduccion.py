from manim import *


class EDScene(Scene):

    def construct(self):
        title = TextMobject("Sección 2: Teoría de juegos evolutiva")
        title.scale(1.5)
        title.set_color(BLUE)
        title.move_to([0, 0, 0])

        self.play(
            Write(title)
        )

        self.wait(3)

        self.play(
            title.animate.to_edge(UP)
        )

        l = BulletedList(r"Teoría de juegos aplicada a poblaciones que evolucionan", "Dinámica de las estrategias", "Modelado con ecuaciones diferenciales")

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
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
from manim import *


class EDScene(Scene):

    def construct(self):
        title = TextMobject("Sección 1: Teoría de juegos")
        title.scale(1.5)
        title.set_color(BLUE)
        title.move_to([0, 0, 0])

        self.play(
            Write(title)
        )

        self.wait(3)

#        self.play(
#            title.animate.to_edge(UP)
#        )

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )

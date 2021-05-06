from manim import *
import requests


class EDScene(Scene):

    def construct(self):
        title = TextMobject("Halcones y Palomas")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(8)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1/1.5)
        )

        Dove = SVGMobject("Dove.svg", height=1, width=2)
        Dove.init_colors(self);
        Dove.set_x(1)
        Dove.set_y(0)

        Hawk = SVGMobject("Hawk.svg", height=1, width=2)
        Hawk.init_colors(self);

        self.play(
          FadeIn(Dove)
        )

        #Dove.generate_target()
        #Dove.target.shift(3*LEFT)
        #self.play(
        #  MoveToTarget(Dove)
        #)

        Hawk.set_x(-1)
        Hawk.set_y(0)


        self.play(
          FadeIn(Hawk)
        )

        self.wait(7)

        Dove.generate_target()
        Dove.target.shift(LEFT)
        #Dove.shift(3*RIGHT)

#        Hawk.save_state()

        self.play(
          MoveToTarget(Dove),
          #ScaleInPlace(Dove, 2),
          FadeOut(Hawk)
        )

        self.play(ScaleInPlace(Dove,2))

        self.wait(4)

        self.play(ScaleInPlace(Dove, 0.5),
        Transform(Dove, Hawk))

        self.play(ScaleInPlace(Hawk, 2))

        self.wait(7)

        self.play(
          ScaleInPlace(Hawk, 0.5)
        )

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )

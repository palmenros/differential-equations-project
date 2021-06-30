from manim import *


class EDScene(Scene):

    def construct(self):
        title = Tex("Créditos")
        title.scale(1.5)
        title.set_color(BLUE)

        self.play(
            Write(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP).scale(1/1.5)
        )
        tAut = Tex("Autores").shift(2.5*UP).set_color("#95FC05")
        tMGA = Tex("Martín Gómez Abejón").shift(2*UP)
        tDMG = Tex("Daniel Martín Gómez").shift(1.5*UP)
        tPPA = Tex("Pedro Palacios Almendros").shift(1*UP)
        tHer = Tex("Herramienta de edición de vídeo").shift(0*UP).set_color("#95FC05")
        banner = ManimBanner().scale(0.3).shift(-1*UP)
        tMan = Tex("y sus librerías").shift(-2*UP)
        tMus = Tex("Música").shift(-3*UP).set_color("#95FC05")
        uVR  = Tex("Vincent Rubinetti").shift(-3.5*UP)
        self.play(FadeIn(tAut),FadeIn(tMGA),FadeIn(tDMG),FadeIn(tPPA))
        self.play(FadeIn(tHer),FadeIn(banner),FadeIn(tMan))
        self.play(FadeIn(tMus),FadeIn(uVR))
        self.play(banner.expand())
        self.play(ApplyMethod(banner.shift,0.9*RIGHT))
        self.wait(5)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
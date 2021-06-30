from manim import *


class EDScene(Scene):

    def construct(self):
        title = Tex("Ecuaciones generalizadas de Lotka-Volterra")
        title.scale(1.4)
        
        self.play(
            Write(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP).scale(1/1.4)
        )

        l = BulletedList(r"Generalización del modelo depredador-presa", "$n$ especies, modelo apto para competición", "Relacionado con replicador, trabajaremos solo con $A$", "No apto para comportamientos no lineales o mutualismo").shift(UP*0.5)

        self.play(
            Write(l[0]),Write(l[1]),Write(l[2]),Write(l[3])
        )
        self.wait(2)
        f = MathTex("y'_i=y_i\\left( r_i+\\sum_{j=1}^{n} b_{ij}y_j \\right)\\text{, los parámetros son }B\\text{ y }\\vec{r}").move_to(title).shift(DOWN*5.7)
        self.play(
            Write(f)
        )
        self.wait(35)
        title2 = Tex("Cambio de variables Lotka-Volterra / replicador").to_edge(UP)
        LV = MathTex("y'_i=y_i\\left( r_i+\\sum_{j=1}^{n} b_{ij}y_j \\right)").shift(2*UP).set_color(BLUE)
        self.play(
            FadeOut(l),ReplacementTransform(title,title2),ReplacementTransform(f,LV)
        )

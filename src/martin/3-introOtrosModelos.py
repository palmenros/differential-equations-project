from manim import *


class EDScene(Scene):

    def construct(self):
        title = Tex("Introducción a modelos más complejos")
        title.scale(1.4)
        
        self.play(
            Write(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP).scale(1/1.4)
        )

        l = BulletedList("Propagación por imitación, no por herencia", "\\[x_i\'=x_i\\sum_{j=1}^p [f_{ij}(\\vec{x})-f_{ji}(\\vec{x})]x_j\\]", "$f$ lineales es la ecuación del replicador", "Caso muy general: $x_i\'=x_ig_i(\\vec{x}),g_i \\in \\mathcal{C}^1,\\sum_{i=1}^p x_i g_i(\\vec{x})=0 $", "Las dinámicas {\\itshape payoff monotonic } tienen propiedades\\\\de equilibrio similares al replicador").shift(DOWN*0.5)

        self.play(
            Write(l[0]),Write(l[1])
        )
        self.wait(10)
        self.play(Write(l[2]))
        self.wait(10)
        self.play(Write(l[3]))
        self.wait(20)
        self.play(Write(l[4]))
        self.wait(20)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )

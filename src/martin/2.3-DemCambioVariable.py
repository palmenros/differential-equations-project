from manim import *


class EDScene(Scene):

    def construct(self):
        
        title = Tex("Demostración del cambio de variables").scale(1.4)
        self.play(
            Write(title)
        )

        

        self.play(
            title.animate.to_edge(UP).scale(1/1.4)
        )
        #Demostraciones "#8F79FC"
        
        F0 = Tex("\\[x_i\'=x_i[(A\\vec{x})_i- \\vec{x} \\cdot A\\vec{x}]\\]").shift(2*UP).set_color("#8F79FC")
        F1 = Tex("\\[x_i\'=x_i\\left[\\sum_{j=1}^pa_{ij}x_j- \\vec{x} \\cdot A\\vec{x}\\right]\\]").shift(0*UP).set_color("#8F79FC")
        F1b = Tex("\\[-x_p\'=-x_p\\left[\\sum_{j=1}^pa_{pj}x_j- \\vec{x} \\cdot A\\vec{x}\\right]\\]").shift(-2*UP).set_color("#8F79FC")

        
        
        self.play(Write(F0))
        
        self.play(ReplacementTransform(F0.copy(),F1))
        
        self.play(FadeOut(F0),ReplacementTransform(F1.copy(),F1b))
        self.wait(1)
        self.play(ApplyMethod(F1.shift,2*UP))
        F2 = Tex("\\[x_i\'x_p=x_ix_p\\left[\\sum_{j=1}^pa_{ij}x_j- \\vec{x} \\cdot A\\vec{x}\\right]\\]").shift(0*UP).set_color("#8F79FC")
        F2b = Tex("\\[-x_ix_p\'=-x_ix_p\\left[\\sum_{j=1}^pa_{pj}x_j- \\vec{x} \\cdot A\\vec{x}\\right]\\]").shift(-2*UP).set_color("#8F79FC")
        self.play(ReplacementTransform(F1.copy(),F2))
        self.play(FadeOut(F1))
        self.play(ApplyMethod(F2.shift,2*UP),ApplyMethod(F1b.shift,2*UP))
        self.play(ReplacementTransform(F1b.copy(),F2b))
        self.play(FadeOut(F1b))
        self.play(ApplyMethod(F2b.shift,2*UP))
        F3 = Tex("\\[x_i\'x_p-x_ix_p\'=x_ix_p\\left[\\sum_{j=1}^pa_{ij}x_j-\\sum_{j=1}^pa_{pj}x_j\\right]\\]").shift(-2*UP).set_color("#8F79FC")
        cF3 = F3.copy()
        self.play(ReplacementTransform(F2.copy(),F3),ReplacementTransform(F2b.copy(),cF3))
        self.remove(cF3)
        self.wait(1)
        self.play(FadeOut(F2),FadeOut(F2b))
        self.play(ApplyMethod(F3.shift,4*UP))
        F4 = Tex("\\[\\frac{x_i\'x_p-x_ix_p\'}{x_p^2 \\cdot x_p}=\\frac{x_i}{x_p}\\left[\\sum_{j=1}^pa_{ij}\\frac{x_j}{x_p}-\\sum_{j=1}^pa_{pj}\\frac{x_j}{x_p}\\right]\\]").shift(0*UP).set_color("#8F79FC")
        F5 = Tex("\\[\\frac{y_i\'}{x_p}=y_i\\left[\\sum_{j=1}^{p-1}a_{ij}\\frac{x_j}{x_p}+a_{ip}-\\sum_{j=1}^{p-1}a_{pj}\\frac{x_j}{x_p}-a_{pp}\\right]\\]").shift(-2*UP).set_color("#8F79FC")
        self.play(ReplacementTransform(F3.copy(),F4))
        self.wait(1)
        self.play(ReplacementTransform(F4.copy(),F5))
        self.wait(3)
        self.play(FadeOut(F3),FadeOut(F4))
        self.play(ApplyMethod(F5.shift,4*UP))
        F6 = Tex("\\[\\frac{y_i\'}{x_p}=y_i\\left[(a_{ip}-a_{pp})+\\sum_{j=1}^{p-1}(a_{ij}-a_{pj})y_j\\right]\\]").shift(0*UP).set_color("#8F79FC")
        self.play(ReplacementTransform(F5.copy(),F6))
        F7 = Tex("\\[r_i = a_{ip}-a_{pp},b_{ij}=a_{ij}-a_{nj}\\text{, deformación del tiempo}\\]").set_color("#BBFFBB").shift(-2*UP)
        self.play(FadeIn(F7))
        self.wait(5)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )

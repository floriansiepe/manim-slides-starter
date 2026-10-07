from manim import *

from manim_slides import Slide


class BasicExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_slide()  # Waits user to press continue to go to the next slide

        self.next_slide(loop=True)  # Start loop
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()  # This will start a new non-looping slide

        self.play(dot.animate.move_to(ORIGIN))


class AnotherExample(Slide):
    def construct(self):
        square = Square(color=RED)
        self.play(FadeIn(square))
        self.next_slide()
        self.play(square.animate.rotate(PI / 4))
        self.play(FadeIn(Tex("Rotate by $\\frac{\\pi}{4}$").next_to(square, DOWN, buff=1.5)))
        self.next_slide()
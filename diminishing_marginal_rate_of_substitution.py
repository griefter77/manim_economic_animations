from manim import*

class Slide23Micro22(Scene):
	def construct(self):

		ax= Axes(x_range=[0,15,3], y_range=[0,15,3],
			x_length=7, y_length=7,
			axis_config={"include_tip": False, "include_ticks":False}
			)


		k2=35

		def func(x):
			return k2/x

		graph= ax.plot(func,color=RED_E, x_range=[2.5,13])
		graph_label= ax.get_graph_label(graph, MathTex('U_{1}'), x_val=14)

		x= ValueTracker(4)
		dy= ValueTracker(4)

		slope= always_redraw(lambda: ax.get_secant_slope_group(
			x= x.get_value(),
			dx= -1,
			dx_label= Tex('1').shift(DOWN*1),
			dy_label= DecimalNumber(dy.get_value(), num_decimal_places=0),
			dy_line_color=BLUE_D,
			graph= graph,
			secant_line_length=0.001,
			secant_line_color=YELLOW)
		)

		slope1= always_redraw(lambda: ax.get_secant_slope_group(
			x= 4,
			dx= -1,
			dx_label= 1,
			dy_label=4,
			dy_line_color=BLUE_D,
			graph= graph,
			secant_line_length=0.001,
			secant_line_color=YELLOW)
		)

		slope2= always_redraw(lambda: ax.get_secant_slope_group(
			x= 6,
			dx= -1,
			dx_label= 1,
			dy_label= 2,
			dy_line_color=BLUE_D,
			graph= graph,
			secant_line_length=0.001,
			secant_line_color=YELLOW)
		)

		self.add(ax, graph, graph_label)
		self.wait(1)

		self.play(Create(slope))
		self.wait(1.5)
		self.play(x.animate.set_value(6), dy.animate.set_value(2),run_time=2)
		self.play(Create(slope1))


		self.wait(1.5)

		self.play(x.animate.set_value(10), dy.animate.set_value(0.25),run_time=2)
		self.wait(0.5)
		self.play(Create(slope2))
		self.wait(2)




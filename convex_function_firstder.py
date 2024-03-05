from manim import*



class Derivative(Scene):
	def construct(self):

		#defining value tracker
		x=ValueTracker(0.3)
		dx=ValueTracker(0.8)


		#plane 1
		#root= 0.9735, 1.215
		ax= Axes(x_range=[-0.5, 4, 2.05882], x_length=7.5, tips=False,
				y_range=[-0.5, 5, 2], y_length=3).shift(LEFT*3.5)

		graph= ax.plot(lambda x: 3.5*x -0.85* x**2, x_range=[0.3,3.8],
						color=RED_C
		)

		graph_lab = (
            MathTex("f(x)=3.5x-0.85x^2")
            .set(width=4)
            .next_to(graph, UP, buff=1.3)
            .set_color(RED_C)
        )

		slope= always_redraw(lambda: ax.get_secant_slope_group(
			x= x.get_value(),
			dx= dx.get_value(),
			dx_label= DecimalNumber(dx.get_value()),
			dy_label='dy',
			dy_line_color=BLUE_D,
			graph= graph,
			secant_line_length=3,
			secant_line_color=YELLOW)
		)

		t_label = always_redraw(lambda: ax.get_T_label(x_val=x.get_value(), graph=graph, label=DecimalNumber(x.get_value())))

		dot_1= always_redraw( lambda:
			Dot(color=GREEN).
			scale(1.2).
			move_to(ax.c2p(x.get_value(), graph.underlying_function(x.get_value() )))
			)

		dot_2= always_redraw( lambda:
			Dot(color=GREEN).
			scale(1.2).
			move_to(ax.c2p(dx.get_value() + x.get_value(), 
			graph.underlying_function(x.get_value() + dx.get_value() )))
			)

		#end of plane 1

		#plane 2
		ax2= Axes(x_range=[-1, 4, 1], x_length=5, tips=False,
				 y_range=[-4, 3, 2], y_length=5).shift(RIGHT*4)

		graph2= always_redraw(lambda: 
				ax2.plot(lambda x: 3.5-1.7*x, x_range=[0.3, x.get_value()], 
					color=YELLOW)
		)

		graph2_lab = (
            MathTex("f'(x)=3.5-1.7x")
            .set(width=3)
            .next_to(ax2, UP, buff=0.5)
            .set_color(YELLOW)
        )

		point2_1= ax2.c2p(0.35,2.9)
		point2_2= ax2.c2p(3.8,-2.9)
		point2_3= ax2.c2p(2.06, 0)


		dot2_1 = Dot(point2_1)
		dot2_1_lab= Text('(0.30, 3)',font_size=25).next_to(dot2_1, RIGHT, buff=0.1)

		dot2_2 = Dot(point2_2)
		dot2_2_lab= Text('(3.8, -3)',font_size=25).next_to(dot2_2, LEFT, buff=0.1)

		dot2_3 = Dot(point2_3, color=RED)
		dot2_3_lab= Text('(2.06, 0)',font_size=25, color=RED).next_to(dot2_3, UR, buff=0.1)




		#end of plane 2
			
		#slope value stuff
		slope_value_text = (
            Tex("Slope Value: ")
            .next_to(ax, DOWN, buff=1.2)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

		slope_value = always_redraw(
        	lambda:DecimalNumber(num_decimal_places=1).
        	set_value(graph2.underlying_function(x.get_value())).
        	next_to(slope_value_text, RIGHT, buff=0.2).
        	set_color(YELLOW)).add_background_rectangle()
       	


		#animation
		#drawing the first axes
		self.play(Create(ax))

		#drwaing the main concave function
		self.play(Create(graph), Create(graph_lab))
		
		#drawing the slope
		self.play(Create(dot_1), Create(dot_2))
		self.wait(1)
		self.play(Create(slope), run_time=2)

		#drawing tangent line
		self.play(dx.animate.set_value(0.001), run_time=3)

		#showing slope value
		self.play(Create(slope_value_text), Create(slope_value))

		#showing t_label
		self.play(Create(t_label))
		self.wait(2)

		#showing second derivative plane
		self.play(Create(ax2))
		self.play(Create(graph2_lab))
		self.wait(3)

		#showing first second plane dot
		self.play(Create(dot2_1), Create(dot2_1_lab))
		self.wait(3)

		#showing function of the derivative
		self.add(graph2)

		#wiggle to get audience attention back
		self.play(Wiggle(t_label), run_time=2)

		#showing stationary point
		self.play(x.animate.set_value(2.05882), run_time=4)
		self.wait(1.5)

		#showing dot on second plane for stationary point
		self.play(Create(dot2_3), Create(dot2_3_lab))
		self.wait(2)

		#showing the end of the first function
		self.play(x.animate.set_value(3.8), run_time=3)

		#showing second second plane dot
		self.play(Create(dot2_2), Create(dot2_2_lab))
		self.wait(3)




		

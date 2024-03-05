from manim import *

class Elasticity(Scene):
	def construct(self):

		#making axes

		ax= Axes(x_range=[0,9,20], x_length=8, y_length=6,
			y_range=[0,17,21],tips=False, include_tick=False
			).shift(LEFT*1.5)

		special_xvalues = [3.75, 5, 3]
		special_yvalues = [7.5, 10, 6, 15]

		special_xticks = [ax[0].get_tick(val, 0.1).set_color(WHITE) for val in special_xvalues]
		special_xlabels = [DecimalNumber(val, font_size=25, color=WHITE)
        .next_to(t, DOWN, buff=0.1) for val,t in zip(special_xvalues,special_xticks)]

		special_yticks = [ax[1].get_tick(val, 0.1).set_color(WHITE) for val in special_yvalues]
		special_ylabels = [DecimalNumber(val, font_size=25, color=WHITE)
        .next_to(t, LEFT, buff=0.1) for val,t in zip(special_yvalues,special_yticks)]

		axes_ticks= VGroup()
		axes_ticks.add(*special_ylabels, *special_yticks, *special_xticks, *special_xlabels )


		#value tracker for slope
		d_slope= ValueTracker(2)
		d_xint= ValueTracker(7.5)


		#demand curve

		def demand(x):
			return 15- d_slope.get_value() *x

		d_curve= always_redraw(lambda: ax.plot(demand, x_range=[0, 6] ))


		#supply curve

		def supply(x):
			return 2*x

		s_curve= ax.plot(supply, x_range=[0, 6])


		#equilibrium point

		x_eq= ValueTracker(15/4)
		y_eq= ValueTracker(15/2)

		eq_h_line= always_redraw (lambda: ax.get_lines_to_point(ax.c2p(5.01, 
				y_eq.get_value()),color=RED, line_func=Line), 
				)
		eq_t_label = always_redraw(lambda: ax.get_T_label(x_val=x_eq.get_value(), 
			graph=d_curve, label=None, triangle_size=0.1))

		#equilibrium line for surplus

		surplus_line= always_redraw( lambda: ax.plot(lambda x: y_eq.get_value(),
				 x_range=[0,7.5], color=RED))


		#surpluses area

		area= always_redraw (lambda: ax.get_area(d_curve, color=GREEN, x_range=(0, x_eq.get_value()),
		 opacity=0.5,bounded_graph=surplus_line))

		area2= always_redraw (lambda: ax.get_area(s_curve, color=PURPLE, x_range=(0, x_eq.get_value()),
			opacity=0.5,bounded_graph=surplus_line))

		surplus_area= VGroup()
		surplus_area.add(area, area2)


		#showing surplus amount

		o_consumer_surplus_text= Tex("Original Consumer Surplus Area: 14",
			font_size=33).move_to(RIGHT *4 + UP *3).set_color(GREEN)

		o_producer_surplus_text= Tex("Original Producer Surplus Area: 14",
			font_size=33).next_to(o_consumer_surplus_text, DOWN, buff=0.2).set_color(PURPLE)

		o_surplus_text= VGroup()
		o_surplus_text.add(o_producer_surplus_text,o_consumer_surplus_text)


		consumer_surplus_text= (
			Tex("Consumer Surplus Area:", font_size=33).
			next_to(o_producer_surplus_text, DOWN, buff=0.2).
			set_color(GREEN)

			)

		consumer_surplus_value= always_redraw(lambda:
			DecimalNumber(num_decimal_places=1, font_size=33).
			set_value(1/2* ((15-y_eq.get_value()) * x_eq.get_value())).
			next_to(consumer_surplus_text, RIGHT, buff=0.2).
			set_color(GREEN)

			)

		producer_surplus_text= (
			Tex("Producer Surplus Area:", font_size=35).
			next_to(consumer_surplus_text, DOWN, buff= 0.2).
			set_color(PURPLE)

			)

		producer_surplus_value= always_redraw(lambda:
			DecimalNumber(num_decimal_places=1, font_size=35).
			set_value(1/2* (y_eq.get_value() * x_eq.get_value())).
			next_to(producer_surplus_text, RIGHT, buff=0.2).
			set_color(PURPLE)

			)

		surplus_text=VGroup()
		surplus_text.add(consumer_surplus_text, consumer_surplus_value,
			producer_surplus_text, producer_surplus_value)



		#basic setup, first equilibrium

		self.play(Create(ax), Create(d_curve),Create(s_curve)
			)
		self.play(Create(axes_ticks))
	
		self.play(Create(surplus_line), Create(eq_t_label))
		self.wait()

		#adding surpluses area
		self.play(Create(surplus_area))
		self.wait(2)

		#adding surpluses text
		self.play(Create(o_surplus_text))
		self.wait(1)
		self.play(Create(surplus_text))
		self.wait(1)

		self.play(Wiggle(d_curve), Wiggle(s_curve))


		#decreasing demand slope
		self.play(d_slope.animate.set_value(1), 
				d_xint.animate.set_value(7.5),
				x_eq.animate.set_value(5),
				y_eq.animate.set_value(10), run_time=3
				)

		self.wait(2)



		#increasing demand slope
		self.play(d_slope.animate.set_value(3),
				d_xint.animate.set_value(5),
				x_eq.animate.set_value(3),
				y_eq.animate.set_value(6), run_time=3
				)
		self.wait(2)
		
		
		#changing equilibrium
		

		self.wait(3)






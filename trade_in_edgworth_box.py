from manim import*


class Slide31Micro22W3(Scene):
	def construct(self):

		#edgeworth box
		ax1= Axes(x_range=[0,12], 
		y_range=[0,25],
		x_length=8,
		y_length=5,
       	axis_config={"include_tip": False, "include_ticks":False},
       	x_axis_config={"include_numbers":False}).shift(UP*0.5)

		x_label = ax1.get_x_axis_label(
            Tex("Loaves of Bread per Year").scale(0.65), edge=DOWN, direction=DOWN, buff=1
        )

		y_label = ax1.get_y_axis_label(
            Tex("Litres of Wine per Year").scale(0.65).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=1,
        )

		keeslab= Tex("Kees",font_size=30).next_to(ax1, LEFT).shift(DOWN*3.5)
		botleft= MathTex("O", font_size=30).next_to(keeslab,UP).shift(RIGHT*0.4)
		aaronlab= Tex("Aaron", font_size=30).next_to(botleft,UP).shift(UP*5.5+RIGHT*9.5)
		topright= MathTex("O'", font_size=30).next_to(aaronlab,DL)


		ax_1= VGroup(ax1, x_label, y_label,keeslab,botleft,aaronlab,topright)

		ax2= Axes(x_range=[0,12], 
		y_range=[0,25],
		x_length=-8,
		y_length=-5,
       	axis_config={"include_tip": False, "include_ticks":False},
       	x_axis_config={"include_numbers":False}).shift(UP*0.5)

		edgeworth= VGroup(ax_1, ax2)


		#ic lines


		bud_line= ax1.plot(lambda x: 19-0.6*x)
		bud_linelab= MathTex("B_{1}", font_size=25).next_to(bud_line, DR, buff=0.1)
		budline= VGroup(bud_line, bud_linelab)

		k_g= ax1.plot(lambda x: (70/x), x_range=[3,9], color=BLUE_D)
		k_glab= MathTex("K_{g}", font_size=25).next_to(k_g, DR, buff=0.1)
		kg= VGroup(k_g, k_glab)

		a_g= ax2.plot(lambda x: 65/x, x_range=[3.3,9], color=YELLOW_D)
		a_glab= MathTex("A_{g}", font_size=25).next_to(a_g, DR, buff=0.1)
		ag= VGroup(a_g, a_glab)

		k_e= ax1.plot (lambda x:48.6/x+8.4, x_range=[7,12], color=BLUE_D)
		k_elab= MathTex("K_{e}", font_size=25).next_to(k_e, RIGHT, buff=0.1)
		ke= VGroup(k_e, k_elab)

		a_e= ax2.plot (lambda x:100/x-2.3, x_range=[4,11.5], color=GREEN_D)
		a_elab= MathTex("A_{e}", font_size=25, color=GREEN_D).next_to(a_e, DR, buff=0.1)
		ae= VGroup(a_e, a_elab)

		#end of ic lines

		#dots

		dot_g= Dot(ax1.c2p(4.2,16.6))
		dot_glab= MathTex("g", font_size=30).next_to(dot_g, UR, buff=0.1)
		dotg= VGroup(dot_g, dot_glab)

		dot_ek= Dot(ax1.c2p(9,13.6))
		dot_eklab= MathTex("e_{k}", font_size=30).next_to(dot_ek, UR, buff=0.1)
		dotek= VGroup(dot_ek, dot_eklab)

		dot_ea= Dot(ax1.c2p(1,18.2))
		dot_ealab= MathTex("e_{a}", font_size=30).next_to(dot_ea, UP, buff=0.1)
		dotea= VGroup(dot_ea, dot_ealab)

		dot_i= Dot(ax1.c2p(4.2,13.6))
		dot_ilab= MathTex("i", font_size=30).next_to(dot_i, UR, buff=0.1)
		doti= VGroup(dot_i, dot_ilab)

		dot_k= Dot(ax1.c2p(1,16.6))
		dot_klab= MathTex("k",font_size=30).next_to(dot_k, DL, buff=0.1)
		dotk= VGroup(dot_k, dot_klab)

		movdot_gikx= ValueTracker(4.2)
		movdot_giky= ValueTracker(16.6)
		movdotgik= always_redraw(lambda: (Dot(ax1.c2p(movdot_gikx.get_value(), 
			movdot_giky.get_value()))))

		movdot_gkax= ValueTracker(4.2)
		movdot_gkay= ValueTracker(16.6)
		movdotgka= always_redraw(lambda: (Dot(ax1.c2p(movdot_gkax.get_value(), 
			movdot_gkay.get_value()))))

		#end of dots

		#braces
		brace_gi= BraceBetweenPoints(ax1.c2p(4.2,16.6), ax1.c2p(4.2,13.6))
		brace_gilab= Tex("Selling Wine", font_size=30).next_to(brace_gi, LEFT, buff=0.1)
		bracegi= VGroup(brace_gi, brace_gilab)

		brace_ik= BraceBetweenPoints(ax1.c2p(4.2,13.6), ax1.c2p(9,13.6))
		brace_iklab= Tex("Buying Bread", font_size=30).next_to(brace_ik, DOWN, buff=0.1)
		braceik= VGroup(brace_ik, brace_iklab)

		#lines

		horline_1= ax1.get_horizontal_line(ax1.c2p(4.2,16.6))
		horline_1lab= MathTex("d", font_size=30).next_to(horline_1, LEFT, buff=0.2)
		horline1= VGroup(horline_1, horline_1lab)
		
		horline_2= DashedLine(ax1.c2p(4.2,16.6), ax1.c2p(12,16.6))
		horline_2lab= MathTex("h", font_size=30).next_to(horline_2, RIGHT, buff=0.2)
		horline2= VGroup(horline_2, horline_2lab)


		verline_1= ax1.get_vertical_line(ax1.c2p(4.2,16.6))
		verline_1lab= MathTex("c", font_size=30).next_to(verline_1, DOWN, buff=0.2)
		verline1= VGroup(verline_1, verline_1lab)


		verline_2= DashedLine(ax1.c2p(4.2,16.6), ax1.c2p(4.2,25))
		verline_2lab= MathTex("f", font_size=30).next_to(verline_2, UP, buff=0.2)
		verline2= VGroup(verline_2, verline_2lab)

		line_ik= DashedLine(ax1.c2p(4.2,13.6), ax1.c2p(9,13.6))
		line_ak= DashedLine(ax1.c2p(1,16.6), ax1.c2p(1,18.2))

		lines= VGroup(horline1, horline2, verline1, verline2)

		#end of lines

		#animations
		self.add(edgeworth)

		self.play(Create(dotg), Create(lines), run_time=3)
		self.play(Create(kg), Create(ag))
		self.wait(1.5)
		self.play(Create(budline))
		self.wait(2)

		self.play(FadeOut(ag))
		self.wait(1)
		self.play(Create(ke), Create(dotek))
		self.wait(1)
		self.play(FadeOut(kg))
		self.wait(2)

		self.add(movdotgik)
		self.play(movdot_gikx.animate.set_value(4.2),movdot_giky.animate.set_value(13.6))
		self.add(doti)
		self.wait(1)
		self.play(Create(bracegi))
		self.wait(1.5)

		self.play(movdot_gikx.animate.set_value(9),movdot_giky.animate.set_value(13.6), run_time=2)
		self.play(Create(line_ik))
		self.play(Create(braceik))
		self.wait(2)
		self.play(FadeOut(braceik, bracegi))
		self.wait(1)

		self.play(Create(ag))
		self.wait(1)
		self.play(Create(ae), Create(dotea))
		self.wait(1)
		self.play(FadeOut(ag))
		self.add(movdotgka)
		self.play(movdot_gkax.animate.set_value(1),movdot_gkay.animate.set_value(16.6), run_time=2)
		self.add(dotk)
		self.wait(2)
		self.play(movdot_gkax.animate.set_value(1),movdot_gkay.animate.set_value(18.2), run_time=2)
		self.play(Create(line_ak))
		self.wait(4)













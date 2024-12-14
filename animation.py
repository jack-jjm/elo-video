from MF_Tools import *
from style import *

class simulation1(Scene):

    def construct(self):
        from simulation import Simulation
        sim = Simulation(100, k=10)

        plot_width = 2 * max(sim.true_max - sim.true_mean, sim.true_mean - sim.true_min) * 1.1
        x0 = sim.true_mean - plot_width / 2
        y0 = 1500 - plot_width / 2

        axes = QuadrantAxes(
            x_range=[x0, x0 + plot_width],
            y_range=[y0, y0 + plot_width],
            x_length=5,
            y_length=5,
            axis_config={ "include_ticks": False, "tip_width": 0.2, "tip_height": 0.2, "stroke_width": 10, "color": cyan }
        )
        axes.shift(UP * 0.5)

        guide = DashedLine(
            axes.c2p(x0, y0),
            axes.c2p(x0 + plot_width, y0 + plot_width),
            color=cyan,
            stroke_width=5
        )
        self.add(guide)

        y_label = Text("Elo", font_size=25, **text_style)
        x_label = Text("True rating", font_size=25, **text_style)

        y_label.rotate(90*DEGREES)
        y_label.next_to(axes, LEFT)
        x_label.next_to(axes, DOWN)

        n_games_label = Text("0 rounds played", font_size=25, **text_style).next_to(x_label, DOWN)
        n_games_label.shift(DOWN * 0.15)
        self.add(n_games_label)

        dot_style = {
            "radius": 0.07,
            "color": cyan
        }

        dots = [
            Dot(**dot_style).move_to(axes.c2p(x, y))
            for (x, y) in zip(sim.true_ratings, sim.ratings)
        ]

        t = 0
        n_games = 0
        def update(_, dt):
            nonlocal t
            nonlocal n_games

            t += 60 * dt
            if t < 1: return
            t = 0
            
            for dot, x, y in zip(dots, sim.true_ratings, sim.ratings):
                dot.move_to(
                    axes.c2p(
                        x, y
                    )
                )
            
            for _ in range(30):
                sim.update()
                n_games += 1

        def update_label(n_games_label, dt):
            # power = 0
            # n = n_games
            # while n > 10:
            #     n /= 10
            #     power += 1
            # exponent = "⁰¹²³⁴⁵⁶⁷⁸⁹"[power]
            new_text = Text(
                f"{n_games:,} rounds played",
                font_size=25,
                **text_style
            ).move_to(n_games_label)
            n_games_label.become(new_text)

        self.add(axes, x_label, y_label)

        self.play(
            Create(VGroup(*dots)),
            run_time=0.5
        )
        self.wait()
    
        dots[0].add_updater(update)
        n_games_label.add_updater(update_label)

        self.wait(15, frozen_frame=False)


class simulation2(Scene):

    def construct(self):
        from simulation import Simulation
        k1 = 10
        k2 = 100
        sim = Simulation(100, k=k1)
        sim2 = Simulation(100, k=k2)

        plot_width = 2 * max(sim.true_max - sim.true_mean, sim.true_mean - sim.true_min) * 1.1
        x0 = sim.true_mean - plot_width / 2
        y0 = 1500 - plot_width / 2

        axes = QuadrantAxes(
            x_range=[x0, x0 + plot_width],
            y_range=[y0, y0 + plot_width],
            x_length=5,
            y_length=5,
            axis_config={ "include_ticks": False, "tip_width": 0.2, "tip_height": 0.2, "stroke_width": 10, "color": cyan }
        )

        axes2 = QuadrantAxes(
            x_range=[x0, x0 + plot_width],
            y_range=[y0, y0 + plot_width],
            x_length=5,
            y_length=5,
            axis_config={ "include_ticks": False, "tip_width": 0.2, "tip_height": 0.2, "stroke_width": 10, "color": cyan }
        )

        axes2.next_to(axes, RIGHT, buff=2)

        VGroup(axes, axes2).center()

        k_label1 = Text(f"k = {k1}", font_size=25, **text_style)
        k_label2 = Text(f"k = {k2}", font_size=25, **text_style)
        k_label1.next_to(axes,  DOWN, buff=0.25)
        k_label2.next_to(axes2, DOWN, buff=0.25)
        self.add(k_label1, k_label2)

        guide = DashedLine(
            axes.c2p(x0, y0),
            axes.c2p(x0 + plot_width, y0 + plot_width),
            color=cyan,
            stroke_width=5
        )
        guide2 = DashedLine(
            axes2.c2p(x0, y0),
            axes2.c2p(x0 + plot_width, y0 + plot_width),
            color=cyan,
            stroke_width=5
        )
        self.add(guide)
        self.add(guide2)

        n_games_label = Text("0 rounds played", font_size=25, **text_style).center()
        n_games_label.next_to(k_label1, DOWN, coor_mask=(0, 1, 0))
        # n_games_label.shift(DOWN * 0.15)
        self.add(n_games_label)

        dot_style = {
            "radius": 0.07,
            "color": cyan
        }

        dots = [
            Dot(**dot_style).move_to(axes.c2p(x, y))
            for (x, y) in zip(sim.true_ratings, sim.ratings)
        ]

        dots2 = [
            Dot(**dot_style).move_to(axes2.c2p(x, y))
            for (x, y) in zip(sim2.true_ratings, sim2.ratings)
        ]

        t = 0
        n_games = 0
        def update(_, dt):
            nonlocal t
            nonlocal n_games

            t += 60 * dt
            if t < 1: return
            t = 0
            
            for dot, x, y in zip(dots, sim.true_ratings, sim.ratings):
                dot.move_to(
                    axes.c2p(
                        x, y
                    )
                )

            for dot, x, y in zip(dots2, sim2.true_ratings, sim2.ratings):
                dot.move_to(
                    axes2.c2p(
                        x, y
                    )
                )
            
            for _ in range(4):
                sim.update()
                sim2.update()
                n_games += 1

        def update_label(n_games_label, dt):
            # power = 0
            # n = n_games
            # while n > 10:
            #     n /= 10
            #     power += 1
            # exponent = "⁰¹²³⁴⁵⁶⁷⁸⁹"[power]
            new_text = Text(
                f"{n_games:,} rounds played",
                font_size=25,
                **text_style
            ).move_to(n_games_label)
            n_games_label.become(new_text)

        self.add(axes)
        self.add(axes2)

        self.play(
            Create(VGroup(*dots)),
            Create(VGroup(*dots2)),
            run_time=0.5
        )
        self.wait()

        dots[0].add_updater(update)
        n_games_label.add_updater(update_label, call_updater=True)

        self.wait(14, frozen_frame=False)


class QuadrantAxes(Axes):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        patch = Square(side_length=0.1, stroke_width=0, fill_color=cyan, fill_opacity=1)
        patch.move_to(self.c2p(self.x_range[0], self.y_range[0]))
        self.add(patch)

    @staticmethod
    def _origin_shift(axis_range):
        return axis_range[0]

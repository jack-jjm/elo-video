import numpy as np


class Simulation:
    
    def __init__(self, n_players=1000, k=10, seed=0):
        self.n_players = n_players
        self.k = k
        self.r0 = 1500
        self.s = 400

        self.rng = np.random.default_rng(seed) # 3

        # uniform        
        # self.true_ratings = np.random.uniform(-1000, 1000, size=n_players)
        # self.weights = np.power(10, self.true_ratings / self.s)

        # normal
        self.true_ratings = self.rng.normal(0, 1000, size=n_players)
        self.true_ratings.sort()
        self.weights = np.power(10, self.true_ratings / self.s)

        self.true_mean = float(np.mean(self.true_ratings))
        self.true_min = float(np.min(self.true_ratings))
        self.true_max = float(np.max(self.true_ratings))

        self.indices = np.arange(0, self.n_players, 1).astype(np.int32)
        self.ratings = self.r0 * np.ones(self.n_players)

    def naive_matchmaking(self, indices):
        n_players = len(indices)
        opponents = self.rng.choice(n_players, size=n_players // 2, replace=False)
        team_a = indices[opponents]
        team_b = np.delete(indices, opponents)
        self.rng.shuffle(team_b)
        return team_a, team_b
    
    def close_matchmaking(self):
        sorted_indices = np.argsort(self.ratings)
        a_teams = []
        b_teams = []
        for i in range(0, self.n_players, 200):
            slice = sorted_indices[i:i+200]
            team_a, team_b = self.naive_matchmaking(slice)
            a_teams.append(team_a)
            b_teams.append(team_b)

        return np.concatenate(a_teams), np.concatenate(b_teams)

    def update(self):
        n_players = self.n_players
        k = self.k
        r0 = self.r0
        s = self.s
        weights = self.weights
        indices = self.indices
        ratings = self.ratings

        team_a, team_b = self.naive_matchmaking(self.indices)
        
        rating_differences = ratings[team_b] - ratings[team_a]
        expected_scores_a = 1 / (1 + 10**(rating_differences / s))

        probabilities = weights[team_a] / (weights[team_a] + weights[team_b])
        scores_a = self.rng.binomial(1, probabilities)

        rewards_a = k*(scores_a - expected_scores_a)
        rewards_b = -rewards_a
        ratings[team_a] += rewards_a
        ratings[team_b] += rewards_b


def render(surface):
    import pygame.draw as draw

    def xy(true_rating, rating):
        x = 400 + int((true_rating - 1500) / 4)
        y = 400 - int((rating - 1500) / 4)
        return x, y

    surface.fill((0, 0, 0))

    draw.line(
        surface, (255, 0, 0),
        xy(0, 0),
        xy(3000, 3000)
    )

    for true_r, rating in zip(simulation.true_ratings, simulation.ratings):
        x, y = xy(true_r, rating)
        draw.circle(surface, (255, 255, 255), (x, y), 2)

    estimated_gap = (simulation.ratings.max() - simulation.ratings.min()) / 400
    true_gap = np.log10(simulation.weights.max() / simulation.weights.min())

    print(f"{estimated_gap:.3f}/{true_gap:.3f}", end="    \r")

    simulation.update()

simulation = Simulation()
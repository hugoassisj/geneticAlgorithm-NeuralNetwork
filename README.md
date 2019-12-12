[![HitCount](http://hits.dwyl.io/hugoassisj/geneticAlgorithm-NeuralNetwork.svg)](http://hits.dwyl.io/hugoassisj/geneticAlgorithm-NeuralNetwork)

# geneticAlgorithm-NeuralNetwork
Using a Genetic Algorithm to train a Neural Network to solve the Inverted Pendulum problem.

Observation:

| Num | Observation          | Min     | Max    |
|-----|----------------------|---------|--------|
| 0   | Cart Position        | -4.8    | 4.8    |
| 1   | Cart Velocity        | -Inf    | Inf    |
| 2   | Pole Angle           | -24 deg | 24 deg |
| 3   | Pole Velocity At Tip | -Inf    | Inf    |

Actions:

| Num | Action                 |
|-----|------------------------|
| 0   | Push cart to the left  |
| 1   | Push cart to the right |

 * Note: The amount the velocity that is reduced or increased is not fixed; it depends on the angle the pole is pointing. This is because the center of gravity of the pole increases the amount of energy needed to move the cart underneath it

Reward:
    Reward is 1 for every step taken, including the termination step

Starting State:
    All observations are assigned a uniform random value in [-0.05..0.05]

Episode Termination:


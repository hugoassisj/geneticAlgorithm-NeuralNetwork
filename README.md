[![HitCount](http://hits.dwyl.io/hugoassisj/geneticAlgorithm-NeuralNetwork.svg)](http://hits.dwyl.io/hugoassisj/geneticAlgorithm-NeuralNetwork)

# geneticAlgorithm-NeuralNetwork
Using a Genetic Algorithm to train a Neural Network to solve the Inverted Pendulum problem.

![one](https://user-images.githubusercontent.com/45035051/76994682-88ee8800-692d-11ea-86a2-978504a558e7.png)

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

![Picture1](https://user-images.githubusercontent.com/45035051/76994908-d3700480-692d-11ea-8dd8-a9078b957160.gif)


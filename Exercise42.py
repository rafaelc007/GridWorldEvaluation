from GridWorld import Gridworld
import numpy as np


class ExcentricGridWorld(Gridworld):
    def __init__(self):
        self._finals = [0, 15]
        self._side = 4
        self._n_states = self._side**2
        self._init_vars(self._n_states+1)

    def _walk(self, state, direction):
        """
        state 15 depicted in the exercise is state 16 here and it is a separate state.
        :param state: actual state
        :param direction: direction to walk
        :return: (next state, reward)
        """
        if state == 16:
            if direction == "u" : return (13, -1)
            elif direction == "d": return (16, -1)
            elif direction == "l": return (12, -1)
            elif direction == "r": return (14, -1)
        elif state == 13 and direction == 'd':
            return (16, -1)     # attach separate state S_16 to S_13
        else:
            return super()._walk(state, direction)

    def gen_rand_policy(self):
        return np.matrix([[0.25] * 4] * (self._n_states+1), dtype=float)

    def print_vals(self):
        super().print_vals()
        print([0, self._values[-1], 0, 0])

def test_states(grid: Gridworld):
    for idx in range(17):
        [print("-", end =" ") for _ in range(11)]
        print()
        for act in ["u", "d", "l", "r"]:
            print("s = {}, a = {} : n_s = {}".format(idx, act, grid._walk(idx, act)[0]))

if __name__ == "__main__":
    grid = ExcentricGridWorld()

    # test_states(grid)
    grid.pol_eval()
    grid.print_vals()
    [print("-", end =" ") for _ in range(11)]
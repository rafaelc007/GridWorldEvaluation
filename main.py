import numpy as np

class Gridworld:
    def __init__(self, n_side, final_states: list):
        if final_states:
            self._finals = final_states
        self._side = n_side
        self._n_states = self._side**2
        self._state_list = np.arange(self._n_states)

    def _walk(self, state, direction):
        if state in self._finals:
            return state
        elif direction == "u":
            return state if state < self._side else state-self._side
        elif direction == "d":
            return state if state > self._n_states-self._side else state+self._side
        elif direction == "l":
            return state if state % self._side == 0 else state-1
        elif direction == "r":
            return state if state % self._side == self._side-1 else state+1


def PolEval(policy: np.matrix, theta=1e-3):
    """
    :param policy: matrix of policy in format [n_states, n_actions]
    :param theta: threshold to stop the evaluation
    :return: state values after policy evaluation
    """
    V = [0.0]*policy.size[0]
    delta = 0.0
    while(delta < theta):
        for idx in range(len(V)):
            V[idx] = 
    return

if __name__ == "__main__":
    grid = Gridworld(4, [0, 15])



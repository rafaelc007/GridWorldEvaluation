import numpy as np

class Gridworld:
    def __init__(self, n_side, final_states: list):
        if final_states:
            self._finals = final_states
        self._side = n_side
        self._n_states = self._side**2
        self._state_list = np.arange(self._n_states)

    def walk(self, state, direction):
        """
        walk a step and find out where you end up.
        :param state: actual state to eval
        :param direction: direction where to go {'u', 'd', 'r', 'l'}
        :return: {next state, reward}
        """
        if state in self._finals:
            return state, 0
        elif direction == "u":
            return (state, -1) if state < self._side else state-self._side
        elif direction == "d":
            return (state, -1) if state > self._n_states-self._side else state+self._side
        elif direction == "l":
            return (state, -1) if state % self._side == 0 else state-1
        elif direction == "r":
            return (state, -1) if state % self._side == self._side-1 else state+1

    def p(self, n_state, state, action):
        """
        return dynamics of the environment for a next state, given an actual state and action taken.
        :param n_state: next state
        :param state: actual state
        :param action: action taken
        :return: p(s'|s,a)
        """
        for dir in ["u", "d", "l", "r"]:
            n_s, r = self.walk(state, dir)
            if n_state == n_s : return 1
        return 0

def PolEval(env: Gridworld, policy: np.matrix, theta=1e-3):
    """
    :param policy: matrix of policy in format [n_states, n_actions]
    :param theta: threshold to stop the evaluation
    :return: state values after policy evaluation
    """
    V = np.zeros(policy.size[0], dtype=float)
    Q = np.matrix([[[0]*policy.size[1]]*policy.size[0]], dtype=float)
    delta = 0.0
    while delta < theta:
        for s in range(len(V)):
            for a in ["u", "d", "l", "r"]:
                n_s, r = env.walk(s, a)
                Q[s, a] += (r + V[n_s])
            V[s] = np.dot(policy[s,:],Q[s,:])
    return V

if __name__ == "__main__":
    grid = Gridworld(4, [0, 15])



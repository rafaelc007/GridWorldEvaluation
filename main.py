import numpy as np

class Gridworld:
    def __init__(self, n_side, final_states: list):
        if final_states:
            self._finals = final_states
        self._side = n_side
        self._n_states = self._side**2
        self._state_list = np.arange(self._n_states)
        self._values = np.zeros(self._n_states, dtype=float)
        self._action_values = np.matrix([[0]*4]*self._n_states, dtype=float)

    def gen_rand_policy(self):
        return np.matrix([[0.25] * 4] * self._n_states, dtype=float)

    def _walk(self, state, direction):
        """
        walk a step and find out where you end up.
        :param state: actual state to eval
        :param direction: direction where to go {'u', 'd', 'r', 'l'}
        :return: {next state, reward}
        """
        if state in self._finals:
            return state, 0
        elif direction == "u":
            return (state, -1) if state < self._side else (state-self._side, -1)
        elif direction == "d":
            return (state, -1) if state >= self._n_states-self._side else (state+self._side, -1)
        elif direction == "l":
            return (state, -1) if state % self._side == 0 else (state-1, -1)
        elif direction == "r":
            return (state, -1) if state % self._side == self._side-1 else (state+1, -1)

    def p(self, n_state, state, action):
        """
        return dynamics of the environment for a next state, given an actual state and action taken.
        :param n_state: next state
        :param state: actual state
        :param action: action taken
        :return: p(s'|s,a)
        """
        for dir in ["u", "d", "l", "r"]:
            n_s, r = self._walk(state, dir)
            if n_state == n_s : return 1
        return 0

    def print_vals(self):
        n_size = int(np.sqrt(self._values.size))
        for idx in range(n_size):
            print(self._values[idx*n_size:idx*n_size+n_size])

    def pol_eval(self, policy=None, theta=1e-4):
        """
        :param policy: matrix of policy in format [n_states, n_actions]
        :param theta: threshold to stop the evaluation
        :return: state values after policy evaluation
        """
        if not policy:
            policy = self.gen_rand_policy()
        V = self._values.copy()
        Q = self._action_values.copy()
        delta = 1e100
        while delta > theta:
            delta = 0.0
            for s in range(len(V)):
                Q[s, :] = [0.0]*4
                for a, action in enumerate(["u", "d", "l", "r"]):
                    n_s, r = self._walk(s, action)
                    Q[s, a] += (r + V[n_s])
                new_V = np.dot(policy[s, :], np.transpose(Q[s, :]))[0, 0]
                delta = np.maximum(delta, np.abs(V[s] - new_V))
                V[s] = new_V
        self._values = V
        self._action_values = Q
        return V

if __name__ == "__main__":
    grid = Gridworld(4, [0, 15])
    grid.pol_eval()
    grid.print_vals()
    print(["="]*11)
    print(grid._action_values[11,1])
    print(grid._action_values[7,1])


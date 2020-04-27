from GridWorld import Gridworld


if __name__ == "__main__":
    grid = Gridworld(4, [0, 15])
    grid.pol_eval()
    grid.print_vals()
    print(["="]*11)
    print(grid._action_values[11,1])
    print(grid._action_values[7,1])


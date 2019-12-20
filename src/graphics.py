import matplotlib.pyplot as plt
from algorithms import *
import tests


def showAlgorithms(points, gen=None):
    fig, ax = plt.subplots()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    def press(event):
        if event.key == 'd':
            n = next(gen)
            if n is not None:
                showAlgorithms(next(gen), gen)
            plt.close(fig)
    if gen is not None:
        fig.canvas.mpl_connect('key_press_event', press)

    # display legend
    ritter_leg = plt.Line2D([0], [0], marker='o', color="w", alpha=0.5, label='Ritter',
                            markerfacecolor="r", markersize=15),
    plt.legend(handles=ritter_leg)

    # get all points coordinates
    x_list = [p.x for p in points]
    y_list = [p.y for p in points]
    # draw points
    ritter_circle = ritter(points)
    plt.xlim(ritter_circle.center.x - ritter_circle.radius*1.5,
             ritter_circle.center.x + ritter_circle.radius*1.5)
    plt.ylim(ritter_circle.center.y - ritter_circle.radius*1.5,
             ritter_circle.center.y + ritter_circle.radius*1.5)
    ax.set_aspect('equal')
    ax.add_artist(plt.Circle((ritter_circle.center.x, ritter_circle.center.y),
                             ritter_circle.radius, color='r', alpha=0.5))
    ax.scatter(x_list, y_list, 1)
    plt.show()


def showAllFiles():
    t = tests.gen_lists()
    l = next(t)
    showAlgorithms(l, t)


if __name__ == '__main__':
    showAllFiles()

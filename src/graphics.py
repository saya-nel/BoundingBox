import matplotlib.pyplot as plt
import matplotlib.patches as patches
from algorithms import *
import tests


def showAlgorithms(points, name, gen=None):
    # window parameters
    fig, ax = plt.subplots(num=name)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # event for switch tests
    def press(event):
        if event.key == 'd':
            next_points, file_name = next(gen)
            if next_points is not None:
                showAlgorithms(next_points, file_name, gen)
            plt.close(fig)
    if gen is not None:
        fig.canvas.mpl_connect('key_press_event', press)

    # display legend
    toussaint_leg = patches.Patch(color='b', label='Toussaint')
    ritter_leg = plt.Line2D([0], [0], marker='o', color="w", alpha=0.5, label='Ritter',
                            markerfacecolor="r", markersize=15)
    plt.legend(handles=[toussaint_leg, ritter_leg])

    # draw points
    x_list = [p.x for p in points]
    y_list = [p.y for p in points]
    ax.scatter(x_list, y_list, 1)

    # draw ritter
    ritter_circle = ritter(points)
    plt.xlim(ritter_circle.center.x - ritter_circle.radius*1.5,
             ritter_circle.center.x + ritter_circle.radius*1.5)
    plt.ylim(ritter_circle.center.y - ritter_circle.radius*1.5,
             ritter_circle.center.y + ritter_circle.radius*1.5)
    ax.set_aspect('equal')
    ax.add_artist(plt.Circle((ritter_circle.center.x, ritter_circle.center.y),
                             ritter_circle.radius, color='r', alpha=0.5))

    # draw toussaint
    touss = toussaint(points)
    touss_l = [touss.a, touss.b, touss.c, touss.d]
    for i in range(1, len(touss_l)):
        plt.plot([touss_l[i - 1].x, touss_l[i].x],
                 [touss_l[i - 1].y, touss_l[i].y], color='b')
    plt.plot([touss_l[0].x, touss_l[len(touss_l) - 1].x],
             [touss_l[0].y, touss_l[len(touss_l) - 1].y], color='b')

    # dislay
    plt.show()


def showAllFiles():
    gen = tests.gen_lists()
    l, fic = next(gen)
    showAlgorithms(l, fic, gen)


if __name__ == '__main__':
    showAllFiles()

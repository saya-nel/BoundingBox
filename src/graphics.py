import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
    # draw points & ritter
    ritter_circle = ritter(points)
    plt.xlim(ritter_circle.center.x - ritter_circle.radius*1.5,
             ritter_circle.center.x + ritter_circle.radius*1.5)
    plt.ylim(ritter_circle.center.y - ritter_circle.radius*1.5,
             ritter_circle.center.y + ritter_circle.radius*1.5)
    ax.set_aspect('equal')
    ax.add_artist(plt.Circle((ritter_circle.center.x, ritter_circle.center.y),
                             ritter_circle.radius, color='r', alpha=0.5))
    ax.scatter(x_list, y_list, 1)
    # draw quickHull
    qh = quickHull(points)
    for i in range(1, len(qh)):
        plt.plot([qh[i - 1].x, qh[i].x],
                 [qh[i - 1].y, qh[i].y], color='g')
    plt.plot([qh[0].x, qh[len(qh) - 1].x],
             [qh[0].y, qh[len(qh) - 1].y], color='g')
    # draw toussaint
    touss = toussaint(points)
    touss_l = [touss.a, touss.b, touss.c, touss.d]
    for i in range(1, len(touss_l)):
        plt.plot([touss_l[i - 1].x, touss_l[i].x],
                 [touss_l[i - 1].y, touss_l[i].y], color='b')
    plt.plot([touss_l[0].x, touss_l[len(touss_l) - 1].x],
             [touss_l[0].y, touss_l[len(touss_l) - 1].y], color='b')

    plt.show()


def showAllFiles():
    t = tests.gen_lists()
    l = next(t)
    showAlgorithms(l, t)


if __name__ == '__main__':
    showAllFiles()

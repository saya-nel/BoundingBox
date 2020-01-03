import matplotlib.pyplot as plt
import matplotlib.patches as patches
from algorithms import *
import tests
import statistics
import sys


def showAlgorithms(points, name, gen=None):
    """
    Display Toussaint's and Ritter's algorithms applied to the list points,
    with the window name name, if most of one file need to be tested, you can
    pass a generator that return a list of points from the gen arg
    """
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
    toussaint_leg = patches.Patch(color='g', label='Toussaint')
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
                 [touss_l[i - 1].y, touss_l[i].y], color='g', alpha=0.5)
    plt.plot([touss_l[0].x, touss_l[len(touss_l) - 1].x],
             [touss_l[0].y, touss_l[len(touss_l) - 1].y], color='g', alpha=0.5)

    # dislay
    plt.show()


def showAllFiles():
    """
    Apply the algorithms to all file and display them one by one
    , you can go to the next file by pressing 'd' key
    """
    gen = tests.gen_lists()
    l, fic = next(gen)
    showAlgorithms(l, fic, gen)


def showExecutionTime(gap):
    """
    Show the execution time of the algorithms applied to points lists
    from size 256 to 425984, with the gap given in parameter. 
    The recomended gap for a fast display is 10 000
    The recomended gap for a precise display is 1 000
    """
    # window parameters
    fig, ax = plt.subplots(num="Execution time")
    ax.set_xlabel('Number of points')
    ax.set_ylabel('Computation time (in seconds)')

    points_number = range(256, 425984, gap)
    touss, rit = tests.algorithms_time(gap)

    plt.plot(points_number, touss, color="g", label="Toussaint")
    plt.plot(points_number, rit, color="r", label="Ritter")
    plt.legend()
    plt.show()


def showAlgorithmsQuality():
    """Display the algorithms quality"""
    fig, ax = plt.subplots(num="Quality")
    ax.set_xlabel("File index")
    ax.set_ylabel("quality")

    file_numbers = range(1, 1664)
    touss, rit = tests.algorithms_quality()

    plt.plot(file_numbers, touss, color="g", label="Toussaint", alpha=0.3)
    plt.plot(file_numbers, rit, color="r", label="Ritter", alpha=0.3)
    plt.legend()

    print("moyenne | toussaint :", statistics.mean(touss), "ritter :", statistics.mean(
        rit))
    print("ecart type | toussaint :", statistics.stdev(
        touss), "ritter :", statistics.stdev(rit))
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "quality":
            showAlgorithmsQuality()
        elif sys.argv[1] == "time":
            if len(sys.argv) > 2:
                try:
                    showExecutionTime(int(sys.argv[2]))
                except:
                    print(
                        "le dernier argument doit etre un entier positif, representant le gap.")
            else:
                showExecutionTime(1000)
    else:
        print("Vous pouvez passer au test suivant en appuyant sur la touche 'd'")
        showAllFiles()

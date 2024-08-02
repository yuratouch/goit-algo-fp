import matplotlib.pyplot as plt
import math

def draw_pythagoras_tree(ax, x, y, length, angle, depth, max_depth):
    if depth > max_depth:
        return
    
    x2 = x + length * math.cos(math.radians(angle))
    y2 = y + length * math.sin(math.radians(angle))

    ax.plot([x, x2], [y, y2], color='green')

    new_length = length * math.sqrt(0.5)
    draw_pythagoras_tree(ax, x2, y2, new_length, angle + 45, depth + 1, max_depth)
    draw_pythagoras_tree(ax, x2, y2, new_length, angle - 45, depth + 1, max_depth)

def main():
    recursion_depth = int(input("Введіть рівень рекурсії: "))

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    draw_pythagoras_tree(ax, 0, 0, 100, 90, 0, recursion_depth)

    plt.show()

if __name__ == "__main__":
    main()

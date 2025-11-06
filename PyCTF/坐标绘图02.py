import matplotlib.pyplot as plt

def read_coordinates(file_path):
    coords = []
    with open(file_path, 'r', encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if not line or not line.startswith('('):
                continue
            try:
                x_str, y_str = line.strip("()").split(',')
                x = float(x_str.strip())
                y = float(y_str.strip())
                coords.append((x, y))
            except Exception as e:
                print(f"Error parsing line '{line}': {e}")
    return coords

def plot_coords(coords):
    if not coords:
        print("No coordinates to plot.")
        return
    x, y = zip(*coords)
    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, s=8, color='black', alpha=0.7)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter plot of coordinates')
    plt.grid(False)
    plt.axis('equal')
    plt.show()

# 直接执行
coords = read_coordinates("C:/Users/admin/Desktop/download.txt")
plot_coords(coords)
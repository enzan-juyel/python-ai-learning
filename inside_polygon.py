import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point

def inside_polygon(polygon, points):
   return all([polygon.contains(Point(point)) for point in points])

def plot_polygon(coordinates, points):
    polygon = Polygon(coordinates)

    # Extract x and y coordinates for the polygon
    x_poly, y_poly = zip(*polygon.exterior.coords)

    # Extract x and y coordinates for the points and close if it's a bounding box
    x_points, y_points = zip(*points + [points[0]])

    plt.figure(figsize=(8, 8))

    # Plot the polygon
    plt.plot(x_poly, y_poly, marker='o', linestyle='-', color='blue', label="Polygon")
    plt.fill(x_poly, y_poly, alpha=0.3, color='blue')

    # Plot the points (bounding box or other points)
    plt.plot(x_points, y_points, marker='s', linestyle='--', color='red', label="Points")

    # Labels and title
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Polygon with Points Visualization")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()


def main():
    # Define the polygon
    coordinates = [
        (103.520420, 1.513053),
        (103.878854, 1.603657),
        (104.255104, 1.289642),
        (103.829578, 1.043506),
        (103.447971, 1.131381),
        (103.520420, 1.513053)
    ]
    # Create a polygon object
    polygon = Polygon(coordinates)

    # Define the new bounding box
    max_lat, max_lon = 1.3763114804773484, 104.00135742506856
    min_lat, min_lon = 1.3711263721016846, 103.97453214308564

    points = [
        (min_lon, max_lat),
        (max_lon, max_lat),
        (max_lon, min_lat),
        (max_lon, min_lat)
    ]

    # Check if the points are inside the polygon
    is_inside = inside_polygon(polygon, points)
    if is_inside:
        plot_polygon(coordinates, points)
    else:
        print("The points are not inside the polygon")

if __name__ == "__main__":
    main()
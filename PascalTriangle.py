def pascal_triangle(rows):
    # Declare default triangle
    triangle = [[1], [1, 1]]
    # Last row marker
    last_row = triangle[1]
    for i in range(2, rows):
        # First value in row
        row = [1]
        # Create middle values of row
        for j in range(0, len(last_row)-1):
            cell = last_row[j] + last_row[j+1]
            row.append(cell)
        # Last value in row
        row.append(1)
        # Add row to triangle
        triangle.append(row)
        # Update last row marker
        last_row = row
    return triangle


def print_pascal_triangle(triangle_data):
    triangle = ''
    for row in triangle_data:
        for cell in row:
            triangle += str(cell) + ' '
        triangle += '\n'
    print(triangle)


print_pascal_triangle(pascal_triangle(10))

lio = input("Enter a list of heights separated by space: ").split()
heights = []
for i in lio:
    height = int(i)
    heights.append(height)

average_heights = sum((heights)) / len(heights)
rounded_average = round(average_heights)

print(f"The average height is {rounded_average}")

input("Press ENTER to exit")

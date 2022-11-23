def main():
  points = []
  for i in range(4):
    print('Input the point number ' + str(i + 1))
    points.append({
      'x': int(input('x: ')),
      'y': int(input('y: ')),
      'z': int(input('z: '))
    })

  min_distance = float('inf')
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      min_distance = min([min_distance, abs(((points[i]['x'] - points[j]['x'])**2 + (points[i]['y'] - points[j]['y'])**2 + (points[i]['z'] - points[j]['z'])**2)**0.5)])
  
  print('The answer is: ' + str(min_distance))


if __name__ == '__main__':
  main()

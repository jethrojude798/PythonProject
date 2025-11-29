choice = int(input('enter your choice (1-5)'))
if choice == 1:
    print('Calculating distance')
    distance = int(input('enter value for distance'))
    time = int(input('enter value for time'))

    velocity = distance / time

    print('velocity is', velocity)

elif choice == 2:
    print('Calculating force')
    mass = int(input('enter value for mass'))
    acceleration = int(input('enter value for acceleration'))

    force = mass * acceleration

    print('force is', force)

elif choice == 3:
    print('Calculating volume')
    length = int(input('enter value for lenght'))
    breadth = int(input('enter value for breadth'))
    height = int(input('enter value for height'))

    volume = length * breadth * height

    print('volume is', volume)

elif choice == 4:
    print('Calculating power')
    work = int(input('enter value for work'))
    time = int(input('enter value for time'))

    power = work / time

    print('power is', power)

elif choice == 5:
    print('Calculating density')
    mass = int(input('enter value for mass'))
    volume = int(input('enter value for volume'))

    density = mass / volume

    print('density is', density)


else:
    print('Invalid choice , please choose correct value ')

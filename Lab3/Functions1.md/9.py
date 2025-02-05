def sphere(rad):
    Volume = (4/3) * 3.14 * (rad**3)
    print(f"Volume: {Volume:.3f}")
rad = float(input("Radius: "))
sphere(rad)
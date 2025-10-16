motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('bmw')
print(motorcycles)
motorcycles.insert(0, 'harley-davidson')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(f"i like {popped_motorcycle}")
too_cool = 'suzuki'
motorcycles.remove(too_cool)
print(motorcycles)
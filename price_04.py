from price_03 import read_file
ring_data=read_file("price.csv")
small_ring=[]
for ring in ring_data:
    if ring["radius"]<5:
        small_ring.append((ring["metal"],ring["price"],ring["radius"]))
for ring in small_ring:
    print(ring)

ring_data.sort(key=lambda all_data : all_data['metal'])


for data in ring_data:
    print(data)

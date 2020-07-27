def song_lyrics(n):
    if n==2:
        print("%d bottles of beer on the wall" %n)
        print("%d bottles of beer" %n)
        print("Take one down, pass it around")
        print("%d bottle of beer on the  table" %(n-1))
    elif n==1:
        print("%d bottle of beer on the wall" %n)
        print("%d bottle of beer" %n)
        print("Take one down, pass it around")
        print("No more bottles of beer on the  table")

    elif n==0:
        print("No bottles of beer on the wall")
        print("No bottles of beer")
        print("We took 'emdown passed 'em aroun")
        print("No more bottles of beer on the wall")
    else:
        print("%d bottles of beer on the wall" %n)
        print("%d bottles of beer" %n)
        print("Take one down, pass it around")
        print("%d bottles of beer on the  table" %(n-1))

    if n>0:
        
    print()

for i in range(99,-1,-1):
    song_lyrics(i)

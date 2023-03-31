from pynput import keyboard
import time
xPlane = []  # 10
yPlane = []  # 15

blockObj = "X"

blockObjYVal = 15

blockObjXVal = 0
Running1 = True
Running2 = True
maximumVal = 0
while Running2 == True:




    # building an x/y plane:
    for x in range( 20 ):
        xPlane.append( '-' )

    for z in range( 20 ):
        yPlane.append( xPlane )

    def newListEachTime(n):
        lst = [];
        for x in range(len(yPlane)):
            lst.append( '-' )

        lst[n] = 'X'
        return lst

    yPlane[blockObjYVal - 1] = (newListEachTime( blockObjXVal ))
    def KeyLoggerPro():
        print("Enter a key: ")
        with keyboard.Events() as events:
        # Block for as much as possible
            event = events.get(1e6)
            if event.key == keyboard.KeyCode.from_char('w'):
                return "W"
            elif event.key == keyboard.KeyCode.from_char('a'):
                return "A"
            elif event.key == keyboard.KeyCode.from_char('s'):
                return "S"
            elif event.key == keyboard.KeyCode.from_char('d'):
                return "D"
            elif event.key == keyboard.KeyCode.from_char('p'):
                return "P"
            elif event.key == keyboard.KeyCode.from_char('l'):
                return "L"

    maximumVal +=20
    while Running1 == True:
        yPlane[blockObjYVal - 1] = xPlane
        keyRecorded = KeyLoggerPro()
        time.sleep( 0.1 )  # Sleep for 3 seconds
        print(keyRecorded)
        if keyRecorded == 'D':
            blockObjXVal += 1
        elif keyRecorded == 'A':
            blockObjXVal -= 1
        elif keyRecorded == 'S':
            blockObjYVal -= 1
        elif keyRecorded == 'W':
            blockObjYVal += 1
        elif keyRecorded == 'P':
            break
        else:
            Running2 = False
            Running1 = False
        print( blockObjYVal, blockObjXVal )
        if (blockObjXVal < maximumVal and blockObjXVal >= 0) and (blockObjYVal <= maximumVal and blockObjYVal >= 0):

            yPlane[blockObjYVal - 1] = (newListEachTime( blockObjXVal ))
            x1 = 0
            while x1 in range( len( yPlane ) ):
                lastY = len( yPlane ) - 1
                print( yPlane[lastY - x1] )
                x1 += 1
        else:
            yPlane[maximumVal - 1] = (newListEachTime( maximumVal -1))
            print("YOU CAN NOT MOVE ANY FURTHER!")
            if keyRecorded == 'D':
                blockObjXVal += 1
            elif keyRecorded == 'A':
                blockObjXVal -= 1
            elif keyRecorded == 'S':
                blockObjYVal -= 1
            elif keyRecorded == 'W':
                blockObjYVal += 1
            x1 = 0
            while x1 in range( len( yPlane ) ):
                lastY = len( yPlane ) - 1
                print( yPlane[lastY - x1] )
                x1 += 1
            break
    x1 = 0
    while x1 in range( len( yPlane ) ):
        lastY = len( yPlane ) - 1
        print( yPlane[lastY - x1] )
        x1 += 1

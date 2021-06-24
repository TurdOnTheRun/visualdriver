import numpy, cv2

def easeOutQuad(x):
    return 1 - (1 - x) * (1 - x)

img = numpy.zeros([1000,1000,1])

t = 0

while(t<2): 
    cv2.imshow("image", img)
    # Press Q on keyboard to  exit
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

    

   
# Closes all the frames
cv2.destroyAllWindows()
import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def detection(frame):
    optimized_frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces = face_ref.detectMultiScale(optimized_frame,scaleFactor=1.1,minSize=(100, 100))
    return faces

def box(frame):
    faces = detection(frame)
    count = len(faces)
    
    for x, y, w, h in detection(frame):
        cv2.rectangle(frame, (x, y),(x+w,y+h),(255,0,0),4)
    
    cv2.putText(frame,f'Jumlah Orang: {count}',(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)    
        
def close():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = camera.read()
        frame = cv2.flip(frame,1)
        box(frame)
        cv2.imshow("Human",frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            close()
            
if __name__ == '__main__':
    main()
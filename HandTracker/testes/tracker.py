import cv2
import mediapipe as mp
import time
import numpy as np
import pyautogui

#######

CAM_WIDTH, CAM_HEIGHT = 680, 480
CAM_FPS = 100
MAX_HANDS = 2
SMOTHENING = 3
SCREEN_LIMIT = 2

######

class HandTracker():
    
    def __init__(self, ):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=MAX_HANDS)
        self.fingertipId = [4, 8, 12, 16, 20]
        self.click = 0
        

    def findHands(self, image, draw=True):
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                    
        return image

    def findPosition(self, img, hand=0, draw=True):
        yList = []
        xList = []
        delimiter = []
        self.handTrack = []
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[hand]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.handTrack.append([id, cx, cy])
                
                if draw:
                    cv2.circle(img, (cx, cy), 5, (0,255,0), cv2.FILLED)

        if xList and yList:
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            delimiter = xmin, ymin, xmax, ymax
            
            if draw:
                cv2.rectangle(img, 
                    (xmin - 20, ymin - 20), 
                    (xmax + 20, ymax + 20), 
                    (70,130,180), 2)
            
        return self.handTrack, delimiter
    
    
    def fungersUp(self):
        # 1 Up
        # 0 Down
        fingers = []
        click_movement = self.handTrack[self.fingertipId[0]][1] <= self.handTrack[self.fingertipId[0]-1][1]
        
        # self.handTrack[posiçaõ do dedo (na doc tem os ids)][eixo (id, x, y, z)]
        # Thumb
        fingers.append(1)
        if click_movement:
            if self.click == 0:
                self.click = 1
                fingers[0] = 0
        else:
            self.click = 0

        # if self.handTrack[self.fingertipId[0]][1] > self.handTrack[self.fingertipId[0]-1][1]:
        #     self.click = 0
        #     fingers.append(1)
        # else:
        #     self.click = 1
        #     fingers.append(0)
            
            
        # Others Fingers
        for id in range(1, 5):
            if self.handTrack[self.fingertipId[id]][2] < self.handTrack[self.fingertipId[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
                
        return fingers


def main():
    pTime = 0
    cTime = 0
    plocX,plocY = 0,0
    clocX,clocy = 0,0

    cap = cv2.VideoCapture(0)
    cap.set(3, CAM_WIDTH)
    cap.set(4, CAM_HEIGHT)
    cap.set(5, CAM_FPS)
    
    if not cap.isOpened():
        print("Não foi possível acessar a câmera")
        exit()

    screenWidth, screenHeight = pyautogui.size()
    handTracker = HandTracker()
    
    while True:
        success, image = cap.read()
        
        image = handTracker.findHands(image)
        handTrack, delimiter = handTracker.findPosition(image)

        # Track Finger 4
        # if len(handTrack) != 0:
        #     print(handTrack[4])
            
        # FPS
        # cTime = time.time()
        # fps = 1 / (cTime - pTime)
        # pTime = cTime

        # cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
        #             (255, 0, 255), 3)
        
        if len(handTrack) != 0:
            
            x1, y1 = handTrack[8][1:]  # Posição do dedo indicador (ponto 8)
            x2, y2 = handTrack[12][1:]  # Posição do dedo médio (ponto 12)
            fingers = handTracker.fungersUp()

            cv2.rectangle(image, (CAM_FPS, CAM_FPS), (CAM_WIDTH - CAM_FPS, CAM_HEIGHT - CAM_FPS), (255,0,0), 2)
            
            # Move o mouse caso os dedos, indicador e médio, estiver levantado
            if fingers[1] == 1 and fingers[2] == 0:
                x3 = np.interp(x1,(CAM_FPS, CAM_WIDTH-CAM_FPS),(0, screenWidth))
                y3 = np.interp(y1, (CAM_FPS, CAM_HEIGHT-CAM_FPS), (0, screenHeight))
                
                # Smoothing
                clocX = plocX + (x3 - plocX) / SMOTHENING
                clocY = plocY + (y3 - plocY) / SMOTHENING
                
                # Moving Cursor
                x = min(max(screenWidth - clocX, SCREEN_LIMIT), screenWidth - SCREEN_LIMIT)
                y = min(max(clocY + (clocY * 0.25), SCREEN_LIMIT), screenHeight - SCREEN_LIMIT)
                
                pyautogui.moveTo(x, y)
                cv2.circle(image, (x1,y1),15,(255,0,0),cv2.FILLED)
                plocX,plocY = clocX,clocY

                if fingers[0] == 0:
                    pyautogui.click()
                    print('click')
                    

        cv2.imshow('HandTrancker', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
import cv2
import mediapipe as mp
import numpy as np
import robot_arm
import time

x = [90,90,90,90,90,90]
i = 0

def calculate_angle(a,b,c = ""):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

def extract_angles():
    global x

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    mp_pose = mp.solutions.pose
    mp_hands = mp.solutions.hands


    cap = cv2.VideoCapture(0)
    ## Setup mediapipe instance

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5,model_complexity = 0) as pose:
        with mp_hands.Hands(max_num_hands = 2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            while cap.isOpened():
                ret, frame = cap.read()
        
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
          
                # Make detection
                results = pose.process(image)
                hand_results = hands.process(image)
    
                  # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                
                    hand_landmarks = hand_results.multi_hand_landmarks
                    landmarks = results.pose_landmarks.landmark
                
                    hand = -1
                    # Get coordinates
                    left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    right_wrist = [hand_landmarks[hand].landmark[mp_hands.HandLandmark.WRIST].x,hand_landmarks[hand].landmark[mp_hands.HandLandmark.WRIST].y]
                    right_pinky = [hand_landmarks[hand].landmark[mp_hands.HandLandmark.PINKY_TIP].x,hand_landmarks[hand].landmark[mp_hands.HandLandmark.PINKY_TIP].y]
                    right_index = [hand_landmarks[hand].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,hand_landmarks[hand].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y]
                    right_thumb = [hand_landmarks[hand].landmark[mp_hands.HandLandmark.THUMB_TIP].x,hand_landmarks[hand].landmark[mp_hands.HandLandmark.THUMB_TIP].y]          
                
                    # Calculate angles
                    right_elbow_angle = calculate_angle(right_shoulder, right_elbow, right_wrist) #this is the elbow on y axis      y3
                    right_shoulder_angle = calculate_angle(right_hip, right_shoulder, right_elbow)#this is the shoulder on y        y4
                    right_shoulder_angle_x = calculate_angle(left_shoulder, right_shoulder, right_elbow)#shoulder on the x axis     x2
                    right_wrist_angle = calculate_angle(right_elbow,right_wrist,right_index)                                    #   y2 
                    right_wrist_angle_x = calculate_angle(right_shoulder,right_index,right_thumb)        #                          x1
                    right_thumb_angle = calculate_angle(right_thumb,right_wrist,right_index)                                    #   y1

                   
                    # Visualize angles
                    cv2.putText(image, str(right_elbow_angle), tuple(np.multiply(right_elbow, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, str(right_shoulder_angle), tuple(np.multiply(right_shoulder, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, str(right_shoulder_angle_x), tuple(np.multiply(left_shoulder, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, str(right_wrist_angle), tuple(np.multiply(right_wrist, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, str(right_wrist_angle_x), tuple(np.multiply(right_pinky, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, str(right_thumb_angle), tuple(np.multiply(right_thumb, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                    

                except:
                    pass
                 
                          
                #render hand detections
                if hand_results.multi_hand_landmarks:
                    for hand_landmarks in hand_results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
            
                #Render detections pose
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) )
                
                #change 3/27/2024
                
                cv2.namedWindow("window",cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

                cv2.imshow('window', image)
                
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                    
                

                
                try:
                    
                   # x = [right_elbow_angle,right_shoulder_angle,right_shoulder_angle_x,right_wrist_angle,right_wrist_angle_x,right_thumb_angle]
                   x = [right_elbow_angle,right_shoulder_angle,right_shoulder_angle_x,right_wrist_angle,right_thumb_angle, right_wrist_angle_x]

                   global i
                   print(i, x)
                   i += 1
                    
                except:
                    pass
                
                
                robot_arm.setAngles(x)
                    
    cap.release()
    cv2.destroyAllWindows()
extract_angles()

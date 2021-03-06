import face_recognition
import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)

# Tải ảnh người cần nhận diện (đầu tiên là mình) va ma hoa anh do.
son_image = face_recognition.load_image_file("E:/python/nhandienkhuonmat/mau1.jpg")
son_face_encoding = face_recognition.face_encodings(son_image)[0]

# TẢI ẢNH CỦA ÔNG TRUMP Ở ĐÂY .
# trump_image = face_recognition.load_image_file("phucvinh.jpg")
# trump_face_encoding = face_recognition.face_encodings(trump_image)[0]
#tHÊM 1 NGƯỜI = CÁCH
"""
name_image = face_recognition.load_image_file("name.jpg")
name_face_encoding = face_recognition.face_encodings(name_image)[0]
"""

# Tạo 1 mang cac khuon mat da duoc ma hoa va ten
known_face_encodings = [
    son_face_encoding,
    # trump_face_encoding
]
known_face_names = [
    "MauTC",
    "Phuc Vinh"
]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"
        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
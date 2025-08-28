import cv2

def segment_characters(thresh_img):
    """ Segments characters using contours. Returns list of cropped char images. """
    chars = []
    contours, _ = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0]):
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 10 and h > 20:  # filter out noise
            char_img = thresh_img[y:y+h, x:x+w]
            char_img = cv2.resize(char_img, (28, 28))  # normalize size
            chars.append(char_img)
    return chars

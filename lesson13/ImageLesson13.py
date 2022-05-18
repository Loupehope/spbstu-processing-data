import numpy as np
from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Drivers.ReadDriver import *
from Drivers.HistogramModelDriver import *
from Drivers.PlotDriver import *
from PIL import Image, ImageFilter
import pythreshold.utils
import cv2
from Drivers.Stones import *
import imutils

from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage
import numpy as np
import imutils
import cv2

class ImageLesson13:

    @staticmethod
    def run():
        def start(image, original):
            shifted = image # cv2.pyrMeanShiftFiltering(image, 15, 41)

            loaded_image.update(shifted, '_shifted')
            ImageDisplayDriver.save(loaded_image)

            # convert the mean shift image to grayscale, then apply
            # Otsu's thresholding
            gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255,
                                   cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            loaded_image.update(thresh, '_thresh')
            ImageDisplayDriver.save(loaded_image)

            # compute the exact Euclidean distance from every binary
            # pixel to the nearest zero pixel, then find peaks in this
            # distance map
            D = ndimage.distance_transform_edt(thresh)
            localMax = peak_local_max(D, indices=False, min_distance=5, labels=thresh)
            # perform a connected component analysis on the local peaks,
            # using 8-connectivity, then appy the Watershed algorithm
            markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
            labels = watershed(-D, markers, mask=thresh)
            print("[INFO] {} unique segments found".format(len(np.unique(labels)) - 1))

            masks = np.zeros(gray.shape, dtype="uint8")
            masks = cv2.cvtColor(masks, cv2.COLOR_GRAY2RGB)

            stones = 0
            # loop over the unique labels returned by the Watershed
            # algorithm
            for label in np.unique(labels):
                # if the label is zero, we are examining the 'background'
                # so simply ignore it
                if label == 0:
                    continue
                # otherwise, allocate memory for the label region and draw
                # it on the mask
                mask = np.zeros(gray.shape, dtype="uint8")
                mask[labels == label] = 255
                # detect contours in the mask and grab the largest one
                cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                biggest_contour = max(cnts, key=cv2.contourArea)

                # cv2.drawContours(original, cnts, -1, (255, 0, 0), 1)

                area = cv2.contourArea(biggest_contour)
                x, y, w, h = cv2.boundingRect(biggest_contour)

                if int(w) == 8 and int(h) == 8:
                    # Draw the rectangle
                    cv2.rectangle(original, (x, y), (x + w, y + h), (255, 0, 0), 1)
                    cv2.rectangle(masks, (x, y), (x + w, y + h), (255, 255, 255), thickness=-1)
                    stones += 1
                # if int(w) < 6 and int(h) == 6 and 7 < int(area) <= 30:
                #     # Draw the rectangle
                #     cv2.rectangle(original, (x, y), (x + w, y + h), (255, 0, 0), 1)
                #     cv2.rectangle(masks, (x, y), (x + w, y + h), (255, 255, 255), thickness=-1)
                #     stones += 1
                # elif int(h) < 6 and int(w) == 6 and 7 < int(area) <= 30:
                #     # Draw the rectangle
                #     cv2.rectangle(original, (x, y), (x + w, y + h), (255, 0, 0), 1)
                #     cv2.rectangle(masks, (x, y), (x + w, y + h), (255, 255, 255), thickness=-1)
                #     stones += 1

            loaded_image.update(masks, '_mask')
            ImageDisplayDriver.save(loaded_image)
            loaded_image.update(original, '_final')
            ImageDisplayDriver.save(loaded_image)

            return stones

        loaded_image = SPDImage.fromFile('lesson13/', 'stones', '.jpg', np.uint8)
        loaded_image.modified_image = np.array(loaded_image.modified_image)
        original = loaded_image.copy()
        ImageModelDriver.log_correction(loaded_image, 1)
        ImageModelDriver.grayscale(loaded_image)
        loaded_image.update(loaded_image.modified_image.astype(np.uint8), '_original')

        ImageDisplayDriver.save(loaded_image)
        image = cv2.cvtColor(loaded_image.modified_image, cv2.COLOR_GRAY2RGB)
        original = cv2.cvtColor(original.modified_image, cv2.COLOR_GRAY2RGB)
        st = start(image, original)
        print(st)

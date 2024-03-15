# A42
# Image Averages

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the average RGB values of a region
def average(region):
    redAve = np.average(region[:, :, 0])
    greenAve = np.average(region[:, :, 1])
    blueAve = np.average(region[:, :, 2])

    return (redAve, greenAve, blueAve)

# Function to set RGB values of a region
def setRegion(region, r, g, b):
    region[:, :, 0] = r
    region[:, :, 1] = g
    region[:, :, 2] = b


def quarter(img2, levels):
    """
    Takes an image and the number of splits to make.
    Splits the image into regions (2**levels x 2**levels pieces)
    and averages each of these regions separately.
    Calls average() and setRegion() to average and set colors for the
    regions.
    """
    h = img2.shape[0]
    w = img2.shape[1]
    hReg = h // 2 ** levels
    wReg = w // 2 ** levels
    for i in range(2 ** levels):
        for j in range(2 ** levels):
            # Average the region:
            r, g, b = average(img2[i * hReg:(i + 1) * hReg, j * wReg:(j + 1) * wReg])
            setRegion(img2[i * hReg:(i + 1) * hReg, j * wReg:(j + 1) * wReg], r, g, b)

# Main function
def main():
    file = input('Enter image file name: ')         # imageAverages.png
    img = plt.imread(file)

    # Divides the image in 1/2, 1/4, 1/8, ... 1/2^8, and displays each:
    for i in range(8):
        img2 = img.copy()  # Make a copy to average
        quarter(img2, i)  # Split in half i times, and average regions

        plt.imshow(img2)  # Load our new image into pyplot
        plt.show()  # Show the image (waits until closed to continue)

    # Shows the original image:
    plt.imshow(img)  # Load image into pyplot
    plt.show()  # Show the image (waits until closed to continue)


# Allow script to be run directly:
if __name__ == "__main__":
    main()

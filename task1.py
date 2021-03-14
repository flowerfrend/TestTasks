import sys
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(format(sys.argv[1])) as file:
            sequence = [row.strip() for row in file]
        for i, item in enumerate(sequence):
            sequence[i] = int(item)

        print('%.2f' % round(np.percentile(sequence, 90), 2))
        print('%.2f' % round(np.median(sequence), 2))
        print('%.2f' % round(np.amax(sequence), 2))
        print('%.2f' % round(np.amin(sequence), 2))
        print('%.2f' % round(np.nanmean(sequence), 2))
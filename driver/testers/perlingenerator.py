import random
import cv2
import numpy as np
from time import sleep


PERLIN_SIZE = 900
SEED_START = 999
# Good Ones: 999

# // void perlin_setup() {
# //   for(unsigned int i = 0; i < PERLIN_SIZE; i++){
# //     randomSeed(PERLIN_SETUP_SEED + i);
# //     perlinSeed[i] = (float) random() / (float) RANDOM_MAX;
# //   }
# // }

def get_noise_array():

    noiseArray = []

    for i in range(PERLIN_SIZE):
        random.seed(SEED_START + i)
        noiseArray.append(random.random()) #use random.uniform to push it one way
    
    return noiseArray

def get_perlin_array(noiseArray, nOctaves, fBias):

    perlinArray = [0.0] * PERLIN_SIZE

    for x in range(PERLIN_SIZE):
        fNoise = 0.0
        fScaleAcc = 0.0
        fScale = 1.0
        # print(x)

        for o in range(nOctaves):
            nPitch = int(PERLIN_SIZE >> o)
            nSample1 = int((x / nPitch)) * nPitch
            nSample2 = int((nSample1 + nPitch) % PERLIN_SIZE)

            # print(nPitch, nSample1, nSample2)

            fBlend = (x - nSample1) / nPitch
            fSample = (1.0 - fBlend) * noiseArray[nSample1] + fBlend * noiseArray[nSample2]

            fScaleAcc += fScale
            fNoise += fSample * fScale
            fScale = fScale / fBias
            
        perlinArray[x] = fNoise / fScaleAcc
    
    return perlinArray

# // void Effect::_perlin_setup()
# // { 
# //   // _set1 are octaves
# //   byte nOctaves = _set1;
# //   // _set2 is bias
# //   float fBias = (float)_set2/100.0f;

# //   for (unsigned int x = 0; x < PERLIN_SIZE; x++)
# //   {
# //     float fNoise = 0.0f;
# //     float fScaleAcc = 0.0f;
# //     float fScale = 1.0f;

# //     for (int o = 0; o < nOctaves; o++)
# //     {
# //       int nPitch = PERLIN_SIZE >> o;
# //       int nSample1 = (x / nPitch) * nPitch;
# //       int nSample2 = (nSample1 + nPitch) % PERLIN_SIZE;

# //       float fBlend = (float)(x - nSample1) / (float)nPitch;

# //       float fSample = (1.0f - fBlend) * _perlinSeed[nSample1] + fBlend * + _perlinSeed[nSample2];

# //       fScaleAcc += fScale;
# //       fNoise += fSample * fScale;
# //       fScale = fScale / fBias;
# //     }

# //     // Scale to seed range
# //     _perlin_array[x] = fNoise / fScaleAcc;
# //   }
# // }


if __name__ == "__main__":
    noiseArray = get_noise_array()
    perlinArray = get_perlin_array(noiseArray, 9, 0.9)
    steptime = 200
    frame = np.zeros([500,500,1],dtype=np.uint8)

    # for f in perlinArray:
    #     print(f)
    #     frame.fill(int(f*255))
    #     cv2.imshow('Frame', frame)  
    #     # Press Q on keyboard to exit
    #     if cv2.waitKey(steptime) & 0xFF == ord('q'):
    #         break

    print(*perlinArray, sep="f, ")

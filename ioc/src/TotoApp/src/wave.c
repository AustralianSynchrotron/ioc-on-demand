#include <stdio.h>
#include <aSubRecord.h>
#include <registryFunction.h>
#include <epicsExport.h>
#include <stdlib.h>

#include <epicsMath.h>
#include <epicsTime.h>


static float randomFloatFromRange (float min, float max) {
  float v = (float)rand()/(float)(RAND_MAX);
  return (max - min) * v + min;
}


static long processWave (aSubRecord* record) {
  float* vala = (float*)record->vala;
  double velocity = .5;
  double vt = velocity * (double)time(NULL);
  int numWaves = 3;
  double noiseAmpl = .1;
  double signal, noise;
  long i;
  for (i = 0; i < record->nova; i++) {
    double x = (double)i / 100;
    signal = sin(x + vt) +
             sin(2 * x + vt + .1) +
             sin(3 * x + vt + .2);
    noise = randomFloatFromRange(-noiseAmpl, noiseAmpl);
    vala[i] = signal / numWaves + noise;
  }
  return 0;
}


epicsRegisterFunction(processWave);

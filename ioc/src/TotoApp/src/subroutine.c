#include <stdio.h>
#include <dbDefs.h>
#include <registryFunction.h>
#include <subRecord.h>
#include <alarm.h>
#include <recGbl.h>
#include <epicsExport.h>
#include <dbStaticLib.h>
#include <epicsMath.h>


static float randomFloatFromRange (float min, float max) {
  float v = (float)rand()/(float)(RAND_MAX);
  return (max - min) * v + min;
}


typedef long (*processMethod) (subRecord* record);


static long initSubroutine (subRecord* record, processMethod process) {
  record->val = 5.123;
  return 0;
}


static long processSubroutine (subRecord* record) {
  record->val += randomFloatFromRange(-.1, .1);
  record->udf = 0;
  return 0;
}


static long processReadback (subRecord* record) {
  double stepSize = .25;
  if (fabs(record->val - record->a) <= stepSize) {
    record->val = record->a;
  } else if (record->val < record->a) {
    record->val += stepSize;
  } else if (record->val > record->a) {
    record->val -= stepSize;
  }
  record->udf = 0;
  return 0;
}


epicsRegisterFunction(initSubroutine);
epicsRegisterFunction(processSubroutine);

epicsRegisterFunction(processReadback);

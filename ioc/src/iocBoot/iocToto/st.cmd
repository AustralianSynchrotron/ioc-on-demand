#!../../bin/linux-x86_64/Toto

## You may have to change Toto to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/Toto.dbd"
Toto_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("db/records.db","PREFIX=$(HOSTNAME)")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=icsHost"
epicsThreadSleep(1)

dbpf("$(HOSTNAME):LONG_STRING", "Once upon a time...")

TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = Toto
# Toto.dbd will be created and installed
DBD += Toto.dbd

# Toto.dbd will be made up from these files:
Toto_DBD += base.dbd

# Include dbd files from all support applications:
#Toto_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#Toto_LIBS += xxx

# Toto_registerRecordDeviceDriver.cpp derives from Toto.dbd
Toto_SRCS += Toto_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
Toto_SRCS_DEFAULT += TotoMain.cpp
Toto_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#Toto_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
Toto_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE


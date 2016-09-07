# Mosquitto-RPM

This repo contains the files used to build am RPM of the Mosquitto MQTT broker.

# Building a new RPM

ssh $BUILD_SERVER`
cd /usr/src/rpm`
# MAKE SURE THERE IS NOTHING TO SAVE HERE FIRST`
```
rm -rf \*

git clone git@github.com:myDevicesIoT/Mosquitto-RPM.git

cd /usr/src/rpm/SOURCES

sudo wget https://github.com/myDevicesIoT/mosquitto/archive/v1.4.10.tar.gz

cd ../`

sudo git clone https://github.com/myDevicesIoT/mosquitto.git

sudo tar xvzf SOURCES/v1.4.10.tar.gz

rm -rf mosquitto\*/.git\*

diff -uNr mosquitto-1.4.10 mosquitto > $SOURCES/$NEW_PATC_NAME.patch

rm -rf mosquitto\*

rpmbuild -ba SPECS/mosquitto-1.4.10-1.spec
```

# Notes

* These instructions are based on using the official 1.4.10 source. If this base version changes, do not use any previous patches, and start from scratch.
* Do not commit any resulting files to this repo except for changes to __\*.spec__ and changes to or new __\*.patch__ files.

# Mosquitto-RPM

This repo contains the files used to build am RPM of the Mosquitto MQTT broker.

# Building a new RPM

```
ssh $BUILD_SERVER
git clone git@github.com:myDevicesIoT/Mosquitto-RPM.git

# build libwebsockets library that Mosquitto depends on first
rpmbuild -D '%_topdir %(echo $HOME)/Mosquitto-RPM' -ba $HOME/Mosquitto-RPM/SPECS/libwebsockets-2.1.0-1.spec --noclean

# build Mosquitto
cd SOURCES
wget https://github.com/myDevicesIoT/mosquitto/archive/v1.4.10.tar.gz
cd ../
git clone https://github.com/myDevicesIoT/mosquitto.git
tar xvzf SOURCES/v1.4.10.tar.gz
rm -rf mosquitto*/.git*
diff -uNr mosquitto-1.4.10 mosquitto > SOURCES/$NEW_PATCH_NAME.patch
rm -rf mosquitto*
# ADD NEW PATCH FILE(S) and COMMENTS, ETC.
vim SPECS/mosquitto-1.4.10-2.spec
# setting these allows to avoid installing libwebsockets packages on the build server
export CFLAGS="-I $HOME/Mosquitto-RPM/BUILDROOT/libwebsockets-2.1.0*/usr/include"
export LDFLAGS="-L $HOME/Mosquitto-RPM/BUILDROOT/libwebsockets-2.1.0*/usr/lib -L $HOME/Mosquitto-RPM/BUILDROOT/libwebsockets-2.1.0*/usr/lib64"
rpmbuild -D '%_topdir %(echo $HOME)/Mosquitto-RPM' -ba $HOME/Mosquitto-RPM/SPECS/mosquitto-1.4.10-2.spec
```

# Notes

* These instructions are based on using the official 1.4.10 source. If this base version changes, do not use any previous patches, and start from scratch.
* Do not commit any resulting files to this repo except for changes to __\*.spec__ and changes to or new __\*.patch__ files.

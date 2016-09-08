Summary: Mosquitto Broker build
Name: mosquitto
Version: 1.4.10
Release: 1
License: GPL
Group: System Environment/Base
Source: https://github.com/myDevicesIoT/mosquitto/archive/v1.4.10.tar.gz
Patch0: mosquitto-disconnect-notification.patch

%description
Mosquitto MQTT Broker

%prep
%setup -q
%patch0 -p1 -b .buildroot

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall

%clean
[ $RPM_BUILD_ROOT != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/libmosquitto.so.1
/usr/lib/libmosquitto.so
/usr/include/mosquitto.h
/usr/lib/libmosquittopp.so.1
/usr/lib/libmosquittopp.so
/usr/include/mosquittopp.h
/usr/bin/mosquitto_pub
/usr/bin/mosquitto_sub
/usr/sbin/mosquitto
/usr/include/mosquitto_plugin.h
/usr/bin/mosquitto_passwd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Tue Sep 6 2016 David Achenbach <dachenbach@mydevices.com>
- Patch added to notify on disconnect

* Tue Sep 6 2016 David Achenbach <dachenbach@mydevices.com>
- RPM build directly from mosquitto 1.4.10 source

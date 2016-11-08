# pkg-libmicrohttpd
RPM packaging of libmicrohttpd for Sailfish

To get the sources, run download.sh

To build and install:

export SFARCH=armv7hl; mb2 -t SailfishOS-$SFARCH -s ../rpm/libmicrohttpd.spec build

export SFARCH=armv7hl; sb2 -t SailfishOS-$SFARCH -m sdk-install -R rpm -i ../../rpms/devel/libmicrohttpd*$SFARCH.rpm

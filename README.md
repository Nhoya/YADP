# YADP
Yet Another xDelta Patcher

![alt tag](http://i.imgur.com/hy9eyIW.png)

YADP is the first front end for xDelta3 running on Linux.

Actually YADP is able to patch ROMS without any problems.

## How to install:

Before starting you need to install:

**yad, xdelta3 and awk**

### Ubuntu based distro:

```
apt-get install yad xdelta3 awk
```
### Debian <= 8 and others distros without yad in the repos:

yad is officially in the repository of Debian starting from Debian 9 so if you are running a version of debian <= 8 you have to compile it from source,
go to https://code.google.com/p/yad/downloads and download the latest source version.

yad depends on **libgtk3-dev initltool** so make sure they are installed.

#### Extract the archive:

```
tar xf yad-x.x.x.tar.xz && cd yad-x.x.x
```

#### Run the configuration script:

```
./configure
```

#### Build:

```
make && sudo make install
```

Or, if you don't like or are not able to compile just download and install the pre-compiled package from here: 
http://pkgs.org/download/yad

## Running YADP:

After solving the dependencies just clone the repo 

```
git clone https://github.com/em-s-h/YADP.git
```
```
cd YADP && chmod +x YADP
```
and double click on the YADP file to run it.

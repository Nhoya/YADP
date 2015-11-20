# YADP
Yet Another xDelta Patcher

![alt tag](http://i.imgur.com/hy9eyIW.png)

YADP is the first front end for xDelta3 running on Linux.

Actually YADP is able to patch ROMS without problem. ASAP i'l start working on patch generator


####How to install:

before starting you need to install:

**yad, xdelta3 and awk**

##Ubuntu Based Distro

```
apt-get install yad xdelta3 awk
```
##Debian <= 8 and others distros without yad in the repos

yad is officially in the repository of Debian starting from Debian 9 so if you are running a version of debian <= 8 you have to compile it from source
so go here https://code.google.com/p/yad/downloads and downlaod latest source version

#solve dependencies for yad:

**libgtk3-dev initltool** 

extract the archive

```
tar xf yad-x.x.x.tar.xz && cd yad-x.x.x
```

running the configuration script

```
./configure
```
building

```
make && sudo make install
```
Or, if you don't like or are not able to compile just download and install the pre-compiled package from here
http://pkgs.org/download/yad

After solving dependencies just clone the repo 

```
git clone https://github.com/Nhoya/YADP
```
```
cd YADP && chmod +x YADP
```
double click on the YADP file to run it.

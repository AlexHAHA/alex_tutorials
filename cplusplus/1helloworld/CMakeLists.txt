cmake_minimum_required(VERSION 3.4.1)
project(helloworld)



###########
## Build ##
###########
# generate executable file
add_executable(helloworld helloworld.cpp)

# generate static library: libcommon.a
#add_library(common STATIC helloworld.cpp)
# generate dynamic or shared library: libcommon.a libcommon.so
add_library(common SHARED helloworld.cpp)


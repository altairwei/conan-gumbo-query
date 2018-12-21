cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Gumbo REQUIRED)

add_executable(example example.cpp)
include_directories(example ${Gumbo_INCLUDE_DIRS}/gumbo-parser)
target_link_libraries(example ${CONAN_LIBS})

cmake_minimum_required(VERSION 3.24)
project(
        Lab1
        LANGUAGES CXX
        DESCRIPTION "Rozwiązanie problemu RPQ"
)
set(CMAKE_CXX_STANDARD 17)

add_executable(
        Lab1
        main.cpp
        include/Proces.h
        include/Proces.cpp
        include/Shrage.h
        include/Shrage.cpp
)

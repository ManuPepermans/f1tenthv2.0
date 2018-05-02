# Install script for directory: /home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/src/purepursuit

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/purepursuit/cmake" TYPE FILE FILES "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/build/purepursuit/catkin_generated/installspace/purepursuit-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/devel/share/roseus/ros/purepursuit")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/devel/lib/python2.7/dist-packages/purepursuit")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/devel/lib/python2.7/dist-packages/purepursuit")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/build/purepursuit/catkin_generated/installspace/purepursuit.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/purepursuit/cmake" TYPE FILE FILES "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/build/purepursuit/catkin_generated/installspace/purepursuit-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/purepursuit/cmake" TYPE FILE FILES
    "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/build/purepursuit/catkin_generated/installspace/purepursuitConfig.cmake"
    "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/build/purepursuit/catkin_generated/installspace/purepursuitConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/purepursuit" TYPE FILE FILES "/home/jonas/Git/MAP2018/ROS/WS_Nav_PurePursuit/src/purepursuit/package.xml")
endif()


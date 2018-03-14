# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "stablev: 3 messages, 0 services")

set(MSG_I_FLAGS "-Istablev:/home/manupepermans/F1tenthRev2/src/stablev/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(stablev_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg" NAME_WE)
add_custom_target(_stablev_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "stablev" "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg" ""
)

get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg" NAME_WE)
add_custom_target(_stablev_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "stablev" "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg" ""
)

get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg" NAME_WE)
add_custom_target(_stablev_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "stablev" "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/stablev
)
_generate_msg_cpp(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/stablev
)
_generate_msg_cpp(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/stablev
)

### Generating Services

### Generating Module File
_generate_module_cpp(stablev
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/stablev
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(stablev_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(stablev_generate_messages stablev_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg" NAME_WE)
add_dependencies(stablev_generate_messages_cpp _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg" NAME_WE)
add_dependencies(stablev_generate_messages_cpp _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg" NAME_WE)
add_dependencies(stablev_generate_messages_cpp _stablev_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(stablev_gencpp)
add_dependencies(stablev_gencpp stablev_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS stablev_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/stablev
)
_generate_msg_eus(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/stablev
)
_generate_msg_eus(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/stablev
)

### Generating Services

### Generating Module File
_generate_module_eus(stablev
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/stablev
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(stablev_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(stablev_generate_messages stablev_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg" NAME_WE)
add_dependencies(stablev_generate_messages_eus _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg" NAME_WE)
add_dependencies(stablev_generate_messages_eus _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg" NAME_WE)
add_dependencies(stablev_generate_messages_eus _stablev_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(stablev_geneus)
add_dependencies(stablev_geneus stablev_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS stablev_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/stablev
)
_generate_msg_lisp(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/stablev
)
_generate_msg_lisp(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/stablev
)

### Generating Services

### Generating Module File
_generate_module_lisp(stablev
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/stablev
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(stablev_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(stablev_generate_messages stablev_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg" NAME_WE)
add_dependencies(stablev_generate_messages_lisp _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg" NAME_WE)
add_dependencies(stablev_generate_messages_lisp _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg" NAME_WE)
add_dependencies(stablev_generate_messages_lisp _stablev_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(stablev_genlisp)
add_dependencies(stablev_genlisp stablev_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS stablev_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/stablev
)
_generate_msg_nodejs(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/stablev
)
_generate_msg_nodejs(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/stablev
)

### Generating Services

### Generating Module File
_generate_module_nodejs(stablev
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/stablev
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(stablev_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(stablev_generate_messages stablev_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg" NAME_WE)
add_dependencies(stablev_generate_messages_nodejs _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg" NAME_WE)
add_dependencies(stablev_generate_messages_nodejs _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg" NAME_WE)
add_dependencies(stablev_generate_messages_nodejs _stablev_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(stablev_gennodejs)
add_dependencies(stablev_gennodejs stablev_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS stablev_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/stablev
)
_generate_msg_py(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/stablev
)
_generate_msg_py(stablev
  "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/stablev
)

### Generating Services

### Generating Module File
_generate_module_py(stablev
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/stablev
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(stablev_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(stablev_generate_messages stablev_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/pid_input.msg" NAME_WE)
add_dependencies(stablev_generate_messages_py _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_values.msg" NAME_WE)
add_dependencies(stablev_generate_messages_py _stablev_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/manupepermans/F1tenthRev2/src/stablev/msg/drive_param.msg" NAME_WE)
add_dependencies(stablev_generate_messages_py _stablev_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(stablev_genpy)
add_dependencies(stablev_genpy stablev_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS stablev_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/stablev)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/stablev
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(stablev_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/stablev)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/stablev
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(stablev_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/stablev)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/stablev
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(stablev_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/stablev)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/stablev
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(stablev_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/stablev)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/stablev\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/stablev
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(stablev_generate_messages_py std_msgs_generate_messages_py)
endif()

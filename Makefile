# Makefile

# defaults
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl

VHDL_SOURCES += $(PWD)/2_and.hdl
VHDL_SOURCES += $(PWD)/3_and.hdl
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = threeand

# MODULE is the basename of the Python test file
MODULE = main

include $(shell cocotb-config --makefiles)/Makefile.sim
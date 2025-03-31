# Makefile

# defaults
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl

VHDL_SOURCES += $(PWD)/alu.hdl
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = alu

# MODULE is the basename of the Python test file
MODULE = main

EXTRA_ARGS?=--ieee=synopsys
EXTRA_ARGS+=-fexplicit
EXTRA_ARGS+=-fsynopsys

include $(shell cocotb-config --makefiles)/Makefile.sim
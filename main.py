from math import floor

import cocotb
from cocotb.triggers import Timer

async def step():
    """Take one step in time"""
    await Timer(1, units="ns")

@cocotb.test()
async def my_first_test(dut):
    """Try accessing the design."""
    print(dir(dut.a1))
    for i in range(0,8):
        dut.i1.value = i&1 == 1
        dut.i2.value = i&2 == 2
        dut.i3.value = i&4 == 4
        await step()
        print(i,":", dut.i3.value,"&",dut.i2.value,"&",dut.i1.value,"==", (dut.i1.value and dut.i2.value and dut.i3.value), "==", dut.and_result.value)
        assert dut.and_result.value == (dut.i1.value and dut.i2.value  and dut.i3.value), "all and gate tests"

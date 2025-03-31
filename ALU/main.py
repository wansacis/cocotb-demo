import math
from math import floor
from random import random

import cocotb
from cocotb.triggers import Timer

async def step():
    """Take one step in time"""
    await Timer(1, units="ns")

iterations = 50000

def number(a):
    b = 3
    while b == 3:
        b = math.floor(random() * a)
    return b

def assignAB(dut):
    dut.A.value = number(255)
    if dut.ALU_Sel != 0:
        dut.B.value = number(254) + 1
    else:
        dut.B.value = number(255)

@cocotb.test()
async def CARRYOUT(dut):
    for i in range(iterations):
        dut.ALU_Sel.value = number(15)
        assignAB(dut)
        await step()
        assert dut.Carryout == (dut.A.value + dut.B.value > 255), "Carryout wrong"


@cocotb.test()
async def ALU_SEL0_ADDITION(dut):
    dut.ALU_Sel.value = 0

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value + dut.B.value)%256 , "Addition failed!"

@cocotb.test()
async def ALU_SEL1_SUBTRACTION(dut):
    dut.ALU_Sel.value = 1

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value - dut.B.value)%256 , "Subtraction failed!"

@cocotb.test()
async def ALU_SEL2_MULTIPLIKATION(dut):
    dut.ALU_Sel.value = 2

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value * dut.B.value) % 256, "Multiplication failed!"

@cocotb.test()
async def ALU_SEL3_DIVISION(dut):
    dut.ALU_Sel.value = 3

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == floor((dut.A.value+0) / (dut.B.value+0)) % 256, "Division failed!"

@cocotb.test()
async def ALU_SEL4_SHIFT_L(dut):
    dut.ALU_Sel.value = 4

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value << 1)&255, "Left Shift failed!"

@cocotb.test()
async def ALU_SEL5_SHIFT_R(dut):
    dut.ALU_Sel.value = 5

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value >> 1), "Right Shift failed!"

@cocotb.test()
async def ALU_SEL6_ROTATE_L(dut):
    dut.ALU_Sel.value = 6

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value << 1 | dut.A.value >> 7)&255, "Left Rotate failed!"

@cocotb.test()
async def ALU_SEL7_ROTATE_R(dut):
    dut.ALU_Sel.value = 7

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value << 7 | dut.A.value >> 1) & 255, "Right Rotate failed!"

@cocotb.test()
async def ALU_SEL8_AND(dut):
    dut.ALU_Sel.value = 8

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value & dut.B.value), "AND failed!"

@cocotb.test()
async def ALU_SEL9_OR(dut):
    dut.ALU_Sel.value = 9

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value | dut.B.value), "OR failed!"

@cocotb.test()
async def ALU_SEL10_XOR(dut):
    dut.ALU_Sel.value = 10

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value ^ dut.B.value), "XOR failed!"

@cocotb.test()
async def ALU_SEL11_NOR(dut):
    dut.ALU_Sel.value = 11

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == ((dut.A.value | dut.B.value) ^ 255), "NOR failed!"

@cocotb.test()
async def ALU_SEL12_NAND(dut):
    dut.ALU_Sel.value = 12

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == ((dut.A.value & dut.B.value) ^ 255), "NOR failed!"

@cocotb.test()
async def ALU_SEL13_XNOR(dut):
    dut.ALU_Sel.value = 13

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == ((dut.A.value ^ dut.B.value) ^ 255), "XNOR failed!"

@cocotb.test()
async def ALU_SEL14_GREATER(dut):
    dut.ALU_Sel.value = 14

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value+127 > dut.B.value+127), "Greater failed!"

@cocotb.test()
async def ALU_SEL15_EQUAL(dut):
    dut.ALU_Sel.value = 15

    for i in range(iterations):
        assignAB(dut)
        await step()
        assert dut.ALU_Out.value == (dut.A.value == dut.B.value), "Equal failed!"
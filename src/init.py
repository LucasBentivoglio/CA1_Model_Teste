#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:48:06 2021

@author: adam
"""
# from neuron import h
# h.nrnmpi_init()

from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='src/cfg.py', 
                                           netParamsDefault='src/netParams.py')

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

sim.pc.done()
#import sys
#sys.exit()
# h.quit()

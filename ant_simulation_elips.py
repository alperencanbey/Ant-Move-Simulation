#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:06:04 2024

@author: Alperen Canbey
"""

import numpy as np

def is_outside_boundary(x, y):
    return ((x - 2.5) / 30) ** 2 + ((y - 2.5) / 40) ** 2 >= 1

def simulate_ant_movement(iterations):
    directions = np.array([[10, 0], [-10, 0], [0, 10], [0, -10]])  # East, West, North, South movements
    times = []
    
    for _ in range(iterations):
        x, y = 0, 0  # Starting position
        time = 0
        
        while not is_outside_boundary(x, y):
            dx, dy = directions[np.random.randint(0, 4)]  # Choose a random direction
            x += dx
            y += dy
            time += 1  # Increment time by 1 second for each move
            
        times.append(time)
    
    return np.mean(times)

# Estimate the average time with a large number of iterations for better accuracy
average_time = simulate_ant_movement(1000)  # Using 10,000 iterations for the simulation

average_time

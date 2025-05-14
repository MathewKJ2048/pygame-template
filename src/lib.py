"""
Used to store everything of general interest, accessible everywhere
"""

from conf import *
from colors import *
from wireframe import *
import random
import math
from pathlib import Path

import pygame
from pygame import Vector3

I = Vector3(1,0,0)
J = Vector3(0,1,0)
K = Vector3(0,0,1)
O = Vector3(0,0,0)

PI = math.pi
TAU = 2*PI
cos = math.cos
sin = math.sin

CLOCK = pygame.time.Clock()

debug_transcript = {}
message_log = {}

def get_debug_transcript():
	global debug_transcript
	return debug_transcript

def log(key,value):
	global debug_transcript
	debug_transcript[key]=value

def pri(message):
	global message_log
	if message in message_log:
		message_log[message] = 1
	else:
		message_log[message]+=1

# Use physics convention for theta and phi
def unit_vector(theta,phi=PI/2):
	return sin(phi)*(cos(theta)*I + sin(theta)*J)+cos(phi)*K

def rotate(v,theta,phi=0):
	r = math.sqrt(v.x*v.x+v.y*v.y)
	t = math.atan2(v.y,v.x)
	p = math.atan2(r,v.z)
	return unit_vector(t+theta,p+phi)



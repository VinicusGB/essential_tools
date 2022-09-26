from asyncio import subprocess
from subprocess import os

def list_input_files(input):
    try: return os.listdir(input)
    except: []
def list_output_files(output):
    return os.listdir(output)
    #except: []

import streamlit as st
from datetime import *
import datetime
import time
import re
import sys
import os
import math

def y(d):
    w = []
    for variable in d:
        time = 0
        if len(variable)!= 0:
            k=list(variable)
            if variable[0][2] == 'am' or variable[0][2] == 'aM' or variable[0][2] == 'Am' or variable[0][2] == 'AM' :
                if variable[1][2] == 'am' or variable[1][2] == 'aM' or variable[1][2] == 'Am' or variable[1][2] == 'AM' :
                    time = z(k)

            if variable[0][2] == 'am' or variable[0][2] == 'aM' or variable[0][2] == 'Am' or variable[0][2] == 'AM' :
                if variable[1][2] == 'pm' or variable[1][2] == 'pM' or variable[1][2] == 'Pm' or variable[1][2] == 'PM' :
                    time = f(k)
                   
            if variable[0][2] == 'pm' or variable[0][2] == 'pM' or variable[0][2] == 'Pm' or variable[0][2] == 'PM' :
                if variable[1][2] == 'pm' or variable[1][2] == 'pM' or variable[1][2] == 'Pm' or variable[1][2] == 'PM' :
                    time = z(k)            
                                          
            if variable[0][2] == 'pm' or variable[0][2] == 'pM' or variable[0][2] == 'Pm' or variable[0][2] == 'PM' :
                if variable[1][2] == 'am' or variable[1][2] == 'aM' or variable[1][2] == 'Am' or variable[1][2] == 'AM' :
                    time = i(k)          
           
           
            w.append(time)
    x = 0
    for variable in w:
        x = x + variable
    return x

       


def q(d):
    log_d = []
    for variable in d:
        l = re.findall(r'([01][0-9]|[0-9]):([0-5][0-9]|[0-9])([apAP][mM])',variable)
        log_d.append(l)
    return log_d    


   
       
def z(k):
    hour1 = int(k[1][0])
    hour0 = int(k[0][0])
    min1 = int(k[1][1])
    min0 = int(k[0][1])
    time=0
           
    if(hour0 == 12):
        if(hour1 != 12):
            hour1 = hour1 + 12
    if(hour0 < hour1):
        time = time + (hour1 - hour0)*60
    else:
        if(hour0 == hour1):
            time = 0
        else:
            time = time + (hour0 - hour1)*60

    if(min1 > min0):
        time = time + (min1 - min0)
    else:
        time = time - (min0 - min1)
            
    return time

   
def i(k):
    min0 = int(k[0][1])
    hour1 = int(k[1][0])
    min1 = int(k[1][1])
    hour0 = int(k[0][0])
    time=0
    if(min1 > min0):
        time = time + (min1 - min0)
    else:
        time = time - (min0 - min1)
           
    if(hour0 == 12):
        hour1 = hour1 - 12
    if(hour1 != 12):
            hour1 = hour1 + 12
    if(hour0 < hour1):
        time = time + (hour1 - hour0)*60
    else:
        if(hour0 == hour1):
            time = 0
        else:
            time = time + (hour0 - hour1)*60
                           
    return time


 
def j(time):
    rh = time/60
    fh = math.floor(rh)
    cm = math.ceil((rh - fh)*60)
    rd = math.floor(rh/24)
    h = math.floor((((time/60)/24)-rd)*24)
    mins = math.ceil((((((time/60)/24)-rd)*24)-h)*60)
    if(h == 0):
        st.write(f"{fh}hours {cm}minutes -- {time} minutes -- {rd}days {mins}minutes -- {rh}hours")
    else:
        st.write(f"{fh}hours {cm}minutes -- {time} minutes -- {rd}days {h}hours {mins}minutes -- {rh}hours")
   


def f(k):
    min0 = int(k[0][1])
    hour0 = int(k[0][0])
    hour1 = int(k[1][0])
    min1 = int(k[1][1])
    time=0
    if(min1 > min0):
        time = time + (min1 - min0)
    else:
        time = time - (min0 - min1)
    if(hour0 == 12):
        hour1 = hour1 - 12
    if(hour1 != 12):
        hour1 = hour1 + 12
    if(hour0 < hour1):
        time = time + (hour1 - hour0)*60
    else:
        if(hour0 == hour1):
            time = 0
        else:
            time = time + (hour0 - hour1)*60
    return time   


def parse(filename):
    d = open(filename, "r")
    changed = q(d)
    xy = y(changed)
    j(xy)

if __name__ == "__main__":

    st.title("Time log parser")
    background = "background.jpg"
    background_ext = "jpg"

    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #87ceeb;
        color:black;
    }
    div.stButton > button:hover {
        background-color: white;
        color:black;
        border: 2px solid #87ceeb;
        }
    </style>""", unsafe_allow_html=True)
    left, right = st.columns(2)

    with left:
        option = st.selectbox(
            'Please select a time log file from the dropdown.',
            ('Carbon.txt', 'TimeLogEnergy.txt', 'TimeLogNitrogen.txt', 'TimeLogWater.txt', 'TimeLogWatershed.txt', 'TimeParser.txt', 'correctcases.txt', 'errorcase.txt'))
        st.write('You selected:', option)

    with right:
        st.empty()

    one, two, three = st.columns(3)
    with one:
        submit = st.button('Submit')
    with two:
        reset = st.button('Reset')
    with three:
        st.empty()
    if submit:
        if not option:
            st.write("Not Found")
        else:
            parse(option)

    if reset:
        option = ""
        st.empty()
        st.write("Your selection has been reset")

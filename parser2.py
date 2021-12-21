import streamlit as st
from datetime import *
import datetime
import time


def file_in(inputFilename):
    dataOut = []
    fileValues = open(inputFilename, "r")
    dataOut.extend(fileValues.readlines())
    fileValues.close()
    return dataOut


def format(timeData):
    try:
        time.strptime(timeData, '%I:%M%p')
        return "Y"
    except ValueError:
        return "N"


def total_time(time_data):
    logTime = datetime.timedelta()
    for i in time_data:
        v1 = datetime.datetime.strptime(i[1], "%I:%M%p")
        v2 = datetime.datetime.strptime(i[0], "%I:%M%p")
        v1_v2 = (v1 - v2)
        if str(v1_v2).count('day') != 0:
            countInitial = "00:00:00"
            dayCount = (str(v1_v2).split(",")[1].strip())
            v4 = datetime.datetime.strptime(countInitial, "%H:%M:%S")
            v3 = datetime.datetime.strptime(dayCount, "%H:%M:%S")
            v3_v4 = (v3 - v4)
            logTime += v3_v4
        else:
            logTime += v1_v2
    sec = logTime.total_seconds()
    mins, sec = divmod(sec, 60)
    hour, mins = divmod(mins, 60)
    return "Total Time Taken is : {} hours {} minutes {} seconds".format(hour, mins, sec)


def get_time_log(fileValues):
    timeTotalValue = []
    lineCheck = ''
    for line, linedata in enumerate(fileValues):
        if linedata.strip('\n').count("Time Log:"):
            lineCheck = line
            break
        else:
            lineCheck = 'TimeLog'
    if lineCheck != "TimeLog":
        for pointer in range(int(lineCheck) + 1, len(fileValues)):
            entry = (fileValues[pointer].split(' - ')[0].split())
            end = (fileValues[pointer].split(' - ')[1:])
            counter = (fileValues[pointer].split(' - ')[1:])
            if len(entry) != 0:
                timeCheckValue = format(entry[-1].strip())
                if len(counter) != 0:
                    timeformatstatus_v1 = format(end[0].split()[0])
                    if timeformatstatus_v1 == "Y" and timeCheckValue == "Y":
                        timeTotalValue.append((entry[-1], str(end[0].split()[0])))
                else:
                    print("No time value in line number : ", pointer + 1)
            else:
                print("No time value in line number : ", pointer + 1)
        return total_time(timeTotalValue)
    else:
        return "There is no Time Log in the file"


def parse(filename):
    file_data = file_in(inputFilename=filename)
    return get_time_log(fileValues=file_data)


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
            total_log = parse(option)
            st.write(total_log)

    if reset:
        option = ""
        st.empty()
        st.write("Your selection has been reset")

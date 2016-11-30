import json
import os
import shutil

allBeersIdName = []

toReplace = ["xxxhdpi","xxhdpi","xhdpi","hdpi","ldpi","mdpi"]
folders = ["drawable-xxxhdpi","drawable-xxhdpi","drawable-xhdpi","drawable-hdpi","drawable-ldpi","drawable-mdpi"]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
    for filename in os.listdir(os.getcwd()):
        fileToMove = folder.replace("drawable-","") + ".png"
        if fileToMove in filename:
             print os.getcwd()+"\\"+folder+"\\"+filename
             shutil.move(os.getcwd()+"\\"+filename, os.getcwd()+"\\"+folder+"\\glass"+filename.replace(folder.replace("drawable-",""),""))
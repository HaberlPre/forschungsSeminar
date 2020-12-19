# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 09:54:42 2020

@author: lucas
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('umfrage.csv')
npdf = df.to_numpy()

"""
0"Zeitstempel",
1"Bitte geben Sie Ihr Geschlecht an:",
2"Bitte wählen Sie ihre Altersgruppe",
3"In welcher Rolle sind Sie an der Universität Regensburg tätig?",
4"Welcher Fakultät gehören Sie an?",
5"Zu welchem Lehrstuhl gehören Sie?",
6"Welche Art von Computer benutzen Sie für die Online-Lehre?",
7"Was für eine Kamera benutzen Sie für die Online-Lehre?",
8"Was für ein Mikrofon benutzen Sie für die Online-Lehre?",
9"Welche weitere Hardware benutzen Sie für Online-Lehre?",
10"Wie gut schätzen Sie Ihre Erfahrung mit der vorhandenen Technik ein?",
11"Haben Sie sich aufgrund der aktuellen Situation im Bezug auf die Technik weitergebildet?",
12"Haben Sie sich aufgrund der aktuellen Situation neue Hardware angeschafft?",
13"Wenn es neue Anschaffungen gab,  wurden diese ...",
14"Verwenden Sie zusätzliche Software neben einer Videokonferenzsoftware?",
15"Erstellen / Streamen Sie Ihre Videos im Home-Office?",
16"Falls Ja: Wie schnell ist Ihr Internet im Home-Office?",
17"Haben Sie bereits vor der Corona-Pandemie Online-Kurse gehalten?",
18"Wie halten Sie Ihre Online-Kurse?",
19"Wenn Sie Ihre  Online-Kurse live halten, welche Elemente werden überwiegend übertragen?",
20"Wenn Sie Ihre  Online-Kurse als Aufnahme bereitstellen, welche Elemente werden darin  überwiegend gezeigt?",
21"Stellen Sie Ihren Hintergrund währen eines Online-Kurses frei?",
22"Welche Perspektive ähnelt der Perspektive Ihrer Kamera während einer Online-Vorlesung am Meisten?",
23"Haben Sie noch Anmerkungen zum Fragebogen oder zum Thema Online-Kurse?",
24"Falls Sie sich für anonymisierte & aufbereitete Ergebnisse dieser Studie interessieren,  können Sie hier Ihre E-Mail-Adresse hinterlegen und wir werden Ihnen diese zukommen lassen."
"""

#Gender
#gender = df["Bitte geben Sie Ihr Geschlecht an:"]
#geder_plot = df.plot.pie(y='Bitte geben Sie Ihr Geschlecht an:', figsize=(5,5))

gender = []
alter = []
rolle = []
fakultät = []
lehrstuhl = []
computer = []
cam = []
mic = []
other_hw = []
erfahrung = []
training = []
new_hw = []
bezahlt = []
other_sw = []
home_office = []
home_internet = []
pre_corona = []
wie_online = []
elemente = []
bereitstellen = []
hintergrund = []
perspektive = []
anmerkung = []
email = [] 

for i in npdf:
    gender.append(i[1])
    alter.append(i[2])
    rolle.append(i[3])
    fakultät.append(i[4])
    lehrstuhl.append(i[5])
    computer.append(i[6])
    cam.append(i[7])
    mic.append(i[8])
    other_hw.append(i[9])
    erfahrung.append(i[10])
    training.append(i[11])
    new_hw.append(i[12])
    bezahlt.append(i[13])
    other_sw.append(i[14])
    home_office.append(i[15])
    home_internet.append(i[16])
    pre_corona.append(i[17])
    wie_online.append(i[18])
    elemente.append(i[19])
    bereitstellen.append(i[20])
    hintergrund.append(i[21])
    perspektive.append(i[22])
    anmerkung.append(i[23])
    email.append(i[24])
        
def unique(list1): 
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        test_item = [x, 0]
        if test_item not in unique_list: 
            list_entry = [x, 0]
            unique_list.append(list_entry) 
    return unique_list

def do_bar_chart(list1, y_label, title):
    objects = []
    data = []
    for i in list1:
        objects.append(i[0])
        data.append(i[1])
    #y_pos = len(objects)
    #print(objects, data, y_pos)
    plt.bar(objects, data, align='center', alpha=0.5)
    plt.xticks(objects)
    plt.ylabel(y_label)
    plt.title(title)
    
    return plt

def do_pie_chart(list1, y_label, title):
    objects = []
    data = []
    for i in list1:
        objects.append(i[0])
        data.append(i[1])
    #y_pos = len(objects)
    #print(objects, data, y_pos)
    #plt.bar(objects, data, align='center', alpha=0.5)
    #plt.xticks(objects)
    #plt.ylabel(y_label)
    #plt.title(title)
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    explode_data = []
    for i in objects:
        explode_data.append(0)
    explode = explode_data  # only "explode" the 2nd slice (i.e. 'Hogs')
    
    fig1, ax1 = plt.subplots()
    ax1.pie(data, explode=explode, labels=objects, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    return plt

def do_boxplot(list1, y_label, title):
    #objects = []
    #data = []
    #for i in list1:
        #objects.append(i[0])
        #data.append(i[1])
    #y_pos = len(objects)
    #print(objects, data, y_pos)
    #plt.bar(objects, data, align='center', alpha=0.5)
    #plt.xticks(objects)
    #plt.ylabel(y_label)
    #plt.title(title)
    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.boxplot(list1)
    
    return plt

#gender
unique_gender = unique(gender)
for i in unique_gender:
    for j in gender:
        if i[0] == j:
            i[1] +=1
            
gender_plot = do_pie_chart(unique_gender, "", "Geschlechterverteilung")
gender_plot.show()

#alter
unique_age = unique(alter)
for i in unique_age:
    for j in alter:
        if i[0] == j:
            i[1] +=1
            
alter_plot = do_bar_chart(unique_age, "", "Altersverteilung")
alter_plot.show()

#rolle
unique_rolle = unique(rolle)
for i in unique_rolle:
    for j in rolle:
        if i[0] == j:
            i[1] +=1

#fakultät
unique_fak = unique(fakultät)
for i in unique_fak:
    for j in fakultät:
        if i[0] == j:
            i[1] +=1
            
#lehrstuhl
unique_lehr = unique(lehrstuhl)
for i in unique_lehr:
    for j in lehrstuhl:
        if i[0] == j:
            i[1] +=1
            
#computer            
unique_comp = unique(computer)
for i in unique_comp:
    for j in computer:
        if i[0] == j:
            i[1] +=1
            
#cam           
unique_cam = unique(cam)
for i in unique_cam:
    for j in cam:
        if i[0] == j:
            i[1] +=1
            
#mic            
unique_mic = unique(mic)
for i in unique_mic:
    for j in mic:
        if i[0] == j:
            i[1] +=1
            
#other_hw            
unique_ohw = unique(other_hw)
for i in unique_ohw:
    for j in other_hw:
        if i[0] == j:
            i[1] +=1
            
#exp            
unique_exp = unique(erfahrung)
for i in unique_exp:
    for j in erfahrung:
        if i[0] == j:
            i[1] +=1
    
exp_plot = do_boxplot(erfahrung, "", "Erfahrung")
exp_plot.show()
            
#training            
unique_training = unique(training)
for i in unique_training:
    for j in training:
        if i[0] == j:
            i[1] +=1
            
#new_hw            
unique_new_hw = unique(new_hw)
for i in unique_new_hw:
    for j in new_hw:
        if i[0] == j:
            i[1] +=1
            
#bezahlt            
unique_bezahlt = unique(bezahlt)
for i in unique_bezahlt:
    for j in bezahlt:
        if i[0] == j:
            i[1] +=1    
            
#other_sw            
unique_other_sw = unique(other_sw)
for i in unique_other_sw:
    for j in other_sw:
        if i[0] == j:
            i[1] +=1
            
#home_office            
unique_home_office = unique(home_office)
for i in unique_home_office:
    for j in home_office:
        if i[0] == j:
            i[1] +=1
            
#home_internet        
unique_home_internet = unique(home_internet)
for i in unique_home_internet:
    for j in home_internet:
        if i[0] == j:
            i[1] +=1
            
#pre_corona            
unique_pre_corona = unique(pre_corona)
for i in unique_pre_corona:
    for j in pre_corona:
        if i[0] == j:
            i[1] +=1
            
#wie_online            
unique_wie_online = unique(wie_online)
for i in unique_wie_online:
    for j in wie_online:
        if i[0] == j:
            i[1] +=1
            
#elemente            
unique_elemente = unique(elemente)
for i in unique_elemente:
    for j in elemente:
        if i[0] == j:
            i[1] +=1
            
#bereitstellen             
unique_bereitstellen = unique(bereitstellen)
for i in unique_bereitstellen:
    for j in bereitstellen:
        if i[0] == j:
            i[1] +=1
            
#hintergrund             
unique_hintergrund = unique(hintergrund)
for i in unique_hintergrund:
    for j in hintergrund:
        if i[0] == j:
            i[1] +=1
            
#perspektive             
unique_perspektive = unique(perspektive)
for i in unique_perspektive:
    for j in perspektive:
        if i[0] == j:
            i[1] +=1
            
#anmerkung             
unique_anmerkung = unique(anmerkung)
for i in unique_anmerkung:
    for j in anmerkung:
        if i[0] == j:
            i[1] +=1
            
#email             
unique_email = unique(email)
for i in unique_email:
    for j in email:
        if i[0] == j:
            i[1] +=1
            
#korrelation alter & erfahrung?
#alter verzahlen
num_alter = []
for i in alter:
    if i == "<20Jahre":
        num_alter.append(20)
    elif i == "20-29 Jahre":
        num_alter.append(25)
    elif i == "30-39 Jahre":
        num_alter.append(35)
    elif i == "40-49 Jahre":
        num_alter.append(45)
    elif i == "50-59 Jahre":
        num_alter.append(55)
    elif i == "60-69 Jahre":
        num_alter.append(65)
    elif i == ">70 Jahre":
        num_alter.append(70)
        
x1 = [1,2,3,4] #nan
x2 = [99,99,99,99] #nan
correlation, p_value = stats.pearsonr(num_alter, erfahrung) #nan nan
print(correlation, p_value)
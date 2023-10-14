#coded by dinesh and rajkumar
from fileinput import filename
from tkinter import N
import discord #bring discord library
from io import StringIO
import requests #The requests library is the de facto standard for making HTTP requests in Python
import json  # brings java script library
import os
from keep_alive import keep_alive

client = discord.Client()
TOKEN='OTU3MzEzODMyMTE0NTg1NjEw.Yj89-w.VgbdK0AlsPzfHryeXNG5IXgcqWY'

eect = "COMPLETE THE CLASS WORK"
due_date = "20/2/22"

psct = "PRACTICE PROB"
due_date2 = "25/8/22"

maths = "SOLVE PROBLEMS"
due_date3 = "28/2/22"

data_stru = "PREPARE FOR EXAM"
due_date4 = "25/8/22"

PSCT_LINK = "https://classroom.google.com/c/NDM0Nzg5NzY0OTY0"
EECT_LINK = "https://classroom.google.com/c/NDM2ODM2OTQxODEy"
LANG_LINK = "https://classroom.google.com/c/NDY0NTM2NDQ1NzIz"
ENG_LINK = "https://classroom.google.com/c/NDM0OTYxMzk5NTAx"
WORKSHOP_LINK = "https://classroom.google.com/c/NDM0Nzc0ODgxMjc0"
CALCUS_AND_MATRIX_ALGEBRA_LINK ="https://classroom.google.com/u/0/c/NDMwMDY0Njg4MDYz"
ADDITION_ENG_LINK = "https://classroom.google.com/u/0/c/NDY0NjA2NDg0OTc4"

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))# display's if you are online with your bot name

@client.event
async def on_disconnect():
    print("Good bye!!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!!")

    if message.content.startswith("$help"):#help list out all the options available to communicate with the bot
        await message.channel.send("$classroom - Get the links of the google classsroom")
        await message.channel.send("$STAFFCONT - Contacts of the Teachers")
        await message.channel.send("$Time table - Get the Time Table")
        await message.channel.send("$course outcome - Get the course outcomes")
        await message.channel.send("$curriculum - Get the curriculum of B-Tech cybersecurity")
        await message.channel.send("$what will i experience - States what you will be capable of after this course")
        await message.channel.send("$hello     - Greetings from the BOT")



    if message.content.startswith("$classroom"):#lists down all the classroom links
        await message.channel.send("PSCT : " + PSCT_LINK)
        await message.channel.send("EECT : " + EECT_LINK)
        await message.channel.send("LANGUAGE : " + LANG_LINK)
        await message.channel.send("COMMUNICAIVE ENGLISH : " + ENG_LINK)
        await message.channel.send("WORKSHOP : " + WORKSHOP_LINK)
        await message.channel.send("CALCUS_AND_MATRIX_ALGEBRA_LINK" + CALCUS_AND_MATRIX_ALGEBRA_LINK)
        await message.channel.send("ADDITION_ENG_LINK" + ADDITION_ENG_LINK)

    if message.content.startswith("$assingments"):

        My_embed = discord.Embed(title="ASSINGMENTS",descrption="assingments")
        # My_embed.add_field(name = " : Do the given sums \n PSCT : Pactice the program \n LAN1: Learn the questtions\n", value = "v2.3.2.0",inline=False)
        My_embed.add_field(name = "EECT:" + (eect), value = "DUE DATE " + due_date , inline=False )
        My_embed.add_field(name = "PSCT:" + (psct), value = "DUE DATE " + due_date2 , inline=False)
        My_embed.add_field(name = "MATHS:" + (maths), value = "DUE DATE " + due_date3 , inline=False)
        My_embed.add_field(name = "DATA STR:" + (data_stru), value = "DUE DATE " + due_date4 , inline=False)

        # My_embed.add_field(name="Date released:",value="july",inline=False)
        My_embed.set_footer(text = " No more assingments ")

        await message.channel.send(embed=My_embed)
        #$STAFFCONT lists the staff name, designation and mobile number
    if message.content.startswith("$STAFFCONT"):
        My_embed = discord.Embed(title="CONTACT",descrption="contact of the teachers",color = 0x00ff00)
        My_embed.add_field(name = "NAME", value = "Dr.V.Vivek" , inline=False )
        My_embed.add_field(name = "CONTACT",value = "1234567890",inline=False )
        My_embed.add_field(name = "DESIGNATION",value = "HOD OF CSE IN CS & AIML",inline=False )
        
        await message.channel.send(embed=My_embed)
        
    if message.content.startswith("$STAFFCONT"):
        My_embed = discord.Embed(title="CONTACT",descrption="contact of the teachers",color = 0x00ff00)
        My_embed.add_field(name = "NAME", value = "Jatinder Pal Singh" , inline=False )
        My_embed.add_field(name = "CONTACT",value = "1234567890",inline=False )
        My_embed.add_field(name = "DESIGNATION",value = "STUDENT CO-ODINATOR ",inline=False )

        await message.channel.send(embed=My_embed)
    
    if message.content.startswith("$STAFFCONT"):
        My_embed = discord.Embed(title="CONTACT",descrption="contact of the teachers",color = 0x00ff00)
        My_embed.add_field(name = "NAME", value = "Dr.Vaisak Mohan" , inline=False )
        My_embed.add_field(name = "CONTACT",value = "1234567890",inline=False )
        My_embed.add_field(name = "DESIGNATION",value = "CHEMISTRY LECTURER",inline=False )
        
        await message.channel.send(embed=My_embed)

    if message.content.startswith("$STAFFCONT"):
        My_embed = discord.Embed(title="CONTACT",descrption="contact of the teachers",color = 0x00ff00)
        My_embed.add_field(name = "NAME", value = "Dr.Midunlal P.V" , inline=False )
        My_embed.add_field(name = "CONTACT",value = "1234567890",inline=False )
        My_embed.add_field(name = "DESIGNATION",value = "PHYSICS LECTURER",inline=False )
        
        await message.channel.send(embed=My_embed)

    if message.content.startswith("$How are you?"):
        await message.channel.send("I'm a bot i don't have any moods or feelings....")

    if message.content.startswith("$Time table"):
        await message.channel.send(file=discord.File('time_table.png'))#to add file or file object we use discord.Files

    if message.content.startswith("$textbooks"):
        await message.channel.send(file=discord.File(fp=StringIO("maths text book"),
        filename="BSG.pdf"))
    
    if message.content.startswith("$course outcome"):#gives what you will be learing during the course
        await message.channel.send("•Network Security Engineer")
        await message.channel.send("•Cybersecurity Analyst")
        await message.channel.send("•Cybersecurity Architect")
        await message.channel.send("•Cybersecurity Specialist")
        await message.channel.send("•Cybersecurity Manager / Officer")
        await message.channel.send("•Chief Information Security Officer (CISO)")
        await message.channel.send("•Cyber Defence Analyst")
        await message.channel.send("•Digital Forensics Investigator")
        await message.channel.send("•Digital Forensics Specialist")
        await message.channel.send("•Digital Forensics Analyst")

    if message.content.startswith("$curriculum"):#gives 4-years of course curriculum
        await message.channel.send("*Semester I")
        await message.channel.send("•Engineering Mathematics -I\t•Applied Chemistry\n•Communicative English\t•Problem Solving Through Programming\n•Workshop Practice\t•Basics of Electrical Engineering")
        await message.channel.send("*Semester II")
        await message.channel.send("•Engineering Graphics\t•Data structure with C\n•ESP\t•Applied Physics")
        await message.channel.send("*Semester III")
        await message.channel.send("•Data Structures\t•Fundamentals of Business Management\n•Introduction to Cybersecurity\t•Programming in Java\n•Computer Architecture and Organization\t•Data Communication & Computer Networks")
        await message.channel.send("*Semester IV")
        await message.channel.send("•Operating System\t•Discrete Math and Graph Theory\n•Database Management System\t•Network Defense for Cybersecurity\n•Python Programming")
        await message.channel.send("*Semester V")
        await message.channel.send("•Software Engineering and Agile Methodologies\t•Web Programming Fundamentals\n•Ethical Hacking\t•Cybersecurity Incident Handling\n•Design and Analysis of Algorithm\t•Elective - I")
        await message.channel.send("*Semester VI")
        await message.channel.send("•Application Security for Java\t•Penetration Testing for Cybersecurity\n•Natural Language Processing\t•Elective - II\n•Elective - III\t•Open Elective - I\n•Project - I")
        await message.channel.send("*Semester VII")
        await message.channel.send("•Elective - IV\t•Elective - V\n•Cyber-Threat Intelligence\t•Open Elective - II\n•Project - II")
        await message.channel.send("*Semester VIII")
        await message.channel.send("•Elective - VI\t•Open Elective - III\n•Project - III / Internship")

    if message.content.startswith("$what will i experience"):#gives you, what you will you be capable of after the 4-years of course
        await message.channel.send("Learn how to configure and protect computer networks and systems. Understand the structure and strategies for managing information security risk. How to establish network security solutions and identify intrusions, as well as the capacity to perform a court-admissible digital forensics investigation. Be able to use cybersecurity abilities in a variety of real-world circumstances.Work on real-world projects, on-the-job training, and internships where you'll learn how to use efficient cyber-risk management to help organisations reach smarter, quicker, and more connected futures, allowing them to develop.")


      
keep_alive()
client.run(TOKEN) #coded by dinesh and rajkumar
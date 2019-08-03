This project is a simple DIY to run a pomodoro timer and post a message to slack 

There are few things that i had to do to make this working 

Some of the code blocks are already pre-complied and copied to the microprocessor, this was done to save 
memory on the processor. 


components used 

1. ESP8266 
2. OLED 
3. Micropython


I had to use mpy_cross to complile 

1. I had to compile the writer.py to writer.mpy (this helps to display text on OLED)
2. Font courier had to be pre-compiled as well. 

More on this in the blog article. 



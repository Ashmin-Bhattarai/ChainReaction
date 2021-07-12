import tkinter as tk
import pygame
 
pygame.init()
 
pwbr_power = 0
pwbr_duration = 0
pwbr_scrn_refresh = 0
pwbr_elps_time = 0
pwbr_ttl_sec = 0
 
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createwidgets()
    # __init__() ---------------------------------------------------------------
 
    def createwidgets(self):
        """
        Creates the numerous widgets that make up the form.
        """
         
        global pwbr_power, pwbr_duration, pwbr_scrn_refresh, pwbr_elps_time
        global pwbr_ttl_sec
         
        pwbr_power += 1
        pwbr_duration += 0.15
        pwbr_elps_time += pwbr_duration
        pwbr_scrn_refresh = 0.333
        pwbr_ttl_sec += pwbr_elps_time
 
        if pwbr_elps_time > pwbr_scrn_refresh:
            pwbr_elps_time = 0
            pwbr_duration = 0
 
        caption_pwr = "Power: " + str(pwbr_power)
        caption_dur = "Duration: " + str(pwbr_duration)
        caption_rfrsh =  "Screen Refresh: " + str(pwbr_scrn_refresh)
        caption_etime = "Elapsed time: " + str(pwbr_elps_time)
        caption_ttl = "Total sec's: " + str(pwbr_ttl_sec)
         
        self.lblpower = tk.Label(self, text=caption_pwr, fg="black")
        self.lblduration = tk.Label(self, text=caption_dur, fg="black")
        self.lblrefreshrate = tk.Label(self, text=caption_rfrsh, fg="black")
        self.lbletime = tk.Label(self, text=caption_etime, fg="black")
        self.lbltotalsec = tk.Label(self, text=caption_ttl, fg="black")
         
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
         
        self.lblpower.grid()
        self.lblduration.grid()
        self.lblrefreshrate.grid()
        self.lbletime.grid()
        self.lbltotalsec.grid()
        self.quitButton.grid()
        self.update()
         
        self.after(1000, self.update_info)
    # createwidgets() ----------------------------------------------------------
     
 
    def update_info(self):
        """
        Updates the status information in the tkinter window.
        """
         
        global pwbr_power, pwbr_duration, pwbr_scrn_refresh, pwbr_elps_time
        global pwbr_ttl_sec
         
        pwbr_power += 1
        pwbr_duration += 0.15
        pwbr_elps_time += pwbr_duration
        pwbr_scrn_refresh = 0.333
        pwbr_ttl_sec += pwbr_elps_time
 
        if pwbr_elps_time > pwbr_scrn_refresh:
            pwbr_elps_time = 0
            pwbr_duration = 0
 
        caption_pwr = "Power: " + str(pwbr_power)
        caption_dur = "Duration: " + str(pwbr_duration)
        caption_rfrsh =  "Screen Refresh: " + str(pwbr_scrn_refresh)
        caption_etime = "Elapsed time: " + str(pwbr_elps_time)
        caption_ttl = "Total sec's: " + str(pwbr_ttl_sec)
 
        self.lblpower.config(text=caption_pwr)
        self.lblduration.config(text=caption_dur)
        self.lblrefreshrate.config(text=caption_rfrsh)
        self.lbletime.config(text=caption_etime)
        self.lbltotalsec.config(text=caption_ttl)
 
        self.after(1000, self.update_info)
    # update_info() ----------------------------------------------------------
# Application() ----------------------------------------------------------------
 
 
pygame.display.set_mode((640, 480))
 
app = Application()
app.master.title("Power Bar")
app.mainloop()
 
 
 
quit_loop = False
while quit_loop is not True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            quit_loop = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.constants.KEYDOWN:
            if event.key == pygame.constants.K_ESCAPE:
                quit_loop = True
                break
            elif event.key == pygame.constants.K_LEFT:
                kbd["left"] = True
            elif event.key == pygame.constants.K_RIGHT:
                kbd["right"] = True
            elif event.key == pygame.constants.K_UP:
                kbd["up"] = True
            elif event.key == pygame.constants.K_DOWN:
                kbd["down"] = True
            elif event.key == pygame.constants.K_SPACE:  # Fire.
                kbd["fire"] = True
            elif event.key == pygame.constants.K_LCTRL:  # Thrust.
                kbd["thrust"] = True
            elif event.key == pygame.constants.K_r:
                kbd["overload"] = True
        elif event.type == pygame.constants.KEYUP:
            if event.key == pygame.constants.K_LEFT:
                kbd["left"] = False
            elif event.key == pygame.constants.K_RIGHT:
                kbd["right"] = False
            elif event.key == pygame.constants.K_UP:
                kbd["up"] = False
            elif event.key == pygame.constants.K_DOWN:
                kbd["down"] = False
            elif event.key == pygame.constants.K_SPACE:  # Fire.
                kbd["fire"] = False
            elif event.key == pygame.constants.K_LCTRL:  # Thrust.
                kbd["thrust"] = False
            elif event.key == pygame.constants.K_r:
                kbd["overload"] = False
            # end if
        # end if
    # end for loop
 
    # { Paint some graphics on the screen.
    #   ...
    # }.
    pygame.display.flip()
# end while loop
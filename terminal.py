#!/usr/bin/env python
from gi.repository import Gtk, Vte, Gdk, GLib
import os, sys
class QuickTerm(Gtk.Window):
#Destroy function a.k.a. closing the window function
    def destroy (self, widget):
        Gtk.main_quit()
#Toolbar functions
    def blue_initial(self,widget):
        self.command="sh /usr/share/initial.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
        
    def blue_connect(self,widget):
        self.command="power on"
        self.command2="\n"			
#Power        
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
        self.length = len(self.command2)
        self.vte.feed_child(self.command2, self.length)
#Agent		        
        self.command="agent on"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
        self.length = len(self.command2)
        self.vte.feed_child(self.command2, self.length)

        self.command="default-agent"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
        self.length = len(self.command2)
        self.vte.feed_child(self.command2, self.length)
#Scan
        self.command="scan on"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
        self.length = len(self.command2)
        self.vte.feed_child(self.command2, self.length)
        
    def copy(self, widget):
        self.vte.copy_clipboard()
        self.vte.grab_focus()
        
    def paste(self, widget):
        self.vte.paste_clipboard()
        self.vte.grab_focus()
        
    def clear_terminal(self,widget):
        self.command="clear"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
                
    def clear_history(self,widget):
        self.command="history -c"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
		
    def memory(self,widget):
        self.command="sh /usr/share/memory.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
            
    def sound(self,widget):
        self.command="sh /usr/share/sound.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
               
    def mount(self,widget):
        self.command="sh /usr/share/mount.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
                
    def wlan(self,widget):
        self.command="sudo sh /usr/share/wlanset.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
            
    def net(self,widget):
        self.command="sudo sh /usr/share/netset.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
                
    def miimo(self,widget):
        self.command="sh /usr/share/starter.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
                                
    def apt(self,widget):
        self.command="sudo sh /usr/share/apt.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
        
    def updates(self,widget):
        self.command="sudo sh /usr/share/updates.sh"
        self.length = len(self.command)
        self.vte.feed_child(self.command, self.length)
                                
###################################################################################
#About dialog function
    def about1 (self, widget):
        about1 = Gtk.AboutDialog()
        about1.set_program_name("Quick Terminal-GTK3 ")
        about1.set_version("V.0.5.2-PostX")
        about1.set_copyright(" Copyright (c) 2017 JJ Posti <techtimejourney.net>")
        about1.set_comments("Quick terminal is a terminal emulator written with Python. The program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.")
        about1.set_website("www.techtimejourney.net")
        about1.run()
        about1.destroy()
#################################################Right click 
    def right_click(self, widget, event):
        if event.button == 3:
            self.menu.show_all()            
            self.menu.popup(None, None, None, None, 0, Gtk.get_current_event_time())
############Make the window	
    def __init__(self):    
    # Create THE WINDOW
        self.window1=Gtk.Window()
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.set_title("Quick Terminal-GTK3")
        self.window1.connect("button_press_event", self.right_click)
#Menu
        self.menu=Gtk.Menu()
#Menu buttons
        #Copy&Paste
        self.copy_it = Gtk.MenuItem("Copy")
        self.copy_it.connect("activate", self.copy)

        self.paste_it = Gtk.MenuItem("Paste")
        self.paste_it.connect("activate", self.paste)
        
        self.menu.append(self.copy_it)
        self.menu.append(self.paste_it)
        
        #Clear history & Clear Terminal
        self.clear_his = Gtk.MenuItem("Clear history")
        self.clear_his.connect("activate", self.clear_history)

        self.clear_ter = Gtk.MenuItem("Clear terminal")
        self.clear_ter.connect("activate", self.clear_terminal)
        
        self.menu.append(self.clear_his)
        self.menu.append(self.clear_ter)

#Memory status
        self.memorys = Gtk.MenuItem("Memory status")
        self.memorys.connect("activate", self.memory)
        
        self.menu.append(self.memorys)
        
        #About Quick Terminal
        self.about_ter = Gtk.MenuItem("About Quick Terminal")
        self.about_ter.connect("activate", self.about1)
        self.menu.append(self.about_ter)                          
#Toolbars
        self.toolbar2=Gtk.Toolbar()
        
#Toolbar2 buttons
        
        self.SOUND_button=Gtk.ToolButton(Gtk.STOCK_EXECUTE)
        self.SOUND_button.set_label("Alsa Sound Selector")
        self.SOUND_button.connect("clicked", self.sound)
        self.SOUND_button.set_tooltip_text ("Alsa Sound Selector")       
        self.toolbar2.insert(self.SOUND_button, -1)
        
        self.WLAN_button=Gtk.ToolButton(Gtk.STOCK_PROPERTIES)
        self.WLAN_button.set_label("Wlan setup")
        self.WLAN_button.connect("clicked", self.wlan)
        self.WLAN_button.set_tooltip_text ("Wlan Setup")       
        self.toolbar2.insert(self.WLAN_button, -1) 
        
        self.NET_button=Gtk.ToolButton(Gtk.STOCK_CONNECT)
        self.NET_button.set_label("Network setup")
        self.NET_button.connect("clicked", self.net)
        self.NET_button.set_tooltip_text ("Network Setup")       
        self.toolbar2.insert(self.NET_button, -1)
               
        self.MOUNT_button=Gtk.ToolButton(Gtk.STOCK_HARDDISK)
        self.MOUNT_button.set_label("Simple Mount")
        self.MOUNT_button.connect("clicked", self.mount)
        self.MOUNT_button.set_tooltip_text ("Simple Mount")       
        self.toolbar2.insert(self.MOUNT_button, -1)
                                 
        self.APT_button=Gtk.ToolButton(Gtk.STOCK_GO_DOWN)
        self.APT_button.set_label("Apt Fetcher")
        self.APT_button.connect("clicked", self.apt)
        self.APT_button.set_tooltip_text ("Apt Fetcher")       
        self.toolbar2.insert(self.APT_button, -1)    

        self.UPDATES_button=Gtk.ToolButton(Gtk.STOCK_REFRESH)
        self.UPDATES_button.set_label("Updates")
        self.UPDATES_button.connect("clicked", self.updates)
        self.UPDATES_button.set_tooltip_text ("Fetch Updates")       
        self.toolbar2.insert(self.UPDATES_button, -1) 

        self.INI_button=Gtk.ToolButton(Gtk.STOCK_APPLY)
        self.INI_button.set_label("Bluetooth Initialization")
        self.INI_button.connect("clicked", self.blue_initial)
        self.INI_button.set_tooltip_text ("Bluetooth Initialization")       
        self.toolbar2.insert(self.INI_button, -1)  
        
        self.BLUE_button=Gtk.ToolButton(Gtk.STOCK_PREFERENCES)
        self.BLUE_button.set_label("Bluetooth Setup")
        self.BLUE_button.connect("clicked", self.blue_connect)
        self.BLUE_button.set_tooltip_text ("Bluetooth Setup")       
        self.toolbar2.insert(self.BLUE_button, -1)  

        self.MIIMO_button=Gtk.ToolButton(Gtk.STOCK_OPEN)
        self.MIIMO_button.set_label("Miimo Tool")
        self.MIIMO_button.connect("clicked", self.miimo)
        self.MIIMO_button.set_tooltip_text ("Miimo Decompress/Compress")       
        self.toolbar2.insert(self.MIIMO_button, -1)
#Terminal
        self.vte = Vte.Terminal()
        self.vte.connect ("child-exited", lambda term: Gtk.main_quit())

#Fork
        self.vte.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            ["/bin/bash"],
            [],
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            )
#Make a clipboard for copy and paste
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

#Scrolled window
        self.scroll=Gtk.ScrolledWindow()
        self.scroll.set_min_content_height(350)
        self.scroll.set_min_content_width(640)
        self.scroll.add(self.vte)

#Vertical box/buttons container
        self.vbox=Gtk.VBox(False)
        self.vbox.pack_start(self.scroll, True, True, True)
        self.vbox.pack_start(self.toolbar2, False, False, False)

#Show everything		
        self.window1.add(self.vbox)
        self.window1.show_all()
         
#Making window resizable and enabling the close window connector        
        self.window1.set_resizable(True)
        self.window1.connect("destroy", Gtk.main_quit)

def main():
    Gtk.main()
    return 0

if __name__ == "__main__":
    QuickTerm()
    main()

#!/usr/bin/env python  
# -*- coding: utf-8 -*-    
import sys   
import commands   
import os   
import os.path   
import pygtk   
import gtk    
import Test 
__author__="riho"   
__date__ ="$2016/01/18 23:42:04$"    
  
class TwitterUI:  
    def __init__(self):  
        #Set the Glade file  
        self.gladefile = "twitter.ui"  
        self.wTree = gtk.Builder()  

	self.wTree.add_from_file(os.path.dirname(os.path.abspath(__file__)) + "/"+self.gladefile)  
	#Create our dictionay and connect it  
	dic = {  

                "btCancel_clicked_cb" : self.on_btnCancel_clicked,  
                "btOK_clicked_cb" : self.on_btnOK_clicked,  
                "on_TopLevel_destroy" : self.on_TopLevel_destroy,
		"on_entry1_activate":self.on_entry_activate}    
	self.wTree.connect_signals(dic) 

        self.mainWindow = self.wTree.get_object ("TopLevel")  
        self.mainWindow.show_all()  
    def on_TopLevel_destroy(self, widget):  
        #ウィンドウを閉じてアプリケーションを終了する  
        gtk.main_quit()  
    def on_btnOK_clicked(self,entry1):  
        #ウィンドウを閉じてアプリケーションを終了する  
	#self.on_entry_activate
	entry = self.wTree.get_object("entry1")
	Test.disp(entry.get_text())
	#print("%s" % text1)
    def on_btnCancel_clicked(self,widget):  
        #ウィンドウを閉じてアプリケーションを終了する  
        gtk.main_quit()  
    def on_entry_activate(self,entry1):
       Test.disp(entry1.get_text())
       #print("%s" % text1)
if __name__ == "__main__":  
    TwitterUI()  
    gtk.main()  

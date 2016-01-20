# -*- coding: utf-8 -*-
import sqlite3
import sys   
import commands   
import os   
import os.path   
import pygtk   
import gtk
__author__="riho"   
__date__ ="$2016/01/20 23:42:04$"  
class TwitterDB:  
    def __init__(self):  
        #Set the Glade file  
        self.gladefile = "twitterdb.ui"  
        self.wTree = gtk.Builder()  

	self.wTree.add_from_file(os.path.dirname(os.path.abspath(__file__)) + "/"+self.gladefile)  
        self.n=1
        self.connector = sqlite3.connect("users.db")
    	self.cursor    = self.connector.cursor()
    	self.cursor.execute("SELECT * from followers")



    	self.result = self.cursor.fetchall()

 	for self.row in self.result:

        #print "===== Hit! ====="

        	print  str(self.n)  + "人目"

        	print "code -- " + unicode(self.row[0])

        	print "name -- " + unicode(self.row[1])

        	print "name -- " + unicode(self.row[3])

        	print "name -- " + unicode(self.row[4])

        	print "name -- " + unicode(self.row[5])

		self.n=self.n+1
    	self.cursor.close()

    	self.connector.close()
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
	text1=entry.get_text()
	print("%s" % text1)
    def on_btnCancel_clicked(self,widget):  
        #ウィンドウを閉じてアプリケーションを終了する  
        gtk.main_quit()  
    def on_entry_activate(self,entry1):
       text1=entry1.get_text()
       print("%s" % text1)


if __name__ == "__main__":
    TwitterDB()  
    gtk.main()  



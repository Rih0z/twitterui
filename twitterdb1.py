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
	self.tree = self.wTree.get_object("treeview1")

        self.tree.append_column( gtk.TreeViewColumn('No.', gtk.CellRendererText(), text=0) )
        self.tree.append_column( gtk.TreeViewColumn('HN', gtk.CellRendererText(), text=1) )
        self.tree.append_column( gtk.TreeViewColumn('ID', gtk.CellRendererText(), text=2) )
        self.tree.append_column( gtk.TreeViewColumn('偽率(％)', gtk.CellRendererText(), text=3) )
        self.tree.append_column( gtk.TreeViewColumn('profile', gtk.CellRendererText(), text=4) )
        self.tree.append_column( gtk.TreeViewColumn('followers_count(人)', gtk.CellRendererText(), text=5) )

        self.tree.set_model(gtk.ListStore(int, str, str,str,str,str))
	self.label1 = self.wTree.get_object("result_1")
	self.label2 = self.wTree.get_object("result_2")
	self.label3 = self.wTree.get_object("result_3")
	self.label4 = self.wTree.get_object("result_4")
	self.label5 = self.wTree.get_object("result_5")
	self.label6 = self.wTree.get_object("result_6")
	self.label7 = self.wTree.get_object("result_7")
	self.label8 = self.wTree.get_object("result_8")
	self.label9 = self.wTree.get_object("result_9")
	self.label10 = self.wTree.get_object("result_10")
	self.label11 = self.wTree.get_object("result_11")
	self.label12 = self.wTree.get_object("result_12")
	self.label13 = self.wTree.get_object("result_13")
	self.label14 = self.wTree.get_object("result_14")
	self.label15 = self.wTree.get_object("result_15")
	self.label16 = self.wTree.get_object("result_16")
	self.label17 = self.wTree.get_object("result_17")
	self.label18 = self.wTree.get_object("result_18")
	self.label19 = self.wTree.get_object("result_19")
	self.label20 = self.wTree.get_object("result_20")
	self.label21 = self.wTree.get_object("result_21")
	self.label22 = self.wTree.get_object("result_22")
	self.label23 = self.wTree.get_object("result_23")
	self.label24 = self.wTree.get_object("result_24")
	self.label25 = self.wTree.get_object("result_25")
	self.label26 = self.wTree.get_object("result_26")
	self.label27 = self.wTree.get_object("result_27")
	self.label28 = self.wTree.get_object("result_28")
	self.label29 = self.wTree.get_object("result_29")
	self.label30 = self.wTree.get_object("result_30")

	#Create our dictionay and connect it  
	dic = {  

                "btCancel_clicked_cb" : self.on_btnCancel_clicked,  
                "btOK_clicked_cb" : self.on_btnOK_clicked,  
                "on_TopLevel_destroy" : self.on_TopLevel_destroy}    
	self.wTree.connect_signals(dic) 

        self.mainWindow = self.wTree.get_object ("TopLevel")  
        self.mainWindow.show_all()  
    def on_TopLevel_destroy(self, widget):  
        #ウィンドウを閉じてアプリケーションを終了する  
        gtk.main_quit()  
    def on_btnOK_clicked(self,entry1):  
        #ウィンドウを閉じてアプリケーションを終了する  
	#self.on_entry_activate
        #self.tree.get_model().append((1, '居石峻寛',"haruka_system",82,"ANCT5。プロコンの…プロコン。",3))
	self.n=1
	self.count=1
        self.connector = sqlite3.connect("users.db")
    	self.cursor    = self.connector.cursor()
    	self.cursor.execute("SELECT * from followers ORDER BY false_percent DESC")



    	self.result = self.cursor.fetchall()

 	for self.row in self.result:

        #print "===== Hit! ====="       self.tree.set_model(gtk.ListStore(int, str, str,str,str,str))
		

		
        	#eval("r"+str(self.count)) = str(self.n)  + "人目"
		eval("self."+"label"+str(self.count)).set_text(str(self.n)  + "人目")
		self.count=self.count+1

        	#eval("result"+str(self.count)) = "name -- " + unicode(self.row[0])
		eval("self."+"label"+str(self.count)).set_text( "HN -- " + unicode(self.row[0]))
		self.count=self.count+1

        	#eval(result+str(self.count)) = "code -- " + unicode(self.row[1])
		eval("self."+"label"+str(self.count)).set_text("ID -- " + unicode(self.row[1]))
		self.count=self.count+1

        	#eval(result+str(self.count)) = "code -- " + unicode(self.row[3])
		eval("self."+"label"+str(self.count)).set_text("偽率 -- " + unicode(self.row[3]))
		self.count=self.count+1

        	#eval(result+str(self.count)) = "code -- " + unicode(self.row[4])
		eval("self."+"label"+str(self.count)).set_text("profile -- " + unicode(self.row[4]))
		self.count=self.count+1

        	#eval(result+str(self.count)) = "code -- " + unicode(self.row[5])
		eval("self."+"label"+str(self.count)).set_text("followers_count -- " + unicode(self.row[5]))
		self.count=self.count+1

		self.tree.get_model().append((self.n,unicode(self.row[0]),unicode(self.row[1]),unicode(self.row[3]),unicode(self.row[4]),unicode(self.row[5])))
		
		self.n=self.n+1
		


    	self.cursor.close()

    	self.connector.close()



    def on_btnCancel_clicked(self,widget):  
        #ウィンドウを閉じてアプリケーションを終了する  
        gtk.main_quit()  


if __name__ == "__main__":

    TwitterDB()  
    gtk.main()  



# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from ctypes.wintypes import SIZE
from operator import truediv
from pickle import TRUE
import wx
import wx.xrc
import string

###########################################################################
## Class MyFrame1
###########################################################################

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame1(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		frame1= wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"bmi calculator", pos = wx.DefaultPosition, size=(500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		#frame1.SetSize(600,600)
		#wx.Frame.__init__(self,parent,title=u"bmi calculator",size=(2000,2000))
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"身高", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 18, 73, 90, 90, False, "標楷體" ) )
		
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, size=(300,-1) )
		self.m_textCtrl3.SetFont( wx.Font( 12, 72, 90, 90, False, "新細明體" ) )
		
		bSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"體重", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 18, 73, 90, 90, False, "標楷體" ) )
		
		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, size=(300,-1) )
		self.m_textCtrl4.SetFont( wx.Font( 12, 72, 90, 90, False, "新細明體" ) )
		
		bSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"bmi 計算結果：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 12, 73, 90, 90, False, "標楷體" ) )
		# self.m_staticText4.Hide()
		
		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"送出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 14, 72, 90, 90, False, "新細明體" ) )
		
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Fit()
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		"""self.m_textCtrl3.Bind( wx.EVT_TEXT_ENTER, self.get_height )
		self.m_textCtrl4.Bind( wx.EVT_TEXT_ENTER, self.get_weight )"""
		self.m_button1.Bind( wx.EVT_BUTTON, self.result )
	
	def __del__( self ):
		pass
	
	
	def result( self, event):
		tmp1=float(self.m_textCtrl4.Value)     #weight
		tmp2=float(self.m_textCtrl3.Value)/100 #height
		print(tmp1)
		print(tmp2)
		tmp2= tmp2**2
		bmi= tmp1 / tmp2
		self.m_staticText4.SetLabel(u"bmi 計算結果："+str(bmi))
		self.m_staticText4.Wrap(-1)
		self.m_staticText4.Show()
		print(bmi)
		event.Skip()
	
if __name__=="__main__":
    app=MyApp(True)
    app.MainLoop()
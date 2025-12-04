AJ='Xem file_path đã dự đoán'
AI='video/'
AH='file_path'
AG='yolov8n-seg.pt'
AF='Instance Segmentation'
AE='Object Detection'
AD='Current value:'
AC='You selected: '
AB='and Object Detection Analysis based on YOLOv8'
AA='Vehicle Trajectory Recognition'
A0='Export successful!'
z='success'
y='Save Chart Image'
x='c'
w='video_output/'
v='mp4v'
u='Videos (*.mp4 *.avi)'
t='Open Video File'
s='yolov8n.pt'
r=zip
q=len
p='User canceled save image operation'
o=None
n='{}:{}'
m='Images (*.png *.jpg *.bmp)'
l='image/2.png'
k=round
j=hasattr
d='Category'
c='Track ID'
b='y'
a='x'
W='./video_output/'
S='Y'
R='X'
Q=str
P=range
N='{:.2f}'
L=False
H=''
G=float
E=True
C=Exception
B=int
A=print
import os as T,sys
from collections import defaultdict as A1
import numpy as O,pandas as X,csv
from ultralytics import YOLO as U
from ultralytics.engine import predictor as A2
import cv2 as D
from PyQt5.QtMultimedia import QMediaPlayer as e,QMediaContent as f
from PyQt5.QtWidgets import QApplication as AK,QWidget,QFileDialog as K,QGraphicsScene as Y,QTabBar,QDialog as A3,QHBoxLayout as A4,QLabel as I,QVBoxLayout as A5,QPushButton as A6,QTableWidgetItem as AL,QMessageBox as J,QGraphicsLineItem,QLineEdit
from PyQt5.QtGui import QImage,QPixmap as V,QFont as g,QIcon as A7,QPalette as M,QColor as h
from PyQt5.QtCore import Qt as F,QUrl as i,QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as A8
from matplotlib.figure import Figure as A9
from pyecharts.charts import HeatMap,Bar3D
from pyecharts import options as Z
class AM(QWidget):
	def __init__(A):super().__init__();A.init_ui()
	def init_ui(A):C=1.;B=.0;A.ui=uic.loadUi('./ui/main_new.ui');A.actiondefault=A.ui.actiondefault;A.actionblack=A.ui.actionblack;A.actionwhite=A.ui.actionwhite;A.actionblue=A.ui.actionblue;A.actionintro=A.ui.actionintro;A.actionversion=A.ui.actionversion;A.actionexit=A.ui.actionexit;A.tabWidget=A.ui.tabWidget;A.tab_image=A.ui.tab_image;A.tab_video=A.ui.tab_video;A.tab_track=A.ui.tab_track;A.tab_count=A.ui.tab_count;A.test2_btn=A.ui.test2_btn;A.test3_btn=A.ui.test3_btn;A.raw_img=A.ui.raw_image;A.res_img=A.ui.res_image;A.select_btn=A.ui.select_btn;A.show_btn=A.ui.show_btn;A.model1=A.ui.combo1;A.conf1=A.ui.conf1;A.conf1.setRange(B,C);A.conf1.setSingleStep(.01);A.conf1.setValue(.25);A.IOU1=A.ui.IOU1;A.IOU1.setRange(B,C);A.IOU1.setSingleStep(.01);A.IOU1.setValue(.45);A.class1=A.ui.class1;A.video1=A.ui.video1;A.choose_video=A.ui.choose_video;A.play_pause1=A.ui.play_pause1;A.media_player1=e();A.media_player1.setVideoOutput(A.video1);A.media_player1.durationChanged.connect(A.getDuration1);A.media_player1.positionChanged.connect(A.getPosition1);A.ui.slider1.sliderMoved.connect(A.updatePosition1);A.video2=A.ui.video2;A.show_video=A.ui.show_video;A.play_pause2=A.ui.play_pause2;A.media_player2=e();A.media_player2.setVideoOutput(A.video2);A.media_player2.durationChanged.connect(A.getDuration2);A.media_player2.positionChanged.connect(A.getPosition2);A.ui.slider2.sliderMoved.connect(A.updatePosition2);A.model2=A.ui.combo2;A.conf2=A.ui.conf2;A.conf2.setRange(B,C);A.conf2.setSingleStep(.01);A.conf2.setValue(.25);A.IOU2=A.ui.IOU2;A.IOU2.setRange(B,C);A.IOU2.setSingleStep(.01);A.IOU2.setValue(.45);A.class2=A.ui.class2;A.video3=A.ui.video3;A.play_pause3=A.ui.play_pause3;A.slider3=A.ui.slider3;A.time3=A.ui.time3;A.choose_btn=A.ui.choose_btn;A.track_path=A.ui.track_path;A.track_btn=A.ui.track_btn;A.export3=A.ui.export3;A.media_player3=e();A.media_player3.setVideoOutput(A.video3);A.media_player3.durationChanged.connect(A.getDuration3);A.media_player3.positionChanged.connect(A.getPosition3);A.ui.slider3.sliderMoved.connect(A.updatePosition3);A.conf3=A.ui.conf3;A.conf3.setRange(B,C);A.conf3.setSingleStep(.01);A.conf3.setValue(.25);A.IOU3=A.ui.IOU3;A.IOU3.setRange(B,C);A.IOU3.setSingleStep(.01);A.IOU3.setValue(.45);A.class3=A.ui.class3;A.video4=A.ui.video4;A.play_pause4=A.ui.play_pause4;A.slider4=A.ui.slider4;A.time4=A.ui.time4;A.choose_btn4=A.ui.choose_btn4;A.count_path=A.ui.count_path;A.count_btn=A.ui.count_btn;A.media_player4=e();A.media_player4.setVideoOutput(A.video4);A.media_player4.durationChanged.connect(A.getDuration4);A.media_player4.positionChanged.connect(A.getPosition4);A.ui.slider4.sliderMoved.connect(A.updatePosition4);A.conf4=A.ui.conf4;A.conf4.setRange(B,C);A.conf4.setSingleStep(.01);A.conf4.setValue(.25);A.IOU4=A.ui.IOU4;A.IOU4.setRange(B,C);A.IOU4.setSingleStep(.01);A.IOU4.setValue(.45);A.class4=A.ui.class4;A.select_xlsx=A.ui.select_xlsx;A.xlsx=A.ui.xlsx;A.show_row=A.ui.show_row;A.show_col=A.ui.show_col;A.input_id=A.ui.input_id;A.draw5=A.ui.draw5;A.show_image5=A.ui.show_image5;A.chart5=A.ui.chart5;A.export5=A.ui.export5;A.hotmap=A.ui.hotmap;A.chart6_2=A.ui.chart6_2;A.data6_1=A.ui.data6_1;A.data6_2=A.ui.data6_2;A.data6_3=A.ui.data6_3;A.export6_1=A.ui.export6_1;A.export6_2=A.ui.export6_2;A.tab_image.clicked.connect(A.open1);A.tab_video.clicked.connect(A.open2);A.tab_track.clicked.connect(A.open3);A.tab_count.clicked.connect(A.open4);A.test2_btn.clicked.connect(A.open5);A.test3_btn.clicked.connect(A.open6);A.model1.currentIndexChanged.connect(A.combo1_change);A.select_btn.clicked.connect(A.select_image);A.show_btn.clicked.connect(A.detect_objects);A.model2.currentIndexChanged.connect(A.combo2_change);A.choose_video.clicked.connect(A.chooseVideo1);A.play_pause1.clicked.connect(A.playPause1);A.play_pause2.clicked.connect(A.playPause2);A.show_video.clicked.connect(A.showVideo);A.choose_btn.clicked.connect(A.chooseVideo3);A.play_pause3.clicked.connect(A.playPause3);A.track_btn.clicked.connect(A.showTrack);A.export3.clicked.connect(A.export_location);A.choose_btn4.clicked.connect(A.chooseVideo4);A.play_pause4.clicked.connect(A.playPause4);A.count_btn.clicked.connect(A.showCount);A.select_xlsx.clicked.connect(A.selectDataset);A.draw5.clicked.connect(A.drawChart5);A.export5.clicked.connect(A.export_chart5);A.tabBar=A.tabWidget.findChild(QTabBar);A.tabBar.hide();A.tabWidget.setCurrentIndex(0);A.actionwhite.triggered.connect(A.menu_white);A.actionblack.triggered.connect(A.menu_black);A.actionblue.triggered.connect(A.menu_blue);A.actiondefault.triggered.connect(A.menu_default);A.actionintro.triggered.connect(A.menu_intro);A.actionversion.triggered.connect(A.menu_version);A.actionexit.triggered.connect(A.myexit);A.export6_1.clicked.connect(A.export_chart6_1);A.export6_2.clicked.connect(A.export_chart6_2)
	def menu_default(B):A('default');E=f"QMainWindow{{background-color: rgb(240,240,240)}}";C=f"QWidget{{background-color: rgb(240,240,240)}}";F=f"QLabel{{color: rgb(20, 120, 80); font: 26pt'Arial'; font-weight: bold;}}";G=f"QLabel{{background-color: rgb(230, 230, 230)}}";D=f"QLabel{{color: rgb(100, 100, 100); font-size: 16pt; font-weight: bold;}}";B.ui.setStyleSheet(E);B.ui.centralwidget.setStyleSheet(C);B.ui.tab.setStyleSheet(C);B.ui.tab_2.setStyleSheet(C);B.ui.tab_3.setStyleSheet(C);B.ui.tab_4.setStyleSheet(C);B.ui.tab_5.setStyleSheet(C);B.ui.tab_6.setStyleSheet(C);B.ui.label_11.setStyleSheet(F);B.ui.label_38.setStyleSheet(G);B.ui.time1.setStyleSheet(D);B.ui.time2.setStyleSheet(D);B.ui.time3.setStyleSheet(D);B.ui.time4.setStyleSheet(D)
	def menu_white(B):A('light');E=f"QMainWindow{{background-color: rgb(250,250,250)}}";C=f"QWidget{{background-color: rgb(250,250,250)}}";F=f"QLabel{{color: rgb(20, 120, 80); font: 26pt'Arial'; font-weight: bold;}}";G=f"QLabel{{background-color: rgb(240, 240, 240)}}";D=f"QLabel{{color: rgb(100, 100, 100); font-size: 16pt; font-weight: bold;}}";B.ui.setStyleSheet(E);B.ui.centralwidget.setStyleSheet(C);B.ui.tab.setStyleSheet(C);B.ui.tab_2.setStyleSheet(C);B.ui.tab_3.setStyleSheet(C);B.ui.tab_4.setStyleSheet(C);B.ui.tab_5.setStyleSheet(C);B.ui.tab_6.setStyleSheet(C);B.ui.label_11.setStyleSheet(F);B.ui.label_38.setStyleSheet(G);B.ui.time1.setStyleSheet(D);B.ui.time2.setStyleSheet(D);B.ui.time3.setStyleSheet(D);B.ui.time4.setStyleSheet(D)
	def menu_black(B):A('dark');E=f"QMainWindow{{background-color: rgb(50,50,50)}}";C=f"QWidget{{background-color: rgb(50,50,50)}}";F=f"QLabel{{color: rgb(40, 240, 160); font: 26pt'Arial'; font-weight: bold;}}";G=f"QLabel{{background-color: rgb(40, 60, 50)}}";D=f"QLabel{{color: rgb(250, 250, 250); font-size: 16pt; font-weight: bold;}}";B.ui.setStyleSheet(E);B.ui.centralwidget.setStyleSheet(C);B.ui.tab.setStyleSheet(C);B.ui.tab_2.setStyleSheet(C);B.ui.tab_3.setStyleSheet(C);B.ui.tab_4.setStyleSheet(C);B.ui.tab_5.setStyleSheet(C);B.ui.tab_6.setStyleSheet(C);B.ui.label_11.setStyleSheet(F);B.ui.label_38.setStyleSheet(G);B.ui.time1.setStyleSheet(D);B.ui.time2.setStyleSheet(D);B.ui.time3.setStyleSheet(D);B.ui.time4.setStyleSheet(D)
	def menu_blue(B):A('blue');E=f"QMainWindow{{background-color: rgb(230,245,255)}}";C=f"QWidget{{background-color: rgb(230,245,255)}}";F=f"QLabel{{color: rgb(20, 120, 80); font: 26pt'Arial'; font-weight: bold;}}";G=f"QLabel{{background-color: rgb(210, 240, 255)}}";D=f"QLabel{{color: rgb(100, 100, 100); font-size: 16pt; font-weight: bold;}}";B.ui.setStyleSheet(E);B.ui.centralwidget.setStyleSheet(C);B.ui.tab.setStyleSheet(C);B.ui.tab_2.setStyleSheet(C);B.ui.tab_3.setStyleSheet(C);B.ui.tab_4.setStyleSheet(C);B.ui.tab_5.setStyleSheet(C);B.ui.tab_6.setStyleSheet(C);B.ui.label_11.setStyleSheet(F);B.ui.label_38.setStyleSheet(G);B.ui.time1.setStyleSheet(D);B.ui.time2.setStyleSheet(D);B.ui.time3.setStyleSheet(D);B.ui.time4.setStyleSheet(D)
	def menu_intro(Y):
		A('intro')
		try:D=A3();D.setWindowTitle('introduction');D.setFixedSize(1200,800);W=A4(D);R=I();S=V(l);S=S.scaled(400,350);R.setPixmap(S);R.setAlignment(F.AlignCenter);W.addWidget(R);J=g();J.setPointSize(18);J.setBold(E);G=g();G.setPointSize(10);G.setBold(E);T=M();H=M();T.setColor(M.WindowText,h(10,80,50));H.setColor(M.WindowText,h(30,180,80));B=A5();K=I(AA);K.setAlignment(F.AlignCenter);K.setFont(J);K.setPalette(T);L=I(AB);L.setAlignment(F.AlignCenter);L.setFont(J);L.setPalette(T);N=I('This software is dedicated to traffic object tracking and detection,');N.setAlignment(F.AlignCenter);N.setPalette(H);N.setFont(G);O=I('performing trajectory recognition and plotting tasks using YOLOv8,');O.setAlignment(F.AlignCenter);O.setPalette(H);O.setFont(G);P=I('and organizing collected data into traffic datasets,');P.setAlignment(F.AlignCenter);P.setPalette(H);P.setFont(G);Q=I('facilitating subsequent data processing, analysis, and visualization.');Q.setAlignment(F.AlignCenter);Q.setPalette(H);Q.setFont(G);B.addSpacing(100);B.addWidget(K);B.addWidget(L);B.addSpacing(50);B.addWidget(N);B.addWidget(O);B.addWidget(P);B.addWidget(Q);B.addSpacing(100);U=A6('Close',D);U.setFixedSize(150,60);U.clicked.connect(D.close);B.addWidget(U,alignment=F.AlignCenter);W.addLayout(B);D.setWindowIcon(A7(l));D.exec()
		except C as X:A(X)
	def menu_version(X):
		U='version';A(U)
		try:D=A3();D.setWindowTitle(U);D.setFixedSize(1200,800);T=A4(D);O=I();P=V(l);P=P.scaled(400,350);O.setPixmap(P);O.setAlignment(F.AlignCenter);T.addWidget(O);G=g();G.setPointSize(18);G.setBold(E);H=g();H.setPointSize(14);H.setBold(E);Q=M();R=M();Q.setColor(M.WindowText,h(10,80,50));R.setColor(M.WindowText,h(30,180,80));B=A5();J=I(AA);J.setAlignment(F.AlignCenter);J.setFont(G);J.setPalette(Q);K=I(AB);K.setAlignment(F.AlignCenter);K.setFont(G);K.setPalette(Q);L=I('Version: V 1.0');L.setAlignment(F.AlignCenter);L.setFont(H);L.setPalette(R);N=I('Date: 19-01-2025');N.setAlignment(F.AlignCenter);N.setFont(H);N.setPalette(R);B.addSpacing(100);B.addWidget(J);B.addWidget(K);B.addSpacing(50);B.addWidget(L);B.addWidget(N);B.addSpacing(100);S=A6('Close',D);S.setFixedSize(150,60);S.clicked.connect(D.close);B.addWidget(S,alignment=F.AlignCenter);T.addLayout(B);D.setWindowIcon(A7(l));D.exec()
		except C as W:A(W)
	def open1(A):A.tabWidget.setCurrentIndex(0)
	def open2(A):A.tabWidget.setCurrentIndex(1)
	def open3(A):A.tabWidget.setCurrentIndex(2)
	def open4(A):A.tabWidget.setCurrentIndex(3)
	def open5(A):A.tabWidget.setCurrentIndex(4)
	def open6(B):
		f='category_nums';e='1200';d='600';F='0';B.tabWidget.setCurrentIndex(5);A('Draw Heatmap')
		try:
			G=X.DataFrame(columns=[a,b]);G[a]=B.df[R];G[b]=B.df[S];N=[0,300,600,900,1200,1500,1800,2100];T=[0,200,400,600,800,1000,1200,1400];U=O.zeros((7,7))
			for(k,I)in B.df.iterrows():
				for D in P(7):
					if N[D]<=I[R]and I[R]<=N[D+1]:
						for K in P(7):
							if T[K]<=I[S]and I[S]<=T[K+1]:U[D][K]+=1
			g=[F,'300',d,'900',e,'1500','1800'];h=[F,'200','400',d,'800','1000',e];G=[(A,B,U[A][B])for A in P(7)for B in P(7)];i=HeatMap(init_opts=Z.InitOpts(width='650px',height='500px')).add_xaxis(g).add_yaxis(H,h,G).set_global_opts(title_opts=Z.TitleOpts(title='Heatmap',title_textstyle_opts=Z.TextStyleOpts(font_size=24,padding=20)),visualmap_opts=Z.VisualMapOpts(max_=150,range_color=['#abd9e9','#e0f3f8','#ffffbf','#fee090','#fdae61','#f46d43','#d73027','#a50026'])).set_series_opts(label_opts=Z.LabelOpts(font_size=24));B.hotmap_html=i.render_embed();B.hotmap.setHtml(B.hotmap_html)
		except C as L:A(L)
		A('Draw Bar Chart')
		try:
			B.figure6_2=A9(figsize=(4,2.5));B.myax6=B.figure6_2.add_subplot(111);B.canvas=A8(B.figure6_2);B.data6_1.setText(F);B.data6_2.setText(F);B.data6_3.setText(F)
			if j(B,f):A('category_nums exists')
			else:A('category_nums does not exist')
			if j(B,f):
				A(B.category_nums);M=[]
				for D in P(q(B.category_nums)):M.append(D)
				V=list(B.category_nums.values());W=0
				for(J,E)in B.category_nums.items():
					W+=E
					if J==0:A(J,E);B.data6_2.setText(Q(E))
					if J==2:A(J,E);B.data6_1.setText(Q(E))
					B.data6_3.setText(Q(W))
			else:M=['one','two','three','four'];V=[10,20,15,25]
			B.myax6.bar(M,V,color=['skyblue','lightgreen','lightcoral','lightblue']);B.myax6.set_xlabel('categories');B.myax6.set_ylabel('nums');B.myax6.set_title('categoryies’ nums');B.canvas.draw();c=Y(B);c.addWidget(B.canvas);B.chart6_2.setScene(c)
		except C as L:A(L)
	def combo1_change(B,index):A(AC+B.model1.currentText());A(index)
	def select_image(A):
		C=K();B,D=C.getOpenFileName(A,'Open Image File',H,m)
		if B:A.image_path=B;A.load_image()
	def load_image(B):
		try:D=Y();H=V(B.image_path);E=B.raw_img.size();I=E.width();J=E.height();G=H.scaled(I,J,F.KeepAspectRatio);D.addPixmap(G);B.raw_img.setScene(D);B.raw_img.setSceneRect(G.rect())
		except C as K:A(f"Error occurred while loading and scaling image: {K}")
	def show_image(A):B=Y();E=V(A.image_path);C=A.res_img.size();G=C.width();H=C.height();D=E.scaled(G,H,F.KeepAspectRatio);B.addPixmap(D);A.res_img.setScene(B);A.res_img.setSceneRect(D.rect())
	def detect_objects(D):
		if not D.image_path:return
		F=D.conf1.value();F=G(N.format(F));A(AD,F);A(type(F));A(D.image_path);I=D.IOU1.value();I=G(N.format(I))
		if D.class1.text()==H:J=-1
		else:J=B(D.class1.text())
		if D.model1.currentText()==AE:K=U(s)
		elif D.model1.currentText()==AF:K=U(AG)
		if J==-1:K.predict(D.image_path,save=E,imgsz=320,conf=F,iou=I)
		else:K.predict(D.image_path,save=E,imgsz=320,conf=F,iou=I,classes=J)
		A(A2.update_global_var());L=T.path.basename(D.image_path);A(L)
		try:M=Q(A2.update_global_var())+'\\'+L;A(M);D.image_path=M;D.show_image()
		except C as O:A(O)
	def combo2_change(B,index):A(AC+B.model2.currentText());A(index)
	def chooseVideo1(B):
		try:
			E=K();D,G=E.getOpenFileName(B,t,H,u)
			if D:B.video_path=D;A('Absolute / Relative path? file_path: '+D);B.media_player1.setMedia(f(i(D)));B.media_player1.play()
		except C as F:A(F)
	def playPause1(A):
		if A.media_player1.state()==1:A.media_player1.pause()
		else:A.media_player1.play()
	def getDuration1(A,d):A.ui.slider1.setRange(0,d);A.ui.slider1.setEnabled(E);A.displayTime1(d)
	def getPosition1(A,p):A.ui.slider1.setValue(p);A.displayTime1(A.ui.slider1.maximum()-p)
	def displayTime1(C,ms):A=B(ms/60000);D=B((ms-A*60000)/1000);C.ui.time1.setText(n.format(A,D))
	def updatePosition1(A,v):A.media_player1.setPosition(v);A.displayTime1(A.ui.slider1.maximum()-v)
	def showVideo(E):
		if not E.video_path:A('Please select a video first!');return
		F=E.conf2.value();F=G(N.format(F));A(AD,F);A(type(F));I=E.IOU2.value();I=G(N.format(I));A(I)
		if E.class2.text()==H:K=-1
		else:K=B(E.class2.text())
		if E.model2.currentText()==AE:L=U(s)
		elif E.model2.currentText()==AF:L=U(AG)
		J=D.VideoCapture(E.video_path);R=B(J.get(3));S=B(J.get(4));M=T.path.basename(E.video_path);V=D.VideoWriter_fourcc(*v);O=D.VideoWriter(w+M,V,2e1,(R,S))
		while J.isOpened():
			X,P=J.read()
			if X:
				if K==-1:Q=L.predict(P,conf=F,iou=I)
				else:Q=L.predict(P,conf=F,iou=I,classes=K)
				Y=Q[0].plot();O.write(Y)
			else:break
		J.release();O.release()
		try:E.media_player2.setMedia(f(i(W+M)));E.media_player2.play();A('Check predicted file_path'+W+M)
		except C as Z:A(Z)
	def playPause2(A):
		if A.media_player2.state()==1:A.media_player2.pause()
		else:A.media_player2.play()
	def getDuration2(A,d):A.ui.slider2.setRange(0,d);A.ui.slider2.setEnabled(E);A.displayTime2(d)
	def getPosition2(A,p):A.ui.slider2.setValue(p);A.displayTime2(A.ui.slider2.maximum()-p)
	def displayTime2(C,ms):A=B(ms/60000);D=B((ms-A*60000)/1000);C.ui.time2.setText(n.format(A,D))
	def updatePosition2(A,v):A.media_player2.setPosition(v);A.displayTime2(A.ui.slider2.maximum()-v)
	def chooseVideo3(D):
		try:
			E=K();B,G=E.getOpenFileName(D,t,H,u)
			if B:A(AH,B);D.track_path.setText(B)
		except C as F:A(F)
	def playPause3(A):
		if A.media_player3.state()==1:A.media_player3.pause()
		else:A.media_player3.play()
	def getDuration3(A,d):A.ui.slider3.setRange(0,d);A.ui.slider3.setEnabled(E);A.displayTime3(d)
	def getPosition3(A,p):A.ui.slider3.setValue(p);A.displayTime3(A.ui.slider3.maximum()-p)
	def displayTime3(C,ms):A=B(ms/60000);D=B((ms-A*60000)/1000);C.ui.time3.setText(n.format(A,D))
	def updatePosition3(A,v):A.media_player3.setPosition(v);A.displayTime3(A.ui.slider3.maximum()-v)
	def showTrack(F):
		F.locations={}
		if not F.track_path:return
		K=F.conf3.value();K=G(N.format(K));A(K);Y=F.IOU3.value();Y=G(N.format(Y))
		if F.class3.text()==H:e=-1
		else:e=B(F.class3.text())
		try:
			n=U('yolov8m-obb.pt');Z=T.path.basename(F.track_path.toPlainText());p=AI+Z;A('Video path problem???',p);M=D.VideoCapture(p);A2=A1(lambda:[]);g=[];Q={};s=set();h=L;A('Entering loop!');A(M.isOpened())
			while M.isOpened():
				A3,P=M.read()
				if not A3:break
				c=P.copy()
				if e==-1:A('No class specified, conf: ',K);I=n.track(P,persist=E,conf=K,iou=Y,show=L);A('OBB tracking info');A(I[0].obb)
				else:A('Class specified');I=n.track(P,persist=E,conf=K,iou=Y,classes=e,show=L)
				t=I[0].obb.xywhr.cpu();u=I[0].obb.cls.cpu();k=I[0].obb.id.cpu()if j(I[0].obb,'id')else o;A('boxes:',t);A('classes:',u);A('results[0].boxes.id:',k)
				if k is o:A('Fill frames even without ID, do not skip frames, to prevent missing detection scenes causing incomplete video');g.append(P);continue
				A4=k.int().cpu().tolist()
				for(A5,J,R)in r(I[0].obb.xywhr.cpu(),I[0].obb.id.cpu(),I[0].obb.cls.cpu()):S,V,y,z,X=map(G,A5);A('OBB angle info:');A(X);X=O.degrees(X);A6=(S,V),(y,z),X;l=D.boxPoints(A6);l=O.int0(l);D.drawContours(c,[l],0,(100,255,0),3);D.putText(c,f"ID: {B(J)}",(B(S),B(V)-10),D.FONT_HERSHEY_SIMPLEX,.7,(255,255,255),2)
				for(A7,J,R)in r(t,A4,u):
					S,V,y,z,X=A7
					if J not in F.locations:F.locations[J]=[]
					F.locations[J].append({a:G(S),b:G(V),x:B(R)});h=E
					for A8 in s:
						if J==A8:h=L;break
					if h:
						if B(R)in Q:Q[B(R)]+=1
						else:Q[B(R)]=1
						A(Q)
					s.add(J);d=A2[J];d.append((G(S),G(V)))
					if q(d)>150:d.pop(0)
					A9=O.hstack(d).astype(O.int32).reshape((-1,1,2));D.polylines(c,[A9],isClosed=L,color=(250,170,0),thickness=8)
				g.append(c)
			AA=B(M.get(3));AB=B(M.get(4));AC=D.VideoWriter_fourcc(*v);A0=D.VideoWriter(w+Z,AC,2e1,(AA,AB))
			for P in g:A0.write(P)
			M.release();A0.release();F.category_nums=Q;A('What is category_nums??',F.category_nums)
			if j(F,'categoty_nums'):A('Exists')
		except C as m:A(m)
		try:F.media_player3.setMedia(f(i(W+Z)));F.media_player3.play();A(AJ+W+Z)
		except C as m:A(m)
	def export_location(D):
		C,U=K.getSaveFileName(D,'Save Chart Data',H,'Chart (*.xlsx *.csv)')
		if C:
			A(C);P=T.path.splitext(C)[0];A('Filename:',P);N=T.path.splitext(C)[1];A('File extension:',N)
			if N=='.xlsx':
				F=X.DataFrame(columns=[c,R,S,d])
				for(G,I)in D.locations.items():
					for B in I:J=k(B[a],3);M=k(B[b],3);F=F._append({c:G,R:J,S:M,d:B[x]},ignore_index=E)
				F.to_excel(C,index=L)
			else:
				with open(C,'w',newline=H)as Q:
					O=csv.writer(Q);O.writerow([c,R,S,d])
					for(G,I)in D.locations.items():
						for B in I:J=k(B[a],3);M=k(B[b],3);O.writerow([G,J,M,B[x]])
		else:A(p);return
	def chooseVideo4(D):
		try:
			E=K();B,G=E.getOpenFileName(D,t,H,u)
			if B:A(AH,B);D.count_path.setText(B)
		except C as F:A(F)
	def playPause4(A):
		if A.media_player4.state()==1:A.media_player4.pause()
		else:A.media_player4.play()
	def getDuration4(A,d):A.ui.slider4.setRange(0,d);A.ui.slider4.setEnabled(E);A.displayTime4(d)
	def getPosition4(A,p):A.ui.slider4.setValue(p);A.displayTime4(A.ui.slider4.maximum()-p)
	def displayTime4(C,ms):A=B(ms/60000);D=B((ms-A*60000)/1000);C.ui.time4.setText(n.format(A,D))
	def updatePosition4(A,v):A.media_player4.setPosition(v);A.displayTime4(A.ui.slider4.maximum()-v)
	def showCount(F):
		if not F.count_path:return
		P=F.conf4.value();P=G(N.format(P));Q=F.IOU4.value();Q=G(N.format(Q))
		if F.class4.text()==H:Y=-1
		else:Y=B(F.class4.text())
		try:
			b=U(s);R=T.path.basename(F.count_path.toPlainText());h=AI+R;J=D.VideoCapture(h);j=A1(lambda:[]);c=[];S=600;V=0;d=set()
			while J.isOpened():
				k,I=J.read()
				if k:
					if Y==-1:K=b.track(I,persist=E,conf=P,iou=Q,show=L)
					else:K=b.track(I,persist=E,conf=P,iou=Q,classes=Y,show=L)
					l=K[0].boxes.xywh.cpu()
					if K[0].boxes.id is not o:
						m=K[0].boxes.id.int().cpu().tolist();M=K[0].plot()
						for(n,Z)in r(l,m):
							p,e,z,A0=n;X=j[Z];X.append((G(p),G(e)))
							if q(X)>100:X.pop(0)
							t=O.hstack(X).astype(O.int32).reshape((-1,1,2));D.polylines(M,[t],isClosed=L,color=(250,170,0),thickness=8)
							if e<S and Z not in d:A(I.shape[0]-S);V+=1;d.add(Z)
							A(V);D.line(M,(0,S),(I.shape[1],S),(0,255,0),2);D.putText(M,f"Crossed line count: {V}",(50,100),D.FONT_HERSHEY_SIMPLEX,2,(255,200,0),3,D.LINE_AA)
						A(M);c.append(M)
				else:break
			u=B(J.get(3));x=B(J.get(4));y=D.VideoWriter_fourcc(*v);g=D.VideoWriter(w+R,y,2e1,(u,x))
			for I in c:g.write(I)
			A('Crossed line count:',V);J.release();g.release()
		except C as a:A(a)
		try:F.media_player4.setMedia(f(i(W+R)));F.media_player4.play();A(AJ+W+R)
		except C as a:A(a)
	def selectDataset(B):
		H='Read successfully!';D,L=K.getOpenFileName(o,'Select file to read','.','Excel Files (*.xlsx *.xls);;CSV Files (*.csv)')
		if D:
			if D.endswith('.xlsx'):
				A('Reading Excel file, please wait...')
				try:I=X.ExcelFile(D);B.df=X.read_excel(I)
				except C as E:A(E)
				A(H)
			elif D.endswith('.csv'):A('Reading CSV file, please wait...');B.df=X.read_csv(D);A(H)
			try:
				B.xlsx.setRowCount(B.df.shape[0]);B.xlsx.setColumnCount(B.df.shape[1]);B.show_row.setText(Q(B.df.shape[0]));B.show_col.setText(Q(B.df.shape[1]));B.xlsx.setHorizontalHeaderLabels(B.df.columns.tolist())
				for F in P(B.df.shape[0]):
					for G in P(B.df.shape[1]):J=AL(Q(B.df.iloc[F,G]));B.xlsx.setItem(F,G,J)
			except C as E:A('Please enter a valid dataset!',E)
		else:A('User canceled dataset selection operation');return
	def drawChart5(D):
		if D.input_id.text()==H:A('Please enter the object ID to plot trajectory');I=J();I.setWindowTitle('warning');I.setIcon(J.Warning);I.setText('Please enter the object ID to plot trajectory first');I.exec_();return
		try:K=B(D.input_id.text())
		except ValueError:J.warning(D,'error','Please enter a valid integer',J.Ok);return
		A(D.df);A(K)
		try:A(D.df[c]==K);F=D.df[D.df[c]==K];F=F.reset_index(drop=E)
		except C as L:A(L)
		A('Drawing...')
		try:D.figure5=A9(figsize=(4,3));D.myax=D.figure5.add_subplot(111);D.canvas=A8(D.figure5);N=F[R];O=F[S];A(N);D.myax.set_title('location x and y');D.myax.scatter(N,O,c='green');D.canvas.draw();G=Y(D);G.addWidget(D.canvas);D.chart5.setScene(G);G=Y();A(F[d]);M=V(f"image/{F[d][0]}.png");M=M.scaled(200,200);G.addPixmap(M);D.show_image5.setScene(G)
		except C as L:A(L)
	def export_chart5(D):
		E,G=K.getSaveFileName(D,y,H,m)
		if E:
			D.figure5.savefig(E)
			try:B=J();B.setWindowTitle(z);B.setIcon(J.Information);B.setText(A0);B.exec_()
			except C as F:A(F)
		else:A(p);return
	def export_chart6_1(D):
		E=V();E=D.hotmap.grab();F,I=K.getSaveFileName(D,y,H,m)
		if F:
			E.save(F)
			try:B=J();B.setWindowTitle(z);B.setIcon(J.Information);B.setText(A0);B.exec_()
			except C as G:A(G)
		else:A(p);return
	def export_chart6_2(D):
		E,G=K.getSaveFileName(D,y,H,m)
		if E:
			D.figure6_2.savefig(E)
			try:B=J();B.setWindowTitle(z);B.setIcon(J.Information);B.setText(A0);B.exec_()
			except C as F:A(F)
		else:A(p);return
	def myexit(A):exit()
if __name__=='__main__':AN=AK(sys.argv);AO=AM();AO.ui.show();AN.exec()
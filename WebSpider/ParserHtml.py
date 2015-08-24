__author__ = 'clark'
#coding=utf-8
from sgmllib import SGMLParser
import re
import urllib

class GetFCBM(SGMLParser):
    def reset(self):
        #heand title
        self.title = ""
        self.head_flag = False
        self.getTitleData = False

        #material
        self.FCBM = []
        self.material_flag = False
        self.material_getData = False
        self.material_verbatim = 0

        #step
        self.step = []
        self.step_flag = False
        self.step_getData = False
        self.step_verbatim = 0
        self.img = None

        SGMLParser.reset(self)

    #get head title
    def start_head(self, attrs):
        self.head_flag = True

    def end_head(self):
        self.head_flag = False

    def start_title(self, attrs):
        if self.head_flag:
            self.getTitleData = True

    def end_title(self):
        if self.getTitleData:
            self.getTitleData = False

    #material
    def start_div(self, attrs):
        if self.material_flag:
            print(self.step_flag,attrs)
            if self.step_flag:
                self.step_verbatim += 1
                self.material_verbatim += 1
                return
            for next_k, next_v in attrs:
                if next_k == 'class' and next_v == 'stepcont mll libdm pvl clearfix':
                    self.step_flag = True
                    # return
            self.material_verbatim += 1
            return



        for k,v in attrs:
            if k == 'class' and v == 'retew r3 pb25 mb20':
                self.material_flag = True
                # self.material_verbatim += 1
                return



    def end_div(self):
        if self.material_verbatim == 0:
            self.material_flag = False

        if self.material_flag == True:
            self.material_verbatim -= 1

        if self.step_verbatim == 0:
            self.step_flag = False

        if self.step_flag == True:
            self.step_verbatim -= 1

    def start_td(self, attrs):
        if self.material_flag == False:
            return
        self.material_getData = True

    def end_td(self):
        if self.material_getData:
            self.material_getData = False



    #step
    def start_p(self, attrs):
        if self.step_flag:
            self.step_getData = True

    def end_p(self):
        if self.step_getData:
            self.step_getData = False

    def start_img(self, attrs):
        if self.step_flag:
            for k,v in attrs:
                if k == 'original':
                    self.img = urllib.urlopen(v).read()

    def end_img(self):
        if self.step_getData:
            self.step_getData = False

    def handle_data(self, data):
        if self.material_getData:
            p = re.compile('\s+')
            value = re.sub(p, '', data)
            if len(value):
                self.FCBM.append(value)
        elif self.getTitleData:
            self.title = data
        elif self.step_getData:
            p = re.compile('\s+')
            temp = re.sub(p, '', data)

            if len(temp):
                p = re.compile('^\d+')
                value = p.match(temp)
                if value:
                    self.one_index = value.group()
                else:
                    if not self.one_index:
                        return
                    one = (self.one_index, temp, None)#self.img)
                    self.img = None
                    self.one_index = None
                    self.step.append(one)



    def getHead(self):
        return self.title
    def getMaterial(self):
        return self.FCBM
    def getStep(self):
        return self.step
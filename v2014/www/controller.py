# -*- coding: utf-8 -*-
from tori.controller           import Controller
from tori.decorator.controller import renderer

@renderer('www.view')
class Home(Controller):
    def get(self):
        self.render('index.html')

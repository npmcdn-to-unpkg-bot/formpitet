# -*- coding: utf-8 -*-
from pymongo import MongoClient
from random import choice

client = MongoClient('mongodb://localhost:27017/')
db = client.evotesttask

names_doc = db.names

# CREATE
def add_name(name):
    data = {'name': name, 'epitet':choice(EPITETS)}
    names_doc.insert(data)

#READ
def get_epitet(name):
    data = names_doc.find_one({'name':name})
    return data['epitet']

#GET epitets
EPITETS = ["Великолепный(ая)",
 "Чудесный(ая)",
  "Супер", 
  "Всемогущий(ая)", 
  "Неудержимый(ая)",
  "Ваша Светлость",
  "Пресвятейший(ая)",
  "Непревзойденный(ая)",
  "Великодушный(ая)",
  "Бессмертный(ая)",
  "Удививительный(ая)",
  "Великий Гений",
  "Волшебный(ая)"]



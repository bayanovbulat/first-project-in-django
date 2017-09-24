#-*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from firstapp.models import Graphs
import os
import matplotlib
matplotlib.use('Agg') #Попытка борьбы с backend-ом
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from firstapp.forms import UploadFileForm
from firstapp.models import FileModel

def save(name='', fmt='png'):
    pwd = os.getcwd()  # текущая рабочая дериктория
    iPath = 'firstapp/static'
    if not os.path.exists(
            iPath):  # возвращает True, если path указывает на существующий путь или дескриптор открытого файла
        os.mkdir(iPath)  # создаёт директорию. OSError, если директория существует
    os.chdir(iPath)  # смена текущей директории
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)  # смена текущей директории
    plt.close()

def make_graph(data):
    plt.figure()
    max = 0
    for i in range(8):
        if int(data[1][i+1]) > int(data[1][i]):
            max = int(data[1][i+1])
        else: max = int(data[1][i])
    scatter1 = plt.scatter(0.0, 0.0)
    graph1 = plt.plot([data[0][0], data[0][1]],[data[1][0], data[1][1]],
                      [data[0][1], data[0][2]],[data[1][1],data[1][2]],
                      [data[0][2], data[0][3]], [data[1][2], data[1][3]],
                      [data[0][3], data[0][4]], [data[1][3], data[1][4]],
                      [data[0][4], data[0][5]], [data[1][4], data[1][5]],
                      [data[0][5], data[0][6]], [data[1][5], data[1][6]],
                      [data[0][6], data[0][7]], [data[1][6], data[1][7]],
                      [data[0][7], data[0][8]], [data[1][7], data[1][8]],
                      [data[0][8], data[0][9]], [data[1][8], data[1][9]],
                      )
    text1 = plt.text(data[0][8], data[1][9], 'f(x)')
    osx = int(data[0][9]) + 1
    osy = int(max) + 5
    text2 = plt.text(osx, 0, 'x')
    text3 = plt.text(-1, 25, 'y = f(x)')
    grid1 = plt.grid(True)
    save(name='pic1', fmt='png')
    #plt.savefig('pic1.png')

@csrf_exempt
def hello(request):
    return render_to_response('hello.html')

@csrf_exempt
def thanks(request):
    return render_to_response('thanks.html')

@csrf_exempt
def upload_file(request):
    data_name = 'Добро пожаловать!'
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data_name = 'Файл загружен!'
            # так производится создание объектов модели FileModel и запись их в базу данных
            p1 = FileModel.objects.create(number = request.POST['number'], file = request.FILES['file'])
            data_way1 = 'firstapp/static/'
            data_way2 = str(request.FILES['file'])
            data_way = data_way1 + data_way2
            data = [[], []]
            excel_data_file = xlrd.open_workbook(data_way)
            sheet = excel_data_file.sheet_by_index(0)  # Обращение к нулевой странице
            batch_Names_wanted = []  # список имен
            row_number = sheet.nrows  # количество строк
            if row_number > 0:  # Проверка на пустоту файла
                for row in range(0, row_number):
                    data[0].append(str(sheet.row(row)[0]).replace("number:", "").replace(".0",
                                                                                         ""))  # replace убирает ненужные символы .replace("text:", ""))
                    data[1].append(str(sheet.row(row)[1]).replace("number:", "").replace(".0", ""))
            else:
                render_to_response('thanks.html')
            p1.delete()
            #data_way3 = data_way.replace("/","\\")
            #path = os.path.join(os.path.abspath(os.path.dirname(__file__)), data_way3)
            #os.remove(path)
            make_graph(data)
            return HttpResponseRedirect('/upload')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form, 'data_name': data_name})
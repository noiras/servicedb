from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404
from .models import MasterTable, ColumnTable, ValueTable
from django.db.models import Count 
from django.http import JsonResponse
import os, sys,shutil
from PIL import Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def dashboard(request):
    if request.method == 'POST':
        table_name = request.POST.get('tableName')

        list_column = request.POST.getlist('column')
        list_data = request.POST.getlist('typeData')
        dictionary = dict(zip(list_column, list_data))
        
        p1 = MasterTable(name=table_name)
        p1.save()

        for key, value in dictionary.items():
            p2 = ColumnTable(master_table=p1, name=key, data_type=int(value))
            p2.save()
    
    return render(request,'master/index.html')

def view_detail_dashboard(request, id):
    master_table = MasterTable.objects.get(pk=id)
    column_table = ColumnTable.objects.filter(master_table=id)
    context = {
        'master_table' : master_table,
        'column_table' : column_table,
    }
    return render(request, 'master/edit_column.html', context)    

def viewtable(request):
    data = MasterTable.objects.all()
    context = {
        'datatable' : data,
    }
    return render(request,'master/viewtable.html', context)

def delete_table(request, id):
    masterTable = MasterTable.objects.get(pk=id)
    
    masterTable.delete()
    file_path = r"%s\%s" % (settings.MEDIA_ROOT,masterTable.name)
    shutil.rmtree(file_path, ignore_errors=True)
    return redirect('/master/viewtable')

def devide_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]

def viewsdetailstable(request, id):
    views_master = MasterTable.objects.get(pk=id)
    column_table = ColumnTable.objects.filter(master_table=id)
    # ValueTable.objects.annotate(value=Count('id')).order_by('-id')
    
    context = {
        'column_list' : column_table,
        'views_master' : views_master,
    }

    if request.method == 'POST':
        tableColumn = request.POST.getlist('tableColumn')
        valuecolumn = request.POST.getlist('valueColumn')
        dictionary = dict(zip(tableColumn, valuecolumn))
        

        for column in column_table:
            if(column.data_type == 4):
                file_path = r"%s\%s" % (settings.MEDIA_ROOT,views_master.name)
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                    
                file_path = r"%s\%s\%s" % (settings.MEDIA_ROOT,views_master.name,column.name)
                if not os.path.exists(file_path):
                    os.makedirs(file_path)

                myfile = request.FILES['valueColumn-'+ str(column.pk)]
               
                lokasi = os.path.join(settings.MEDIA_ROOT, views_master.name, column.name, myfile.name)
                with open(lokasi, 'wb') as f:
                    f.write(myfile.read())
                
        
        for key, values in dictionary.items():
            itemColumn = ColumnTable.objects.get(id=key)
            value = ValueTable()
            value.value = values.lower()
            value.save()
            itemColumn.value.add(value)
            
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    values = []
    for column in column_table:     
        value_per_column = []
        for value in column.value.all():
            value_per_column.append({
                'id': value.id,
                'value': value.value
            })
        values.append(value_per_column)
    result = []
    for value in values:
        for index, i in enumerate(value):
            try:
                result[index].append(i)
            except IndexError:
                result.append([i])

    context.update({
        'value_list': result
    })
    
    return render(request, 'master/viewsdetails.html', context)    

def updatevalue(request):
    if request.method == 'POST':
        id = request.POST['id'].split(',')
        val = request.POST['val'].split(',')        
        column_table = request.POST['column_name']
        table_name = request.POST['table_name']

        for a in id:
            vals = ValueTable.objects.get(id=a)
            if(len(request.FILES) != 0):
                if(vals.value[-4:] == '.jpg'):
                    file_path = r"%s\%s" % (settings.MEDIA_ROOT, vals.value)
                    os.remove(file_path)
                    
                    myfile = request.FILES['image']       
                    lokasi = os.path.join(settings.MEDIA_ROOT, table_name, column_table, myfile.name)
                    with open(lokasi, 'wb') as f:
                        f.write(myfile.read())    
                        
                elif(vals.value[-4:] == '.png'):
                    file_path = r"%s\%s" % (settings.MEDIA_ROOT, vals.value)
                    os.remove(file_path)

                    myfile = request.FILES['image']       
                    lokasi = os.path.join(settings.MEDIA_ROOT, table_name, column_table, myfile.name)
                    with open(lokasi, 'wb') as f:
                        f.write(myfile.read())    
                        
                elif(vals.value[-4:] == '.gif'):
                    file_path = r"%s\%s" % (settings.MEDIA_ROOT, vals.value)
                    os.remove(file_path)
    
                    myfile = request.FILES['image']       
                    lokasi = os.path.join(settings.MEDIA_ROOT, table_name, column_table, myfile.name)
                    with open(lokasi, 'wb') as f:
                        f.write(myfile.read())
                elif(vals.value[-4:] == '.JPG'):
                    file_path = r"%s\%s" % (settings.MEDIA_ROOT, vals.value)
                    os.remove(file_path)

                    myfile = request.FILES['image']       
                    lokasi = os.path.join(settings.MEDIA_ROOT, table_name, column_table, myfile.name)
                    with open(lokasi, 'wb') as f:
                        f.write(myfile.read())    
                        
                elif(vals.value[-4:] == '.PNG'):
                    file_path = r"%s\%s" % (settings.MEDIA_ROOT, vals.value)
                    os.remove(file_path)
    
                    myfile = request.FILES['image']       
                    lokasi = os.path.join(settings.MEDIA_ROOT, table_name, column_table, myfile.name)
                    with open(lokasi, 'wb') as f:
                        f.write(myfile.read())
                elif(vals.value[-4:] == '.GIF'):
                    file_path = r"%s\%s" % (settings.MEDIA_ROOT, vals.value)
                    os.remove(file_path)
    
                    myfile = request.FILES['image']       
                    lokasi = os.path.join(settings.MEDIA_ROOT, table_name, column_table, myfile.name)
                    with open(lokasi, 'wb') as f:
                        f.write(myfile.read())

        for index, id_data in enumerate(id):
            obj = ValueTable.objects.get(id=id_data)
            obj.value = val[index]
            obj.save()
        status = 'success'
        return HttpResponse(status)
    else:
        status = 'bad' 
        return HttpResponse(status)

def deletevalue(request):
    if request.method =='POST':
        id = request.POST['id'].split(',')
        val = request.POST['val'].split(',')
        for id_data in id:
            a = ValueTable.objects.get(pk=str(id_data))
            a.delete()
        
        for val_data in val:
            s = val_data.strip()
            
            if(s[-4:] == '.jpg'):
                file_path = r"%s\%s" % (settings.MEDIA_ROOT, s)
                os.remove(file_path)
                
            elif(s[-4:] == '.png'):
                file_path = r"%s\%s" % (settings.MEDIA_ROOT, s)
                os.remove(file_path)
                
            elif(s[-4:] == '.gif'):
                file_path = r"%s\%s" % (settings.MEDIA_ROOT, s)
                os.remove(file_path)
                
            elif(s[-4:] == '.JPG'):
                file_path = r"%s\%s" % (settings.MEDIA_ROOT, s)
                os.remove(file_path)
                
            elif(s[-4:] == '.PNG'):
                file_path = r"%s\%s" % (settings.MEDIA_ROOT, s)
                os.remove(file_path)
                
            elif(s[-4:] == '.GIF'):
                file_path = r"%s\%s" % (settings.MEDIA_ROOT, s)
                os.remove(file_path)
                
            else:
                print('error')   
        status = 'success'
        return HttpResponse(status)
    else:
        status = 'fail'
        return HttpResponse(status)

def tablejson(request):
    datajson = MasterTable.objects.all()
    
    list_Table = []
    for data in datajson:
        
        a = data.id
        b = data.name
        responseData = {
            'table' : b,
            'id' : a
        }
        list_Table.append(responseData)
        
    return JsonResponse(list_Table, safe=False)

def valuejson(request, id):
    

    views_master = MasterTable.objects.get(pk=id)
    column_table = ColumnTable.objects.filter(master_table=id)
    
    values = []
    for column in column_table:     
        value_per_column = []
        for value in column.value.all():
            if column.data_type == ColumnTable.FILE:
                value_data = "{host}/media/{value}".format(host=request.get_host(), value=value.value)
            else:
                value_data = value.value

            value_per_column.append({
                'data_type': column.get_data_type_display().lower(),
                column.name : value_data
            })
        values.append(value_per_column)
    result = []
    for value in values:
        for index, i in enumerate(value):
            try:
                result[index].append(i)
            except IndexError:
                result.append([i])

    
    
    responseResult = {
        'table' : views_master.name,
        'values' : result,
    }
    return JsonResponse(responseResult)
    
def updatecolumn(request):
    if request.method == 'POST':
        pk = request.POST['id']
        inp_val = request.POST['val_input']
        data_type_val = request.POST['val_data_type']

        if data_type_val == '5':
            file_path = r"%s\%s" % (settings.MEDIA_ROOT, inp_val)
            os.remove(file_path)

        column = ColumnTable.objects.get(id=pk)
        column.name = inp_val
        column.data_type = data_type_val
        column.save()

    return redirect('/master/dashboard/')

def deletecolumn(request):
    if request.method == 'POST':
        pk = request.POST['id']
        column = ColumnTable.objects.get(id=pk)
        column.delete()
    return redirect('/master/dashboard/')

def viewsaddcolumn(request,id):
    table_master = MasterTable.objects.get(id = id)
    context = {
        'table_master' : table_master,
    }
    if request.method == 'POST':
        table_name = request.POST.get('tableName')

        list_column = request.POST.getli9ost('column')
        list_data = request.POST.getlist('typeData')
        dictionary = dict(zip(list_column, list_data))
        
        p1 = MasterTable(id=table_master.id)
        
        for key, value in dictionary.items():
            
            p2 = ColumnTable(manhster_table=p1, name=key, data_type=int(value))
            p2.save()
        return redirect('/master/viewtable/')
    return render(request, 'master/add_column.html', context)
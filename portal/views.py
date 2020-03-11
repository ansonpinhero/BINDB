from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from portal.models import MalwareFiles, BenignFiles
from django.views.decorators.csrf import csrf_exempt
from virustotal.vtcheck import check_hash_vt
import csv


@csrf_exempt
def check_benign(request):
    hash_file = request.GET['hash']
    file_name = request.GET['file_name']
    file_size = request.GET['file_size']
    
    if (BenignFiles.objects.filter(sha_256 = hash_file).exists()):
        message = "Duplicate"
    else:
        r = check_hash_vt(hash_file)

        if (r == "Benign"):           
            BenignFiles.objects.get_or_create(file_name = file_name,sha_256 = hash_file , file_size = file_size )
            message = "Benign"
        else:
            message = "Malware"
    return HttpResponse(message)

@csrf_exempt
def check_malware(request):
    hash_file = request.GET['hash']
    file_name = request.GET['file_name']
    file_size = request.GET['file_size']
    
    if (MalwareFiles.objects.filter(sha_256 = hash_file).exists()):
        message = "Duplicate"
    else:
        r = check_hash_vt(hash_file)

        if (r == "Malware"):           
            MalwareFiles.objects.get_or_create(file_name = file_name,sha_256 = hash_file , file_size = file_size )
            message = "Malware"
        else:
            message = "Benign"
    return HttpResponse(message)



def export_malware_files(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="malware_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['File Name','SHA 256', 'File Size', 'Timestamp'])

    files = MalwareFiles.objects.all().values_list('file_name','sha_256','file_size','timestamp')
    for file in files:
        writer.writerow(file)

    return response
    
def export_benign_files(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="benign_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['File Name','SHA 256', 'File Size', 'Timestamp'])

    files = BenignFiles.objects.all().values_list('file_name','sha_256','file_size','timestamp')
    for file in files:
        writer.writerow(file)

    return response


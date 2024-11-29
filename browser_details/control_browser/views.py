from django.shortcuts import render 
from django.http import HttpResponse
import subprocess 
import os
from django.http import JsonResponse
import psutil
import shutil

# Create your views here.



BROWSER_COMMAND = {
    'chrome': 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    'firefox': 'firefox'
}

def home(request):
    return HttpResponse("<h1> Hello there!! </h1>")

def start(request):
    browser = request.GET.get('browser')
    url = request.GET.get('url')
    
    if browser in BROWSER_COMMAND:
        cmd = r'start chrome /new-tab {}'.format(url)
        subprocess.Popen(cmd, shell= True) 
        return JsonResponse({'message' : f"{browser.capitalize()} starting with {url} "})
    return JsonResponse({'error': 'Unsupported browser'}, status = 400)
    

def stop(request):
    browser = request.GET.get('browser')
    if browser  in BROWSER_COMMAND:        
        for proc in psutil.process_iter(['name']):
           if browser.lower() in proc.info['name'].lower():               
            proc.kill()
            
        return JsonResponse({"message": f"{browser.capitalize()} stopped"})                
    return JsonResponse({'error' : "Unsupported Browser"})

def getUrl(request):
    browser = request.GET.get('browser')
    if browser in BROWSER_COMMAND:
        return JsonResponse({"url": f"URL is : {browser}"})

    return JsonResponse({"error": "Unsupported Browser"})

def cleanUp(request):
    browser = request.GET.get('browser')  
      
    path = ""    
    if browser == 'chrome' : 
        path = os.getenv("%LOCALAPPDATA%/Google/Chrome/User Data")
        
    elif browser == 'firefox':
        path = os.getenv("%APPDATA%/Mozilla/Firefox/Profiles" )    
        
    
    if os.path.exists(path):
        shutil.rmtree(path)     
        return JsonResponse({"message": f"{browser.capitalize()} cleaned"})
    return JsonResponse({"message": "Unsupported browser"})
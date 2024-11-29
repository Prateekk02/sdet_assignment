from django.shortcuts import render
import subprocess 
import os
from django.http import JsonResponse
import psutil

# Create your views here.

BROWSER_COMMAND = {
    'chrome': 'google-chrome' if os.name!='nt' else 'chorme',
    'firefox': 'firefox'
}

def start(request):
    browser = request.GET.get('browser')
    url = request.GET.get('url')
    
    if browser in BROWSER_COMMAND:
        subprocess.Popen([BROWSER_COMMAND[browser], url], shell=(os.name== 'nt')) 
        return JsonResponse({'message' : f"{browser.capitalize()} start with {url} "})
    return JsonResponse({'error': 'Unsupported browser'}, status = 400)
    

def stop(request):
    browser = request.GET.get('browser')
    if browser  in BROWSER_COMMAND:        
        for proc in psutil.process_iter(['name']):
           if browser.lower() in proc.info['name'].lower():               
            proc.kill()
            
        return JsonResponse({"message": f"{browser.capitalize()} stopped"})                
    return JsonResponse({'error' : "Unsupported Browser"})

from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
import asyncio
from . pAnalysis import search
import os
import json

# Create your views here.

def index(request):
	return HttpResponse("Hello World! You are at index page!")


async def slowresp():
	a = 1
	await asyncio.sleep(2)
	b = 1
	await asyncio.sleep(2)
	c = 2
	await asyncio.sleep(2)
	d = 2
	await asyncio.sleep(2)
	return [a, b, c, d]

async def makeSearch(dna_string):
	return search(dna_string)


async def search(request):
	par = request.GET.get('q')
	if par is None:
		print (os.getcwd())
		return HttpResponse("No Input")
	elif par == "":
		print (os.getcwd())
		return HttpResponse("Empty String/Invalid Input")
	else:
		print (os.getcwd())
		data = await makeSearch(par)
		if data == -1:
			data = {"success": 0}
		else:
			data["success"] = 1
		return HttpResponse(json.dumps(data))
	

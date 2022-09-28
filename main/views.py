from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy






def IndexView(request):
	if request.method == "POST":
		pass
		


	else:
		context = {}
		return render(request, "main/index.html", context )

        
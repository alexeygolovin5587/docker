from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from sample.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.parsers import JSONParser

from sample.callback import *
from rest_framework.decorators import api_view

from ansible import playbook, callbacks
from django.http import HttpResponse

import StringIO

import json

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CommandView(APIView):

    def get(self, request, format=None):
	cmd = {'cmd': self.request.GET.get('cmd', None)}

	res = run_playbook("/code/echo.yml", cmd)

	return Response(res)

    def post(self, request, format=None):
       
	print self.request.POST
	params = json.loads(self.request.POST.get('cmd', "{}"))

	if 'cmd' in params:
	  cmd = {'cmd': params['cmd']}
	else:
	  cmd = {}

	print cmd
	res = run_playbook("/code/echo.yml", cmd)

	return Response(res)

class AssetsCSVView(APIView):

    def get(self, request, format=None):
	s = StringIO.StringIO()
	s.write("pppp")

	# Grab ZIP file from in-memory, make response with correct MIME-type
	resp = HttpResponse(s.getvalue(), content_type="text/csv")

	return resp

command_view = CommandView.as_view()
assets_csv_view = AssetsCSVView.as_view()

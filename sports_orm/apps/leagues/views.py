from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"leaguesBaseball": League.objects.filter(name__contains="baseball"),
		"leaguesWomen": League.objects.filter(name__contains="women"),
		"leaguesHockey": League.objects.filter(name__contains="hockey"),
		"leaguesNotFoot": League.objects.exclude(name__contains="football"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
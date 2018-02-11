from django.shortcuts import render

def restaurant_list(request):
	context = {
		"restaurants": [
			{
				"name": "Subway",
				"description": "Healthy Food!",
				"opening_time": "12:00 am",
				"closing_time": "12:00 am"
			},
			{
				"name": "Domino's",
				"description": "Pizzaaaa!",
				"opening_time": "12:00 am",
				"closing_time": "12:00 am"
			},
			{
				"name": "Burger King",
				"description": "Not so Healthy Food!",
				"opening_time": "12:00 am",
				"closing_time": "12:00 am"
			},
			{
				"name": "KFC",
				"description": "Veryyyyyy not Healthy Food!",
				"opening_time": "12:00 am",
				"closing_time": "12:00 am"
			},
		]
	}
	return render(request, 'list.html', context)


def restaurant_detail(request):
	context = {
		"name": "Subway",
		"description": "Healthy Food!",
		"opening_time": "12:00 am",
		"closing_time": "12:00 am"
	}
	return render(request, 'detail.html', context)

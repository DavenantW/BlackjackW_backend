from django.contrib import admin
from users.models import users, statistics


@admin.register(users.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email',
    )


@admin.register(statistics.Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = (
        'player', 'money', 'games', 'wins',
    )

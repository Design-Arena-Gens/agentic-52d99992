from django.contrib import admin
from django.utils.html import format_html
from .models import Player


class AgeGroupListFilter(admin.SimpleListFilter):
    title = 'Age group'
    parameter_name = 'age_group'

    def lookups(self, request, model_admin):
        return (
            ('u14', 'Under 14'),
            ('u16', 'Under 16'),
            ('u17', 'Under 17'),
            ('u19', 'Under 19'),
        )

    def queryset(self, request, queryset):
        def age_to_group(age: int):
            if age < 14:
                return 'u14'
            if age < 16:
                return 'u16'
            if age < 17:
                return 'u17'
            if age < 19:
                return 'u19'
            return None
        value = self.value()
        if value:
            ids = [p.id for p in queryset if age_to_group(p.age) == value]
            return queryset.filter(id__in=ids)
        return queryset


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'category', 'gender', 'age', 'tournament_consent', 'institution_name', 'photo_tag')
    list_filter = ('gender', 'category', AgeGroupListFilter, 'tournament_consent')
    search_fields = ('name', 'registration_number', 'institution_name')

    def age(self, obj: Player):  # type: ignore[override]
        return obj.age

    def photo_tag(self, obj: Player):
        if obj.photo:
            try:
                return format_html('<img src="{}" style="height:40px;width:40px;object-fit:cover;border-radius:4px;"/>', obj.photo.url)
            except Exception:
                return "-"
        return "-"
    photo_tag.short_description = 'Photo'

from django.contrib import admin
from .models import JobListing, Application


# This part makes the Job list look organized in the admin panel
@admin.register(JobListing)
class JobAdmin(admin.ModelAdmin):
    # These columns will appear in your admin table
    list_display = ('title', 'company_name', 'category', 'salary_package', 'posted_at')

    # This adds a search bar to the admin panel
    search_fields = ('title', 'company_name')

    # This adds a filter sidebar
    list_filter = ('category', 'posted_at')


# Register the Application model normally
admin.site.register(Application)
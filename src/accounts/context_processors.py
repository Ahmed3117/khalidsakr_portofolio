from admin_interface.models import Theme
# myapp/context_processors.py
def site_logo(request):
    site_logo='static/imgs/site_logo/default_logo.png'
    try:
        # Get the first Theme object
        theme = Theme.objects.first()
        if theme and theme.logo:
            site_logo=theme.logo.url  # Assuming 'logo' is an ImageField
    except Theme.DoesNotExist:
        pass
    
    return {
        'site_logo': site_logo,
    }

from django import forms


# WEB_FRAMEWORKS='Web Frameworks'
# SETTING_UP_DJANGO='Setting up Django'
# URL_MAPPING = 'URL Mapping'
# ANY = 'Any'
# SECTION_CHOICES = [
#     (ANY, '--Any--'),
#     (WEB_FRAMEWORKS, 'Web Frameworks'),
#     (SETTING_UP_DJANGO, 'Setting up Django'),
#     (URL_MAPPING, 'URL Mapping'),
# ]

class SearchForm(forms.Form):
    WEB_FRAMEWORKS='Web Frameworks'
    SETTING_UP_DJANGO='Setting up Django'
    URL_MAPPING = 'URL Mapping'
    ANY = 'Any'
    SECTION_CHOICES = [
    (ANY, '--Any--'),
    (WEB_FRAMEWORKS, 'Web Frameworks'),
    (SETTING_UP_DJANGO, 'Setting up Django'),
    (URL_MAPPING, 'URL Mapping'),
]
    
    term_of_search = forms.CharField(max_length=200)
    section = forms.ChoiceField(choices=SECTION_CHOICES)
    
    

class AddForm(forms.Form):
    WEB_FRAMEWORKS='Web Frameworks'
    SETTING_UP_DJANGO='Setting up Django'
    URL_MAPPING = 'URL Mapping'
    ANY = 'Any'
    SECTION_CHOICES = [
    (ANY, '--Any--'),
    (WEB_FRAMEWORKS, 'Web Frameworks'),
    (SETTING_UP_DJANGO, 'Setting up Django'),
    (URL_MAPPING, 'URL Mapping'),
]
    
    section = forms.ChoiceField(choices=SECTION_CHOICES)
    text = forms.CharField(widget=forms.Textarea)


class EditForm(forms.Form):
    WEB_FRAMEWORKS='Web Frameworks'
    SETTING_UP_DJANGO='Setting up Django'
    URL_MAPPING = 'URL Mapping'
    ANY = 'Any'
    SECTION_CHOICES = [
    (ANY, '--Any--'),
    (WEB_FRAMEWORKS, 'Web Frameworks'),
    (SETTING_UP_DJANGO, 'Setting up Django'),
    (URL_MAPPING, 'URL Mapping'),
]
    
    section = forms.ChoiceField(choices=SECTION_CHOICES, disabled=True, required=False)
    text = forms.CharField(widget=forms.Textarea)
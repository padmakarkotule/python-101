from django import forms
from django.contrib.admin import widgets

"""
Notes on field ordering¶

In the as_p(), as_ul() and as_table() shortcuts, the fields are displayed in the order 
in which you define them in your form class. For example, in the ContactForm example, 
the fields are defined in the order subject, message, sender, cc_myself. To reorder the HTML 
output, just change the order in which those fields are listed in the class.

More granular output¶

The as_p(), as_ul(), and as_table() methods are simply shortcuts – they’re not the 
only way a form object can be displayed.

Also check Bound fields e.g.  BoundField.help_text¶
Form.is_multipart()

Ref. Link - https://docs.djangoproject.com/en/2.2/ref/forms/api/#django.forms.Form 
"""

"""
Built-in Field classes
- BooleanField
- CharField
- ChoiceField¶
- TypedChoiceField *
- DateField
- DateTimeField
- DecimalField   *
- DurationField *
- EmailField
- FileField * (Has two optional arguments for validation, max_length and allow_empty_file)
- FilePathField * (The field allows choosing from files inside a certain directory. It takes five extra arguments; only path is required:)
- FloatField *
- ImageField
- IntegerField
- GenericIPAddressField *
- MultipleChoiceField
- TypedMultipleChoiceField *
- NullBooleanField (Validates nothing (i.e., it never raises a ValidationError)
- RegexField * 
- SlugField * (This field is intended for use in representing a model SlugField in forms.)
- TimeField
- URLField
- UUIDField * (his field will accept any string format accepted as the hex argument to the UUID constructor.)
- ComboField * (Validates the given value against each of the fields specified as an argument to the ComboField.)
                E.g. f = ComboField(fields=[CharField(max_length=20), EmailField()])
- MultiValueField * Aggregates the logic of multiple fields that together produce a single value
- SplitDateTimeField * 

Fields which handle relationships - It's related to Model fields.

Creating custom fields *


"""

class UserForm(forms.Form):
    # Widget - Charfield
    #username = forms.CharField(label='Username', max_length=100, initial='Enter user name')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'djangoform'}), required=True, max_length="8")
    # Widget - Password
    # password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'djangoform'}))

    # Widget - Email
    # email = forms.EmailField(label='Email', initial='We need your email')
    # email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), required = True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'djangoform'}),
                                 required=True)

    # Widget - Integer Field - Same used for Phone number
    # contact = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone number', 'min':10}), required = True )
    contact = forms.IntegerField(
            widget=forms.NumberInput(attrs={'placeholder': 'Phone number', 'class': 'djangoform'}),
            required=True, help_text="Please enter 10 digit valid phone number.")

    # upload Multiple files
    #upload_image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class': 'fileupload'}), required=False)
    upload_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'fileupload'}),
                                   required=False)
    #upload_image = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'fileupload'}), required=False)

    # Date and Time Widgets
    # date = forms.DateField(widget=forms.SelectDateWidget)
    # date = forms.DateTimeField(widget = forms.SelectDateWidget())
    # date = forms.DateTimeField(widget = DatePickerInput(format='%m/%d/%Y'))
    # date = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True }))
    # date = forms.DateField(widget=widgets.AdminDateWidget)
    # date = forms.DateField(widget= forms.DateInput(format='%d/%m/%Y'))
    # # Using AdminDate and Time widget ##

    date = forms.DateField(widget=widgets.AdminDateWidget(attrs={'placeholder': 'Date'}), required=False)
    #time = forms.DateField(widget=widgets.AdminTimeWidget(attrs={'placeholder': 'Time'}), required=False)
    time = forms.TimeField(widget=widgets.AdminTimeWidget(attrs={'placeholder': 'Time'}), required=False)

    #  SelectDateWidget:
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    # Widget Multiple Chocies
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

    favorite_color = forms.MultipleChoiceField(widget=forms.SelectMultiple(), required=False, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False,
                                                choices=FAVORITE_COLORS_CHOICES)


    # Widget - Radio Chocies Widget
    CHOICES = [('1', 'First'), ('2', 'Second')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES, required=False)

    # Widget - url
    url = forms.URLField(widget=forms.URLInput(attrs={'Placeholder':'Enter url'}), required=False)


    # Widget - Charfield and Text Field
    description = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Short description','size': '40'}), required=False)
    comments = forms.CharField(widget=forms.Textarea(attrs={'Placeholder':"Enter Comment",'rows': 5}),required=False)

    # Widget - Boolen
    yes_no = forms.BooleanField(label="Are you coming?, Click check box if coming.", required=False)
    boolean_null = forms.BooleanField(required=False, widget=forms.NullBooleanSelect())
    yes_no = forms.BooleanField(label="Are you coming?, Click check box if coming.", required=False)
    On_Off = forms.BooleanField( widget=forms.CheckboxInput(attrs={'input type':'checkbox', 'checked data-toggle':'toggle'}), required=False)
    Enabled_Disabled = forms.BooleanField(label="Enabled/Disabled", required=False,
                                widget=forms.CheckboxInput(attrs={'data-on':'Enabled','data-off':'Disabled', 'data-toggle':'toggle'}))
    agree = forms.BooleanField(required=True)
    #yes_no = forms.BooleanField(widget=forms.CheckboxInput(), label="Are you coming?", required=False)

    # Widget - MultiWidget
    fields = (
        forms.CharField(widget=forms.TextInput(attrs={'class': 'big'})),
        forms.CharField(widget=forms.TextInput(attrs={'class': 'big'})),
        forms.CharField(widget=forms.TextInput(attrs={'class': 'big'})),
    )
    widge = [fields[0].widget, fields[1].widget, fields[2].widget]
   # multi_value = forms.MultiValueField(fields=fields, widget=forms.MultiWidget(widgets=(forms.TextInput, forms.TextInput, forms.TextInput)))
   # multi_value = forms.MultiValueField(widget=forms.MultiWidget(
   #     widgets=(forms.TextInput, forms.TextInput, forms.TextInput)))

    # When we use following widgetes it's showing error as -
    # Exception Type - AttributeError -
    # Exception Value: 'list' object has no attribute 'strip'
    # So planning to check this later once get some time to investigate.
    # It's working if we remove widget and values as 12/12/2019 (as date date)
    # multi_value = forms.DateTimeField(widget = forms.SplitDateTimeWidget())



from django import forms


class AddmaghaleForm(forms.Form):
    title_Maghale = forms.CharField( label ='Title',max_length = 200 )
    Code_Maghale = forms.IntegerField ( label='Article Code')
    Grouping_Maghale = forms.CharField( label ='Article Type',max_length = 50 )
    file = forms.FileField( label='File')
    ShortExplanation = forms.CharField(label='ShortExplanation', widget=forms.Textarea)
    number_of_Student = forms.IntegerField(label='Student Number')
    name_s = forms.CharField( label ='Student Name',max_length = 50 )
    name_p = forms.CharField( label ='Professor Name',max_length = 50 )



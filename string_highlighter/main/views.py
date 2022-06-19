from django.shortcuts import render
from . import ops

def index(request):
    start = ''
    end = ''
    string = ''
    hg_str = ''
    return render(request, "index.html", {
                'hg_str':hg_str ,
                'normal_str':string ,
                'start':start ,
                'end':end ,
                'string_length':len(string or '')})

def highlight_string(request):

    if request.method == 'POST':
      start = request.POST['start']
      end = request.POST['end']
      string = request.POST['inputText']
      hg_str = ops.html_string_with_highlight(string, start, end)
    return render(request, "index.html", {
            'hg_str':hg_str ,
            'normal_str':string ,
            'start':start ,
            'end':end ,
            'string_length':len(string or '')})
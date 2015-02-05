from string import lowercase

from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from django.template import RequestContext

from count.forms import CountTextForm


def home(r):
    c = dict(f=CountTextForm())
    if r.method == 'GET':
        c = RequestContext(r, c)
        return render_to_response('count/index.html', c)
    elif r.method == 'POST':
        f = CountTextForm(r.POST)
        if f.is_valid():
            e = dict()
            for d in f.cleaned_data['text']:
                if d in lowercase:
                    if d in e: e[d] = e[d] + 1
                    else: e[d] = 1
            for k, v in e.items():
                messages.info(r, "'%s' - %s" % (k, v))
            return redirect('home')
        messages.info(r, 'Redirecting to home.')
        return redirect('home')

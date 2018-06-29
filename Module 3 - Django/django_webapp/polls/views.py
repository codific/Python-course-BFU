from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Poll
from django.db.models import F
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    # Without get_object_or_404
    # try:
    #     poll = Poll.objects.get(id=poll_id)
    # except:
    #     raise Http404(f'Poll with id {poll_id} does not exist')
    # return render(request, 'polls/detail.html', {'poll': poll})

    # With get_object_or_404
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        return render(request, 'polls/results.html', {'poll': poll})
    except:
        return HttpResponse('No such poll')

def vote(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        voted_choice = poll.choice_set.get(pk=request.POST['choice'])
        # Using the F object saves us 1 DB query
        # it directly updates the value, without fetching the object first
        voted_choice.votes = F('votes') + 1
        voted_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(poll.id, ))
        )
    except:
        raise Http404('Wrong poll')


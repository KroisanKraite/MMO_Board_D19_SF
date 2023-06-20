from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser

from .models import *
from .forms import *
from .tasks import notify_author, notify_reply_accepted


@login_required
def accept_reply(request, pk):

    notify_reply_accepted.apply_async([pk], countdown=1)
    reply = Reply.objects.get(pk=pk)
    reply.status = True
    reply.save()

    return redirect('account')


class AddsList(LoginRequiredMixin, ListView):
    model = Advertisement
    ordering = '-date_publication'
    template_name = 'adds_list.html'
    context_object_name = 'adds'
    paginate_by = 2

    def get_queryset(self):
        category = self.request.path[-2:]
        queryset = super().get_queryset()
        self.filterset = Advertisement.objects.filter(category=category)
        return self.filterset


class AddsCreate(LoginRequiredMixin, CreateView):
    form_class = AddsForm
    model = Advertisement
    template_name = 'adds_create.html'
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = CustomUser.objects.get(username=self.request.user)
        post.date_publication = datetime.now()
        post.save()

        return super().form_valid(form)


class AddsUpdate(LoginRequiredMixin, UpdateView):
    form_class = AddsForm
    model = Advertisement
    template_name = 'adds_create.html'
    success_url = reverse_lazy('account')


class AddsDelete(LoginRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'adds_delete.html'
    success_url = reverse_lazy('account')


class ReplyCreate(LoginRequiredMixin, CreateView):
    form_class = ReplyForm
    model = Reply
    template_name = 'reply_create.html'

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.user = CustomUser.objects.get(username=self.request.user)
        reply.advertisement = Advertisement.objects.get(pk=self.kwargs['pk'])
        reply.save()
        self.success_url = self.request.POST.get('previous')

        notify_author.apply_async([reply.pk], countdown=1)

        return super().form_valid(form)


class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'reply_delete.html'
    success_url = reverse_lazy('account')


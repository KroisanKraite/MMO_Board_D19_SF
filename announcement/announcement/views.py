from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from adds.models import Advertisement, Reply
from adds.filters import ReplyFilter


class UserAccount(LoginRequiredMixin, ListView):
    model = Advertisement
    ordering = '-date_publication'
    template_name = 'user_page.html'
    context_object_name = 'adds'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        self.filterset = Advertisement.objects.filter(author=user)
        return self.filterset


class ReplyList(LoginRequiredMixin, ListView):
    model = Reply
    ordering = '-date_publication'
    template_name = 'reply_list.html'
    context_object_name = 'replies'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        queryset = Reply.objects.filter(advertisement__author=user)

        self.filterset = ReplyFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

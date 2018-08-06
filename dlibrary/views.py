from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from dlibrary.forms import  SuserForm
from dlibrary.models import Book, Feedback, Suser


def home(request):
    return render(request, 'home.html')


def front(request):
    return render(request, 'front.html')


@method_decorator(login_required, name='dispatch')
def cse(request):
    return render(request, 'cse.html')


def IT(request):
    return render(request, 'it.html')


def eee(request):
    return render(request, 'eee.html')


def etc(request):
    return render(request, 'etc.html')


def civil(request):
    return render(request, 'civil.html')


def mech(request):
    return render(request, 'mech.html')


def about(request):
    return render(request, 'about.html')


class FeedCreate(CreateView):
    success_url = reverse_lazy('hme')
    model = Feedback
    fields = ['name', 'email', 'mobno', 'subject', 'message']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FeedCreate, self).form_valid(form)


class BookList(ListView):
    model = Book

    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ''
        return Book.objects.all().filter(name__icontains=si).order_by('-id')


@method_decorator(login_required, name='dispatch')
class BookDetail(DetailView):
    model = Book


@method_decorator(login_required, name='dispatch')
class StudentUpdate(UpdateView):
    #     fields=["branch", "sem"]
    form_class = SuserForm
    model = Suser
    success_url = reverse_lazy('hme')


def chkstu(request):
    name2 = request.GET.get("name")
    if name2 is None or name2 == "":
        return render(request, 'chkstu.html')
    else:
        st = User.objects.filter(username=name2)
        if len(st) > 0:
            return render(request, 'chkstu.html', {"err2": "Username already taken "})
        else:
            return render(request, 'chkstu.html', {"err2": ""})


def chkeml(request):
    email2 = request.GET.get("email")
    if email2 is None or email2 == "":
        return render(request, 'chkeml.html')
    else:
        st = User.objects.filter(email=email2)
        if len(st) > 0:
            return render(request, 'chkeml.html', {"err3": "This email is already registered with another username"})
        else:
            return render(request, 'chkeml.html', {"err3": ""})


@method_decorator(login_required, name='dispatch')
class MyListc(TemplateView):
    template_name = "cse.html"

    def get_context_data(self, **kwargs):
        fi = 'CSE'
        context = TemplateView.get_context_data(self, **kwargs)
        context["books"] = Book.objects.all().filter(branch__name__contains='CSE').order_by('id')[:]
        return context


@method_decorator(login_required, name='dispatch')
class MyListe(TemplateView):
    template_name = "etc.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["books"] = Book.objects.all().filter(branch__name__contains='ET&T').order_by('id')[:]
        return context


@method_decorator(login_required, name='dispatch')
class MyListi(TemplateView):
    template_name = "it.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["books"] = Book.objects.all().filter(branch__name__contains='IT').order_by('id')[:]
        return context


@method_decorator(login_required, name='dispatch')
class MyListci(TemplateView):
    template_name = "civil.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["books"] = Book.objects.all().filter(branch__name__contains='CIVIL').order_by('id')[:]
        return context


@method_decorator(login_required, name='dispatch')
class MyListm(TemplateView):
    template_name = "mech.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["books"] = Book.objects.all().filter(branch__name__contains='MECH').order_by('id')[:]
        return context


@method_decorator(login_required, name='dispatch')
class MyListee(TemplateView):
    template_name = "eee.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["books"] = Book.objects.all().filter(branch__name__contains='EEE').order_by('id')[:]
        return context

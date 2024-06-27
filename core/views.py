from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Dish
from .forms import SignUpForm, LogInFrom
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sign_log'] = self.request.user.is_authenticated
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        query = request.POST.get('query')
        if query:
            dishes = Dish.objects.filter(name__icontains=query)
            paginator = Paginator(dishes, 5)  # Show 5 dishes per page.
            page_number = request.POST.get('page')
            page_obj = paginator.get_page(page_number)
            context['results'] = page_obj
            context['query'] = query
        return self.render_to_response(context)

class UserSignUpView(FormView):
    template_name = 'core/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(BaseLoginView):
    template_name = 'core/login.html'
    form_class = LogInFrom
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

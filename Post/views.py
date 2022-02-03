from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from .models import Product
from .forms import PostForm

# Create your views here.
class PostFormView(View):
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'post_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse_lazy('post:image_display', kwargs={'pk': obj.id}))
            # pm=form.cleaned_data.get("payment_method")
            # if pm=="Khalti":
            #     return redirect(reverse("post:khaltirequest"))
            return redirect('/post/success/')
        return render(request, self.template_name, {'form': form})

class PostSuccess(TemplateView):
    template_name = 'post_success.html'
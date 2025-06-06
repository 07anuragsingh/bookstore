from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import redirect
from .models import Book, Contact, Profile
from .form import ProfileForm  # Assuming you have a ProfileForm in forms.py

class HomeView(TemplateView):
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_books'] = Book.objects.filter(is_visible=True)[:10]
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('books:home')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(is_visible=True)

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.filter(is_visible=True)

class MyProfile(ListView):
    model = Book
    context_object_name = 'profiles' # Assuming you have a Profile model
      
    template_name = 'books/my_profile.html'

    def get_queryset(self):
        return Profile.objects.filter(email='anuragsingh8434845379@gmail.com') # Assuming you want to filter by the logged-in user's email

class Form(TemplateView):
    template_name = 'books/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            Profile=form.save(commit=False)  # Create a Profile instance but don't save it yet
            form.save()
            return redirect('books:home')
        return self.render_to_response(self.get_context_data(form=form))
          # Redirect to the home page after form submission

    


    

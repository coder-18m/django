from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category, Comment, Subscribers
from .forms import PostForm, CommentForm, SubscribersForm, MailMessageForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django_pandas.io import read_frame
from django.conf import settings

import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Place

def subscribe(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            post_data = request.POST.copy()
            email = post_data.get("email", None)
            Subscribers.email = email
            form.save()
            # send a confirmation mail
            subject = 'NewsLetter Subscription'
            message = 'Thanks for subscribing to us. Your email ' + email +  ' will now be receiving newsletter emails from CALV. If you have not yet, sign our petition found on our website at www.contactcalv.org.  Please do not reply to this email.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            # send a confirmation mail to host
            subjectB = 'New Subscription'
            messageB = 'The ' + email +  ' has subscribed to the CALV emailing list.'
            email_fromB = settings.EMAIL_HOST_USER
            recipient_listB = [settings.EMAIL_HOST_USER, ]
            send_mail(subjectB, messageB, email_fromB, recipient_listB)
            messages.success(request, 'Subscription Successful')
            return redirect('subscribe')  
    else:
        form = SubscribersForm()
    context = {
        'form': form,

    }
    return render(request, 'news/subscribe.html', context)

def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                'calv.official@outlook.com',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Email sent to Mail List')
            return redirect('mail_letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,

    }
    return render(request, 'news/mail_letter.html', context)


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

#export addresses funciton
def export_addresses_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="addresses.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['First Name', 'Last Name', 'Address']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Place.objects.all().values_list('first_name', 'last_name', 'address')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

#export Subscribers
def export_subscribers_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="subscribers.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Subscribers')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Emails']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Subscribers.objects.all().values_list('email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))




def index(request):
    return render(request, 'index.html', {})

def donate(request):
    return render(request, 'donate.html', {})


class DevelopmentView(TemplateView):
    template_name = 'development_sum.html'

class DevelopmentMapView(TemplateView):
    template_name = 'develop_map.html'

class TransportMapView(TemplateView):
    template_name = 'transport_map.html'

class SchoolsMapView(TemplateView):
    template_name = 'schools_map.html'

class SampleLetterView(TemplateView):
    template_name = 'sample_letter.html'

#class ContactView(TemplateView):
#    template_name = 'contact.html'
# contactCALV@gmail.com

def contact(request):
    if request.method == "POST":
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
        }
        message = '''
        {}
        From: {}

        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, 'calv.official@outlook.com', ['calv.official@outlook.com'])

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})

class FireView(TemplateView):
    template_name = 'fire.html'

class EditView(TemplateView):
    template_name = 'edit_letter.html'

#def home(request):
    #return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['pk']})

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    #fields = ['title', 'author', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

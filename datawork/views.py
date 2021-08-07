from .forms import *
from .models import *
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

# Create your views here.


def marketingindex(r):
    if r.method == 'POST':
        P = indexHead()
        P.image = r.POST.FILES.get('image')
        P.title = r.POST.get('title')
        P.subhead = r.POST.get('subhead')
        P.save()
    content = {
        "pet": indexHead.objects.all(),
        "form": SubscribeForm

    }

    return render(r, 'public/marketing-index.html', content)


def marketingblog(r):
    return render(r, "public/marketing-blog.html", {"form": SubscribeForm()})


def marketingcategory(r):

    return render(r, "public/marketing-category.html", {"form": SubscribeForm()})


def marketingcontact(r):
    forms = ContactForm(r.POST or None)
    if r.method == "POST":
        if forms.is_valid():
            c = contactForm()
            c.name = r.POST.get("name")
            c.email = r.POST.get("email")
            c.phone = r.POST.get('phone')
            c.subject = r.POST.get('subject')
            c.message = r.POST.get('message')
            c.save()
            messages.success(r, 'Form  has been submited successfully')
            return redirect(marketingcontact)
    return render(r, "public/marketing-contact.html", {
        "cat": contactForm.objects.all()
    })


def subs(r):
    forms = SubscribeForm(r.POST or None)
    if r.method == "POST":
        if forms.is_valid():
            S = Subscriber()
            S.email = r.POST.get("email")
            if Subscriber.objects.filter(email=email).exists():
                messages.WARNING(
                    r, "Email is already exists or you are already subscribed")
                return redirect(marketingindex)
            else:
                S.save()
                messages.success(r, 'You Have been Subscribed successfully ')
                return redirect(marketingindex)

    return render(r, "public/marketing-index.html", )


def marketingsingle(r):
    return render(r, "public/marketing-single.html")


# @permission_required('user.is_superuser')
def dashboard(r):
    return render(r, "private/dashboard.html")


def email(r):
    return render(r, 'private/email.html')


def error(r):
    return render(r, "private/404_error.html")


def calendar(r):
    return render(r, 'private/calendar.html')


def charts(r):
    return render(r, 'private/charts.html')


def contact(r):
    return render(r, 'private/contact.html', {
        "cat": contactForm.objects.all(), })


def dashboard_2(r):
    return render(r, 'private/dashboard_2.html')


def general_elements(r):
    return render(r, 'private/general_elements.html')


def icons(r):
    return render(r, 'private/icons.html')


def index(r):
    return render(r, 'private/index.html')


def invoice(r):
    return render(r, 'private/invoice.html')


def login(r):
    return render(r, 'private/login.html')


def map(r):
    return render(r, 'private/map.html')


def media_gallery(r):
    return render(r, 'private/media_gallery.html')


def price(r):
    return render(r, 'private/price.html')


def profile(r):
    return render(r, 'private/profile.html')


def project(r):
    return render(r, 'private/project.html')


def settings(r):
    return render(r, 'private/settings.html')


def tables(r):
    return render(r, 'private/tables.html')


def widgets(r):
    return render(r, 'private/widgets.html')


def success(r):
    return render(r, 'public/success.html')


def subscribers(r):
    return render(r, 'private/subscribers.html', {"form": Subscriber.objects.all()})


def managebanner(r):
    return render(r, 'private/managebanner.html', {"pet": indexHead.objects.all()})


def banneredit(r, id):
    get_id = indexHead.objects.get(id=id)
    forms = Indexheadform(r.POST or None, r.FILES or None, instance=get_id)
    if r.method == "POST":
        if forms.is_valid():
            forms.save()
            return redirect(managebanner)
    return render(r, 'private/banner_edit.html', {
        "pet": indexHead.objects.all(),
        "form": forms,
    }
    )


def delete_banner(r, id):
    get_id = indexHead.objects.get(id=id)
    get_id.delete()
    return redirect(managebanner)


def update(request, id):
    P = indexHead.objects.get(pk=id)
    form = Indexheadform(request.POST, instance=P)
    if form.is_valid:
        form.save()
        P = indexHead.objects.all()
        return redirect(managebanner, {'pet': P})


def addbanner(r):
    forms_ = Indexheadform(r.POST or None, r.FILES or None, )
    if r.method == "POST":
        if forms_.is_valid():
            forms_.save()
            return redirect(managebanner)
    return render(r, 'private/add.html', {
        "pet": indexHead.objects.all(),
        "form": forms_,
    }
    )

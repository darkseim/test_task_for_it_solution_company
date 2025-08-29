from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import QuoteForm
from .models import Quote
from random import choice

def index(request):
    all_quotes = list(Quote.objects.all())
    if all_quotes:
        weighted_list = []
        for quote in all_quotes:
            weighted_list.extend([quote] * quote.weight)
        selected_quote = choice(weighted_list)
        selected_quote.views += 1
        selected_quote.save(update_fields=['views'])
    else:
        selected_quote = None
    return render(request, 'quotes/index.html', {'quote': selected_quote})

def add(request):
    if request.method == "GET":
        form = QuoteForm()
    else:
        form = QuoteForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data["author"]
            text = form.cleaned_data["text"]
            if Quote.objects.filter(author=author).count() >= 3:
                messages.error(request,
                               f"У автора «{author}» уже есть 3 цитаты!")
            elif Quote.objects.filter(text=text).exists():
                messages.error(request, "Такая цитата уже существует!")
            else:
                form.save()
                messages.success(request, "Цитата добавлена!")
                return redirect("quotes:add")
    return render(request, "quotes/add.html", {"form": form})

def top_quotes(request):
    top_10 = Quote.objects.order_by('-likes')[:10]
    return render(request, 'quotes/top.html', {'quotes': top_10})


@require_POST
def vote(request, quote_id, action):
    quote = Quote.objects.get(id=quote_id)
    if action == 'like':
        quote.likes += 1
    elif action == 'dislike':
        quote.dislikes += 1
    quote.save(update_fields=['likes', 'dislikes'])
    return redirect('quotes:index')
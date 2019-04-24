from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from blogify.models import Audience, Article
from blogify.forms  import AudienceForm, ArticleForm


def view_audiences(request):
#return a list of all audience objects
	audiences = Audience.objects.all()
	return render(request,"blog/audience/audiences.html",{"audiences":audiences})

def view_articles(request):
#Return a list of all article objects
	
	articles = Article.objects.all()

	page = request.GET.get('page',1)
	paginator = Paginator(articles,1)

	try:
		page_articles = paginator.page(page)

	except PageNotAnInteger:
		page_articles = paginator.page(1)

	except EmptyPage:
		page_articles = paginator.page(paginator,num_pages)

	page_articles.count = articles.count()

	return render(request,"blog/article/articles.html",{"articles":page_articles})

def view_audience(request,audience_id):
# Return an audience that match the requested audience-id
	url = "/blogify/update_audience/{!s}/".format(audience_id)
	return redirect(url)


def view_article(request,article_id):
# Return an article that match the requested article-id

	try:
		article = Article.objects.get(id = article_id)

		return render(request,"blog/article/article.html",{"article":article})
	except ObjectDoesNotExist:
		error_msg = "The request article does not exist"
		articles = Article.objects.all()
		page = request.GET.get('page',1)
		paginator = Paginator(articles,1)

		try:
			page_articles = paginator.page(page)

		except PageNotAnInteger:
			page_articles = paginator.page(1)

		except EmptyPage:
			page_articles = paginator.page(paginator,num_pages)

		page_articles.count = articles.count()

		return render(request,"blog/article/articles.html",{"articles":page_articles,"error_msg":error_msg})



def add_audience(request):
# Add Audience to database if request method is POST else return add_audience form page if request method is GET

	if request.method == 'POST':
		audience_form = AudienceForm(request.POST)

		if audience_form.is_valid():
			audience = Audience()
			audience.name = audience_form.cleaned_data['name']
			audience.description = audience_form.cleaned_data['description']
			audience.save()

			success_msg = "Your have added audience {!s} to your audience list.".format(audience.name)

			audiences = Audience.objects.all()

			return render(request,"blog/audience/audiences.html",{"audiences":audiences,"success_msg":success_msg})

		else:
			error_msg = "The form you have submitted is not valid. Please ensure that you fill in all required fields and try again."
			return render(request,"blog/audience/add_audience.html",{"form":audience_form,"error_msg":error_msg})
	else:
		audience_form = AudienceForm()
		return render(request,"blog/audience/add_audience.html",{"form":audience_form})


def add_article(request):
# Add Article to database if request method is POST else return add_article form page

	if request.method == 'POST':
		article_form = ArticleForm(request.POST,request.FILES)
		if article_form.is_valid():
			article = Article()
			article.title = article_form.cleaned_data['title']
			article.context_image = article_form.cleaned_data['context_image']
			article.description = article_form.cleaned_data['descriptionSSSS']
			article.body = article_form.cleaned_data['body']
			article.active = article_form.cleaned_data['active']
			article.audience = article_form.cleaned_data['audience']
			article.author = request.user

			article.save()
			success_msg = "Your have added article {!s} to your articles list.".format(article.title)
			return render(request,"blog/article/article.html",{"article":article,"success_msg":success_msg})

		else:
			error_msg = "The form you have submitted is not valid. Please check that all requested fields at filled and try again."
			return render(request,"blog/article/add_article.html",{"form":article_form,"error_msg":error_msg})

	else:
		article_form = ArticleForm()
		return render(request,"blog/article/add_article.html",{"form":article_form})



def update_audience(request,audience_id):
# Updates an Audience's details if request method is POST else returns update_audience form page if request method is GET
	
	#Verify that the requested audience actually exists
	audience = None
	try:
		audience = Audience.objects.get(id = audience_id)
	except ObjectDoesNotExist:
		error_msg = "The requested audience object does not exist"
		audiences = Audience.objects.all()
		return render(request,"blog/audience/audiences.html",{"audiences":audiences,"error_msg":error_msg})
	

	if request.method == 'POST':
		audience_form = AudienceForm(request.POST)

		if audience_form.is_valid():
			audience.name = audience_form.cleaned_data['name']
			audience.description = audience_form.cleaned_data['description']
			audience.save()

			success_msg = "You have updated audience {!s}.".format(audience.name)
			audiences = Audience.objects.all()

			return render(request,"blog/audience/audiences.html",{"audiences":audiences,"success_msg":success_msg})

		else :
			error_msg = "The form you have submitted is not valid. Please ensure that you fill in all required fields and try again."
			return render(request,"blog/audience/update_audience.html",{"form":audience_form,"error_msg":error_msg,"audience_id":audience_id})

	else:
		audience_form = AudienceForm()
		audience_form.fields['name'].initial = audience.name
		audience_form.fields['description'].initial = audience.description

		return render(request,"blog/audience/update_audience.html",{"form":audience_form,"audience_id":audience_id})


def update_article(request,article_id):
# Update an article's details id request method is POST else return update_article form page

	#verify that the requested article exists
	article = None
	try:
		article = Article.objects.get(id = article_id)

	except ObjectDoesNotExist:
		error_msg = "The requested article does not exist"
		articles = Article.objects.all()
		return render(request,"blog/article/articles.html",{"articles":articles,"error_msg":error_msg})

	if request.method == 'POST':
		article_form = ArticleForm(request.POST,request.FILES)

		if article_form.is_valid():
			article.title = article_form.cleaned_data['title']
			article.body = article_form.cleaned_data['body']
			article.description = article_form.cleaned_data['description']
			article.audience = article_form.cleaned_data['audience']
			context_image = article_form.cleaned_data['context_image']
			active = article_form.cleaned_data['active']
			if context_image:
				article.context_image = context_image

			article.save()

			success_msg = "You have updated article {!s}.".format(article.title)

			return render(request,"blog/article/article.html",{"article":article,"success_msg":success_msg})
		else:
			error_msg = "The form you have submiited is not valid. Please fill in all requested fields and try again."
			return render(request,"blog/article/update_article.html",{"form":article_form,"error_msg":error_msg,"article_id":article_id})
	else: # is GET
		article_form = ArticleForm()
		article_form.fields['title'].initial = article.title
		article_form.fields['context_image'].initial = article.context_image
		article_form.fields['description'].initial = article.description
		article_form.fields['body'].initial = article.body
		article_form.fields['active'].initial = article.active
		article_form.fields['audience'].initial = article.audience

		return render(request,"blog/article/update_article.html",{"form":article_form,"article_id":article_id})



def delete_audience(request,audience_id):
#Delete an audience object if request method is POST else ask for confirmation before deleting

	#first check if requested audience exists
	audience = None
	try:
		audience = Audience.objects.get(id = audience_id)

	except ObjectDoesNotExist:
		error_msg = "The requested audience object does not exist"
		audiences = Audience.objects.all()
		return render(request,"blog/audience/audiences.html",{"audiences":audiences,"error_msg":error_msg})

	if request.method == 'POST':
		audience_name = audience.name
		audience.delete()

		audiences = Audience.objects.all()
		success_msg =  "You have successfully deleted audience {!s}".format(audience_name)

		return render(request,"blog/audience/audiences.html",{"audiences":audiences,"success_msg":success_msg,"audience_id":audience_id})
	else :
		related_articles = Article.objects.filter(audience = audience)
		return render(request,"blog/delete_parent.html",{"object_type":"Audience","audience":audience,"related_articles":related_articles,"audience_id":audience_id})



def delete_article(request,article_id):
#Delete an article object if request method is POST else ask for confirmation before deleting article

	#First check if requested article exists
	audience = None
	try:
		article = Article.objects.get(id = article_id)

	except ObjectDoesNotExist:
		error_msg = "The requested article does not exist"
		articles = Article.objects.all()
		return render(request,"blog/article/articles.html",{"articles":articles,"error_msg":error_msg})

	if request.method == 'POST':
		article_title = article.title
		article.delete()

		articles = Article.objects.all()
		success_msg = "You have successfully deleted article - {!s}.".format(article_title)

		page = request.GET.get('page',1)
		paginator = Paginator(articles,1)

		try:
			page_articles = paginator.page(page)

		except PageNotAnInteger:
			page_articles = paginator.page(1)

		except EmptyPage:
			page_articles = paginator.page(paginator,num_pages)

		page_articles.count = articles.count()

		return render(request,"blog/article/articles.html",{"articles":page_articles,"success_msg":success_msg})

	else:
		return render(request,"blog/delete_parent.html",{"object_type":"Article","article":article})
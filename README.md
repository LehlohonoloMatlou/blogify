blogify


Blogify is a simple blogging system with a nice WYSIWYG text editor and infinite page paginator.
You are supposed to add your own frontend code.s


SETUP

1. Add 'blogify' to your python environment

2. Add `blogify` to `INSTALLED_APP` in `settings.py`.

        INSTALLED_APPS += ('blogify', )

3. Add `blogify.urls` to `urls.py`.

        urlpatterns = [
            ...
            url(r'^blogify/', include('blogify.urls')),
            ...
        ]

4. Be sure to set proper `MEDIA_URL` for attachments.
     - The following is an example test code:
     
           MEDIA_URL = '/media/'
           MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    
     - When debug option is enabled(```DEBUG=True```), DO NOT forget to add urlpatterns as shown below:
     
            
            if settings.DEBUG:
                urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
            
     - Please, read the official document more in detail: <https://docs.djangoproject.com/en/1.11/topics/files/>
            from django.conf import settings
            from django.conf.urls.static import static

5. Be sure to set 'LOGIN_URL' in 'settings.py' to require logging in.


Usage
---
When running locally, go to http://127.0.0.1:8000/blogify/articles/

Blogify was implemented with the assumption that you will provide your own frontend work.


To display blogs for a specific audience use Articles.objects.filter(audience__title = 'name_of_target_audience')
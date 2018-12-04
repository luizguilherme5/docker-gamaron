from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from api.users.views import UserViewSet, GroupViewSet
from api.itens.views import ItenViewSet, PlayerInvetoryViewSet
from api.quests.views import QuestViewSet, JournalViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'itens', ItenViewSet)
router.register(r'inventory', PlayerInvetoryViewSet)
router.register(r'quests', QuestViewSet)
router.register(r'journal', JournalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = [
#     path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
#     path(
#         "about/",
#         TemplateView.as_view(template_name="pages/about.html"),
#         name="about",
#     ),
#     # Django Admin, use {% url 'admin:index' %}
#     path(settings.ADMIN_URL, admin.site.urls),
#     # User management
#     path(
#         "users/",
#         include("docker_gamaron.users.urls", namespace="users"),
#     ),
#     path("accounts/", include("allauth.urls")),
#     # Your stuff: custom urls includes go here
# ] + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
# )

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

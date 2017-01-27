from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from articles.models import Article
from articles.models import Comment
from articles.models import ArticleLike
from articles.models import CommentLike


# Article views
class ArticleListView(ListView):
    template_name = "list.html"
    model = Article


class ArticleDetailView(DetailView):
    template_name = "detail.html"
    model = Article

    def tweet(self):
        return '"{}" by @{} http://www.soufflemignon.com/blog/{}/'.format(
            self.get_object().title,
            'mitchellgoffpc'
                if self.get_object().author == 'Mitchell Goff'
                else 'gabrewsk1',
            self.get_object().slug)

    def comments(self):
        return (self.get_object().comments
            .filter(article=self.get_object())
            .annotate(num_likes=Count('likes'))
            .order_by('-num_likes', '-date')
            .prefetch_related(
                'user',
                'likes',
                'likes__user'))



# Like AJAX view
class LikeView(View):
    def post(self, request, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied

        if request.POST.get('type') == 'article':
            model = ArticleLike
            related_model = Article
            field = 'article'
        elif request.POST.get('type') == 'comment':
            model = CommentLike
            related_model = Comment
            field = 'comment'
        else:
            raise PermissionDenied

        try:
            obj = related_model.objects.get(id=request.POST.get('id'))
            data = { 'user': request.user, field: obj }
        except related_model.DoesNotExist:
            raise PermissionDenied

        if request.POST.get('action') == 'create':
            model.objects.create(**data)
        elif request.POST.get('action') == 'delete':
            model.objects.filter(**data).delete()
        else:
            raise PermissionDenied

        return HttpResponse('success')



# Comment AJAX view
class CommentView(View):
    def post(self, request, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied

        try:
            article = Article.objects.get(id=request.POST.get('article'))
        except Article.DoesNotExist:
            raise PermissionDenied

        if request.POST.get('action') == 'create':
            comment = Comment.objects.create(
                user = request.user,
                article = article,
                entry = request.POST.get('entry'))
            comment.num_likes = 0
            return render(request, "comment.html", { 'comment': comment })

        elif request.POST.get('action') == 'delete':
            Comment.objects.filter(
                user = request.user,
                id = request.POST.get('id')).delete()
            return HttpResponse('success')

        elif request.POST.get('action') == 'edit':
            comment = Comment.objects.filter(
                user = request.user,
                id = request.POST.get(id)).first()

            if comment:
                comment.entry = request.POST.get('entry')
                comment.save()
                return render(request, "comment.html", { 'comment': comment })
            else:
                raise PermissionDenied

        else:
            raise PermissionDenied

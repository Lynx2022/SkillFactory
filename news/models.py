from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum



class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()








class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)



class Post(models.Model):
    article = 'ar'
    new = 'ne'
    POSTVARIETY = [
        (article, 'Статья'),
        (new, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_variety = models.CharField(max_length=2, choices=POSTVARIETY, default=article)
    dateCreation = models.DateTimeField(auto_now_add=True)
    categoryType = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=255, default="Новый контент")
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'



class PostCategory(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryTrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()




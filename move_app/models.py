from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Директор"
        verbose_name_plural = "Директоры"


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    duration = models.PositiveIntegerField(verbose_name="Продолжительность")
    director = models.ForeignKey(Director,
                                 on_delete = models.CASCADE,
                                 verbose_name='Резиссер',
                                 related_name='movies',)

    def __str__(self):
        return f'{self.title} - {self.director.name}'
    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural  = 'Фильмы'



STARS = [(i, (str(i))) for i in range(1,6)]
class Review(models.Model):
    text = models.TextField(verbose_name='Текст')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,
                              verbose_name='Фильмы',related_name='reviews')
    star = models.IntegerField(choices=STARS,verbose_name="Оценка", default=5)
    def __str__(self):
        return f'Review - {self.movie.title}'
    class Meta:
        verbose_name= 'Отзыв'
        verbose_name_plural = 'Отзывы'



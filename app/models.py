from django.db import models
from django.urls import reverse
from datetime import datetime


'''1.users- those who have account, recognize by user_name'''


class User(models.Model):
    name = models.CharField(max_length=128, verbose_name='UserName')
    email = models.CharField(max_length=128, verbose_name='Login Email')
    password = models.CharField(max_length=25, verbose_name='Password')
    created = models.DateTimeField(auto_now=True, verbose_name='Created on')

    class Meta:
        verbose_name = 'Content User'
        verbose_name_plural = 'Content Users'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        pass


'''2. content - movies stored in database'''
class Content(models.Model):

    COMPLETE = 'com'
    ON_GOING = 'on'
    TVShow = 'show'
    Movie = 'movie'

    StatusChoices = (
        (COMPLETE, 'Fully uploaded'),
        (ON_GOING, 'Still uploading'),
    )

    TypeChoices = (
        (Movie, 'movie'),
        (TVShow, 'show')
    )

    name = models.CharField(max_length=128, verbose_name='Content Name')
    type = models.CharField(max_length=5, choices=TypeChoices, verbose_name='type')
    status = models.CharField(max_length=3, choices=StatusChoices, verbose_name='status')
    studio = models.CharField(max_length=128, verbose_name='Make By')
    year = models.CharField(max_length=5, verbose_name='Publish Year')
    country = models.CharField(max_length=128, verbose_name='Country Make')
    poster = models.FileField(default=None, verbose_name='poster')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        pass


'''3.Part/season - movies may split into parts and series may split into seasons'''
class Season(models.Model):
    name = models.CharField(max_length=128, verbose_name='Show Name')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='Seasons', verbose_name='Content')

    class Meta:
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'

    def __str__(self):
        return str(self.content) + ' - ' + str(self.name)


'''5. genres- the genres of all movies'''
class Genre(models.Model):
    name = models.CharField(max_length=128, verbose_name='Genre')

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name


'''6. Classification'''
class Classification(models.Model):
    movie = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Movie')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Genre')

    class Meta:
        verbose_name = 'Classification'
        verbose_name_plural = 'Classifications'


'''7. Episode'''
class Episode(models.Model):
    number = models.CharField(max_length=4, verbose_name='Ep Num')
    name = models.CharField(max_length=128, verbose_name='Ep Name')
    content = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episode', verbose_name='episode')
    link = models.FileField(default=None, verbose_name='link')

    class Meta:
        verbose_name = 'Episode'
        verbose_name_plural = 'Episodes'

    def __str__(self):
        return str(self.content) + ' - ep ' + self.number + ': ' + self.name


''' HR- for search engine'''
class HR(models.Model):
    DIRECTOR = 'dir'
    ACTOR = 'act'
    JobChoices =(
        (DIRECTOR, 'director'),
        (ACTOR, 'actor')
    )

    name = models.CharField(max_length=128, verbose_name='Name')
    birth = models.DateField(default=None, verbose_name='BirthDay')
    country = models.CharField(max_length=128, verbose_name='Nationality')
    JobChoices = models.CharField(max_length=5, choices=JobChoices, verbose_name='job')
    image = models.FileField(default=None, verbose_name='image')

    class Meta:
        verbose_name = 'HR'
        verbose_name_plural = 'HRs'

    def __str__(self):
        return self.name


'''10.Crew - Directors participate in movies/shows'''
class Crew(models.Model):
    hr = models.ForeignKey(HR, on_delete=models.CASCADE, verbose_name='crew')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='movie/show')

    class Meta:
        verbose_name = 'Crew'
        verbose_name_plural = 'Crews'


'''13. Error type - error to report'''
'''class ErrorType(models.Model):
    name = models.CharField(max_length=128, verbose_name='ERROR')
    description = models.CharField(max_length=128, verbose_name='Description')

    class Meta:
        verbose_name = 'Error'
        verbose_name_plural = 'Errors'

    def __str__(self):
        return self.name
'''

'''14.Report - user report error on a episode'''
class Report(models.Model):
    LabelingProblem = 'label'
    VideoProblem = 'video'
    SoundProblem = 'sound'
    SubtitlesProblem = 'sub'
    ConnectionProblem = 'connect'

    ProblemChoices = (
        (LabelingProblem, 'Labeling Problem'),
        (VideoProblem, 'Video Problem'),
        (SoundProblem, 'Sound Problem'),
        (SubtitlesProblem, 'Subtitles Problem'),
        (ConnectionProblem, 'Connection Problem'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report', verbose_name='User')
    content = models.ForeignKey(Episode, on_delete=models.CASCADE, verbose_name='Content')
    type = models.CharField(max_length=10, choices=ProblemChoices, default=ProblemChoices[1], verbose_name='Problem type')
    time = models.DateTimeField(auto_now=True, verbose_name='Reported At')

    class Meta:
        verbose_name = "Content's Report"
        verbose_name_plural = "Content's Reports"

    def __str__(self):
        pass


'''15. UserList- User's personal list of movie/show'''
class UserList(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moviecloset')
    '''invite?'''
    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'

    def __str__(self):
        return str(self.user) + ' - ' + str(self.name)


'''16.UserListDetail - the detail of a userlist'''
class UserListDetail(models.Model):
    closet = models.ForeignKey(UserList, on_delete=models.CASCADE, related_name='movies', verbose_name='list')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Content')

    class Meta:
        verbose_name = 'Detail'
        verbose_name_plural = 'Details'

    def __str__(self):
        pass


'''17. WatchHistory - the watch history of a user and a movie.show'''
class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='WatchHistory', verbose_name='user')
    content = models.ForeignKey(Episode, on_delete=models.CASCADE, verbose_name='content')
    time = models.DateTimeField(auto_now=True, verbose_name='watch time')

    class Meta:
        verbose_name = "Content's watch history"
        verbose_name_plural = "Content's watch histories"

    def __str__(self):

        if(self.content.content.content.type == 'show'):

            return str(self.user) + ' - ' + str(self.content) + '-' + str(self.time)

        else:

            return str(self.user) + '-' + str(self.content.content.content) + '-' + str(self.time)

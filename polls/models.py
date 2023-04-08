import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    '''
    Classe para perguntas
     
    question_text = uma pergunta em formato de texto
    pub_date = data da publicação
    
    '''

    question_text = models.CharField(max_length=200) # CharField = Char
    pub_date = models.DateTimeField("date published") # DateTimeField = DateTime

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    '''
    Classe para escolha de voto
     
    question_text = uma pergunta em formato de texto
    choice_text = texto da escolha
    votes = contagem de votos
    
    '''

    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey = FK
    choice_text = models.CharField(max_length=200) # CharField = Char
    votes = models.IntegerField(default=0) # IntegerField = Int

    def __str__(self):
        return self.choice_text
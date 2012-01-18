from django.db import models
from django.conf import settings
from django.core.mail import send_mail

class Feedback(models.Model):
    """
    This model includes all the feedback
    given for the softGIS django application.
    
    When a feedback is saved it sends an email
    to the administrators as set in settings.py.
    
    >>> import settings
    >>> from softgis.models import Feedback
    >>> from django.core import mail
    >>> fb = Feedback(content='some feedback')
    >>> fb.save()
    >>> mail.outbox[0].body
    'some feedback'
    """
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        send_mail('Feedback for the softGIS application',
                self.content,
                'do-not-reply@pehmogis.fi',
                [admin[1] for admin in settings.ADMINS],
                fail_silently=True)
            
        super(Feedback, self).save(*args, **kwargs)

    def __unicode__(self):
        return "feedback " + str(self.create_time)
        

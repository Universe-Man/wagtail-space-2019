from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.embeds.blocks import EmbedBlock

# Create your models here.
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context['blogpages'] = BlogPage.objects.all().live().order_by('-date')
        # self.get_children()
        return context


class BlogPage(Page):
    date = models.DateField()
    intro = models.CharField(max_length=250)
    # body = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(icon='title')),
        ('paragraph', blocks.RichTextBlock(icon='pilcrow')),
        ('embed', EmbedBlock(icon='media'))
    ])

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

from django.views.generic import TemplateView


class ExampleView(TemplateView):
    template_name = "main_page.html"

    # def get(self, request, *args, **kwargs):
    #     import ipdb; ipdb.set_trace()
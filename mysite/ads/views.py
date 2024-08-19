from ads.forms import CreateForm
from ads.models import Ad
from ads.owner import OwnerCreateView
from ads.owner import OwnerDeleteView
from ads.owner import OwnerDetailView
from ads.owner import OwnerListView
from ads.owner import OwnerUpdateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy

FIELDS = ['title', 'price', 'text']
class AdListView(OwnerListView):
    model = Ad
    fields = ['title', 'price', 'text']
    # By convention:
    # template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    fields = FIELDS

class AdCreateView(OwnerCreateView):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = FIELDS


class AdDeleteView(OwnerDeleteView):
    model = Ad
    fields = FIELDS

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response

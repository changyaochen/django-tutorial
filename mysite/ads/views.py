from ads.models import Ad
from ads.owner import OwnerCreateView
from ads.owner import OwnerDeleteView
from ads.owner import OwnerDetailView
from ads.owner import OwnerListView
from ads.owner import OwnerUpdateView


class AdListView(OwnerListView):
    model = Ad
    fields_exclude = ['owner', 'created_at', 'updated_at']
    # By convention:
    # template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    fields_exclude = ['owner', 'created_at', 'updated_at']

class AdCreateView(OwnerCreateView):
    model = Ad
    # List the fields to copy from the Ad model to the Ad form
    fields = ['title', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields_exclude = ['owner', 'created_at', 'updated_at']


class AdDeleteView(OwnerDeleteView):
    model = Ad
    fields_exclude = ['owner', 'created_at', 'updated_at']

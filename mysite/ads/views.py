from ads.models import Ad
from ads.owner import OwnerCreateView
from ads.owner import OwnerDeleteView
from ads.owner import OwnerDetailView
from ads.owner import OwnerListView
from ads.owner import OwnerUpdateView

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
    model = Ad
    # List the fields to copy from the Ad model to the Ad form
    fields = FIELDS

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = FIELDS


class AdDeleteView(OwnerDeleteView):
    model = Ad
    fields = FIELDS

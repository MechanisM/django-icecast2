
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

import httplib

from icecast2.lib import Stat as IceCast2Stats

# Create your views here.

def mount_points(request):
    stats = IceCast2Stats(
        settings.ICECAST2_USERNAME,
        settings.ICECAST2_PASSWORD,
        settings.ICECAST2_URL
    )

    sources = stats.get_sources()

    res = HttpResponse(status=httplib.OK)
    res['Content-Type'] = 'application/xml'
    res.write(loader.render_to_string('icecast2/mount_points.html',
        {'items': sources})
    )

    return res

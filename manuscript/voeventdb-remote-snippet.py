import voeventdb.remote.apiv1 as apiv1
from astropy.coordinates import Angle, SkyCoord

# Define a search cone
cone_centre = SkyCoord(ra=149, dec=51, unit='deg')
cone_radius = Angle(3, unit='deg')

# Define a filter-set
my_filters = {
    apiv1.FilterKeys.cone: (cone_centre, cone_radius),
    apiv1.FilterKeys.ivorn_contains: 'BAT_GRB',
    apiv1.FilterKeys.role: 'observation',
}

# See how many results match our filter-set
n_results = apiv1.count(filters=my_filters)

# List all IVORNs for matching VOEvents, oldest first
matching_ivorns = apiv1.list_ivorn(
    filters=my_filters,
    order=apiv1.OrderValues.author_datetime,
)
# Fetch the raw XML for the first listed VOEvent
xml_content = apiv1.packet_xml(matching_ivorns[0])

